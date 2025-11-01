"""
recursion_domino_full.py
Final Recursion Domino Visualizer (Head vs Tail) - Full version

Features:
 - Fullscreen / auto-resize canvas
 - Auto-fit domino scaling
 - Correct head vs tail visual ordering (tail falls left->right)
 - Call stack visualization (push/pop)
 - Color-coded log panel
 - Educational description text
 - Speed control, Start / Pause / Step / Reset
"""

import tkinter as tk
from tkinter import ttk, messagebox
import math
import os

# ---------- Defaults ----------
DEFAULT_DOMINOES = 8
MAX_DOMINOES = 40
MIN_DOMINOES = 1

BG_COLOR = "#000000"
DOMINO_FILL = "#F3EDED"
DOMINO_BORDER = "#000000"
TEXT_COLOR = "#F04141"
LOG_BG = "#111111"
LOG_FG = "#DDDDDD"

BOTTOM_MARGIN_RATIO = 0.08  # fraction of canvas height for bottom margin
SIDE_PADDING = 20  # px padding on canvas sides
MIN_DOMINO_W = 12
DOMINO_ASPECT = 2.5  # height = width * aspect

# ---------- Geometry helpers ----------
def rotated_rect(cx, cy, w, h, angle_deg):
    a = math.radians(angle_deg)
    hw, hh = w / 2.0, h / 2.0
    corners = [(-hw, -hh), (hw, -hh), (hw, hh), (-hw, hh)]
    pts = []
    ca = math.cos(a); sa = math.sin(a)
    for x, y in corners:
        xr = x * ca - y * sa
        yr = x * sa + y * ca
        pts.append((cx + xr, cy + yr))
    return [coord for p in pts for coord in p]


# ---------- Domino class ----------
class Domino:
    def __init__(self, canvas, cx, cy, w, h, idx):
        self.canvas = canvas
        self.cx = cx
        self.cy = cy
        self.w = w
        self.h = h
        self.idx = idx
        self.angle = 0.0
        self.poly = canvas.create_polygon(rotated_rect(cx, cy, w, h, self.angle),
                                          fill=DOMINO_FILL, outline=DOMINO_BORDER, width=2)
        # center dividing line
        self.line = canvas.create_line(cx, cy - h/2 + 6, cx, cy + h/2 - 6,
                                       fill=DOMINO_BORDER, width=2)
        self.label = canvas.create_text(cx, cy + h/2 + 12, text=str(idx),
                                        fill=TEXT_COLOR, font=("Helvetica", 10))

    def set_angle(self, angle):
        self.angle = angle
        pts = rotated_rect(self.cx, self.cy, self.w, self.h, self.angle)
        self.canvas.coords(self.poly, *pts)
        # update centered vertical line endpoints after rotation
        a = math.radians(self.angle)
        dx = (self.h / 2.0 - 6) * math.sin(a)
        dy = (self.h / 2.0 - 6) * math.cos(a)
        x0, y0 = self.cx - dx, self.cy - dy
        x1, y1 = self.cx + dx, self.cy + dy
        self.canvas.coords(self.line, x0, y0, x1, y1)

    def reset(self):
        self.set_angle(0.0)


# ---------- Animator ----------
class RecursionAnimator:
    def __init__(self, canvas, log_widget, stack_listbox):
        self.canvas = canvas
        self.log = log_widget
        self.stack = stack_listbox
        self.dominoes = []
        self.events = []
        self.current_index = 0
        self.running = False
        self.after_id = None
        self.speed_ms = 60
        self.canvas_w = int(canvas.winfo_reqwidth())
        self.canvas_h = int(canvas.winfo_reqheight())

    # --- layout & domino creation (auto-fit) ---
    def setup_dominoes(self, n):
        self.stop()
        # delete old
        for d in self.dominoes:
            try:
                self.canvas.delete(d.poly)
                self.canvas.delete(d.line)
                self.canvas.delete(d.label)
            except:
                pass
        self.dominoes = []

        # compute current canvas size
        self.canvas.update_idletasks()
        self.canvas_w = max(200, self.canvas.winfo_width())
        self.canvas_h = max(120, self.canvas.winfo_height())

        bottom_margin = int(self.canvas_h * BOTTOM_MARGIN_RATIO)
        max_w = max(100, self.canvas_w - SIDE_PADDING * 2)

        # choose spacing and domino width to fit nicely
        spacing = 10
        total_spacing = (n - 1) * spacing
        avail_for_domino = max_w - total_spacing
        domino_w = max(MIN_DOMINO_W, avail_for_domino / n)
        domino_h = domino_w * DOMINO_ASPECT

        # if dominos would overflow vertically, clamp height
        max_domino_h = self.canvas_h * 0.7
        if domino_h > max_domino_h:
            domino_h = max_domino_h
            domino_w = domino_h / DOMINO_ASPECT

        total_width = n * domino_w + (n - 1) * spacing
        start_x = (self.canvas_w - total_width) / 2.0 + domino_w / 2.0
        y = self.canvas_h - bottom_margin - domino_h / 2.0

        for i in range(n):
            cx = start_x + i * (domino_w + spacing)
            d = Domino(self.canvas, cx, y, domino_w, domino_h, i + 1)
            self.dominoes.append(d)

        self.clear_log()
        self.clear_stack()

    # --- logging helpers ---
    def clear_log(self):
        self.log.config(state="normal")
        self.log.delete("1.0", "end")
        self.log.config(state="disabled")

    def append_log(self, text, tag=None):
        self.log.config(state="normal")
        if tag:
            self.log.insert("end", text + "\n", tag)
        else:
            self.log.insert("end", text + "\n")
        self.log.see("end")
        self.log.config(state="disabled")

    # --- stack helpers ---
    def push_stack(self, text):
        self.stack.insert("end", text)
        # keep last visible
        self.stack.yview_moveto(1.0)

    def pop_stack(self):
        last_index = self.stack.size() - 1
        if last_index >= 0:
            self.stack.delete(last_index)

    def clear_stack(self):
        self.stack.delete(0, "end")

    # --- event builders ---
    def build_events_head(self, n):
        """
        Head recursion model:
        Calls are pushed (call n, call n-1, ..., base)
        Processes happen on unwind: process 1..n (left->right)
        """
        self.events = []
        # push calls descending n..1
        for k in range(n, 0, -1):
            self.events.append(("call", k))
        self.events.append(("base", 0))
        # processes ascending 1..n
        for k in range(1, n + 1):
            self.events.append(("process", k))

    def build_events_tail(self, n):
        """
        Tail recursion model (visualized to fall left->right).
        We'll simulate calls that process each domino before next call:
        call(1), process(1), call(2), process(2), ..., base
        This demonstrates work before recursive call and makes dominoes fall left->right.
        """
        self.events = []
        for k in range(1, n + 1):
            self.events.append(("call", k))
            self.events.append(("process", k))
        self.events.append(("base", 0))

    # --- control flow: start / step / run / pause / reset ---
    def start(self, mode, n, speed_ms):
        self.stop()
        self.speed_ms = max(10, int(speed_ms))
        # prepare dominoes layout and events
        self.setup_dominoes(n)
        if mode == "head":
            self.build_events_head(n)
            self.append_log(f"[INFO] Mode: HEAD recursion (unwind -> fall)", "info")
        else:
            self.build_events_tail(n)
            self.append_log(f"[INFO] Mode: TAIL recursion (work before call -> fall left->right)", "info")

        # log trace summary
        trace = " ".join([f"{e[0]}{e[1]}" for e in self.events])
        self.append_log("Trace: " + trace, "info")

        self.current_index = 0
        self.running = True
        self._schedule_next()

    def _schedule_next(self):
        if not self.running:
            return
        self.after_id = self.canvas.after(self.speed_ms, self._step)

    def _step(self):
        if not self.running:
            return
        if self.current_index >= len(self.events):
            self.append_log("[INFO] Done.", "info")
            self.running = False
            return

        ev, idx = self.events[self.current_index]
        # handle events
        if ev == "call":
            # push stack frame
            self.append_log(f"[CALL] recurse({idx})", "call")
            self.push_stack(f"recurse({idx})")
        elif ev == "process":
            # show process and animate domino
            self.append_log(f"[PROCESS] processing({idx})", "proc")
            # animate domino: index is 1..n mapped to 0..n-1
            domino_index = idx - 1
            self.animate_domino_fall(domino_index)
            # pop stack for non-head immediate pop (for tail we popped here; for head we'll pop on process too)
            # We'll pop only if top matches this frame; ensures correct stack visualization
            if self.stack.size() > 0:
                top_txt = self.stack.get(self.stack.size() - 1)
                if top_txt == f"recurse({idx})":
                    self.pop_stack()
        elif ev == "base":
            self.append_log("[BASE] base case reached", "base")
        self.current_index += 1
        self._schedule_next()

    def step_once(self):
        """Manual step (pauses running if running)."""
        if self.running:
            # pause
            if self.after_id:
                try:
                    self.canvas.after_cancel(self.after_id)
                except:
                    pass
                self.after_id = None
            self.running = False

        if self.current_index >= len(self.events):
            self.append_log("[INFO] No more events.", "info")
            return

        ev, idx = self.events[self.current_index]
        if ev == "call":
            self.append_log(f"[CALL] recurse({idx})", "call")
            self.push_stack(f"recurse({idx})")
        elif ev == "process":
            self.append_log(f"[PROCESS] processing({idx})", "proc")
            domino_index = idx - 1
            self.animate_domino_fall(domino_index)
            # pop if matches
            if self.stack.size() > 0:
                top_txt = self.stack.get(self.stack.size() - 1)
                if top_txt == f"recurse({idx})":
                    self.pop_stack()
        elif ev == "base":
            self.append_log("[BASE] base case reached", "base")
        self.current_index += 1

    def animate_domino_fall(self, idx):
        if idx < 0 or idx >= len(self.dominoes):
            return
        d = self.dominoes[idx]
        if d.angle > 5:
            return  # already fallen

        steps = 12
        delay = max(6, int(self.speed_ms / 8))

        def step(i):
            ang = (i / steps) * 85.0
            d.set_angle(ang)
            if i < steps:
                self.canvas.after(delay, lambda: step(i + 1))

        step(0)

    def pause(self):
        if self.after_id:
            try:
                self.canvas.after_cancel(self.after_id)
            except:
                pass
            self.after_id = None
        self.running = False

    def stop(self):
        self.pause()

    def reset(self):
        self.stop()
        for d in self.dominoes:
            d.reset()
        self.dominoes = []
        self.events = []
        self.current_index = 0
        self.clear_log()
        self.clear_stack()


# ---------- GUI App ----------
class App:
    def __init__(self, root):
        self.root = root
        root.title("Recursion Visualizer — Dominoes (Final)")
        root.configure(bg=BG_COLOR)
        # allow resizing and fullscreen
        root.rowconfigure(1, weight=1)
        root.columnconfigure(0, weight=1)

        self.build_ui()
        # instantiate animator with references to widgets
        self.anim = RecursionAnimator(self.canvas, self.log_text, self.stack_listbox)
        # default setup
        self.domino_count_var.set(DEFAULT_DOMINOES)
        self.on_resize()  # initial layout

    def build_ui(self):
        # Top control frame
        top = ttk.Frame(self.root)
        top.grid(row=0, column=0, sticky="ew", padx=8, pady=6)
        top.columnconfigure(6, weight=1)

        # Mode selection
        ttk.Label(top, text="Mode:", background=BG_COLOR, foreground=TEXT_COLOR).grid(row=0, column=0, sticky="w")
        self.mode_var = tk.StringVar(value="head")
        ttk.Radiobutton(top, text="Head", variable=self.mode_var, value="head").grid(row=0, column=1, sticky="w", padx=(4,0))
        ttk.Radiobutton(top, text="Tail", variable=self.mode_var, value="tail").grid(row=0, column=2, sticky="w", padx=(4,8))

        # Domino count
        ttk.Label(top, text="Dominoes:", background=BG_COLOR, foreground=TEXT_COLOR).grid(row=0, column=3, sticky="w")
        self.domino_count_var = tk.StringVar()
        spin = ttk.Spinbox(top, from_=MIN_DOMINOES, to=MAX_DOMINOES, textvariable=self.domino_count_var, width=6)
        spin.grid(row=0, column=4, sticky="w", padx=(4,8))

        # Speed
                # Speed
        ttk.Label(top, text="Speed:", background=BG_COLOR, foreground=TEXT_COLOR).grid(row=0, column=5, sticky="w")
        
        self.speed_var = tk.IntVar(value=60)
        
        # Percent label updater
        def update_speed_label(value):
            speed_percent_label.config(text=f"{int(float(value))}%")
        
        # Speed scale with live % display
        speed_scale = ttk.Scale(
            top, from_=10, to=240, orient="horizontal",
            variable=self.speed_var, command=update_speed_label
        )
        speed_scale.grid(row=0, column=6, sticky="ew", padx=(4,8))
        top.columnconfigure(6, weight=1)
        
        # Label showing current % value
        speed_percent_label = ttk.Label(top, text=f"{self.speed_var.get()}%", background=BG_COLOR, foreground=TEXT_COLOR)
        speed_percent_label.grid(row=0, column=7, sticky="w", padx=(6, 0))
        
        # Direction hints
        ttk.Label(top, text="← Faster", background=BG_COLOR, foreground=TEXT_COLOR).grid(row=1, column=5, sticky="w", pady=(0,2))
        ttk.Label(top, text="Slower →", background=BG_COLOR, foreground=TEXT_COLOR).grid(row=1, column=6, sticky="e", pady=(0,2))
        
        # Buttons
        btn_frame = ttk.Frame(top)
        btn_frame.grid(row=0, column=7, sticky="e")
        ttk.Button(btn_frame, text="Start", command=self.on_start).grid(row=0, column=0, padx=4)
        ttk.Button(btn_frame, text="Pause", command=self.on_pause).grid(row=0, column=1, padx=4)
        ttk.Button(btn_frame, text="Step", command=self.on_step).grid(row=0, column=2, padx=4)
        ttk.Button(btn_frame, text="Reset", command=self.on_reset).grid(row=0, column=3, padx=4)
        ttk.Button(btn_frame, text="Back", command=self.back).grid(row=0, column=4, padx=4)

        # Middle: canvas (left) + stack & description (right)
        middle = ttk.Frame(self.root)
        middle.grid(row=1, column=0, sticky="nsew", padx=8, pady=6)
        middle.rowconfigure(0, weight=1)
        middle.columnconfigure(0, weight=1)
        middle.columnconfigure(1, weight=0)

        # Canvas area
        canvas_frame = ttk.Frame(middle)
        canvas_frame.grid(row=0, column=0, sticky="nsew")
        canvas_frame.rowconfigure(0, weight=1)
        canvas_frame.columnconfigure(0, weight=1)
        self.canvas = tk.Canvas(canvas_frame, bg=BG_COLOR, highlightthickness=0)
        self.canvas.grid(row=0, column=0, sticky="nsew")
        # bind resize to recalc layout
        self.canvas.bind("<Configure>", lambda e: self.on_resize())

        # Right side control: stack and info
        right = ttk.Frame(middle, width=260)
        right.grid(row=0, column=1, sticky="ns", padx=(8,0))
        ttk.Label(right, text="Call Stack", background=BG_COLOR, foreground=TEXT_COLOR).pack(anchor="w")
        self.stack_listbox = tk.Listbox(right, height=10)
        self.stack_listbox.pack(fill="x", pady=(4,8))

        ttk.Label(right, text="Explanation", background=BG_COLOR, foreground=TEXT_COLOR).pack(anchor="w")
        expl = tk.Text(right, height=9, wrap="word", bg=LOG_BG, fg=LOG_FG)
        expl.insert("1.0",
"""What you see:
- Each domino = one recursive call/frame.
- CALL = pushing a new frame onto the call stack.
- PROCESS = the frame does its work and the domino falls.
- HEAD recursion: work happens on unwinding (dominoes fall left->right).
- TAIL recursion: work happens before the recursive call (dominoes fall left->right here too).
Use Speed & Dominoes controls to experiment.
""")
        expl.config(state="disabled")
        expl.pack(fill="both", expand=False, pady=(4,8))

        # Bottom: log
        bottom = ttk.Frame(self.root)
        bottom.grid(row=2, column=0, sticky="ew", padx=8, pady=(0,8))
        ttk.Label(bottom, text="Trace / Console:", background=BG_COLOR, foreground=TEXT_COLOR).pack(anchor="w")
        self.log_text = tk.Text(bottom, height=8, bg=LOG_BG, fg=LOG_FG, state="disabled", wrap="word")
        self.log_text.pack(fill="both", expand=True, pady=(4,0))

        # configure log tags for colors
        self.log_text.tag_configure("call", foreground="#66c2ff")   # blue-ish
        self.log_text.tag_configure("proc", foreground="#98fb98")   # green-ish
        self.log_text.tag_configure("base", foreground="#ffcc66")   # amber
        self.log_text.tag_configure("info", foreground="#dddddd")   # light gray

        # style tweaks for background colors
        style = ttk.Style()
        try:
            style.configure("TFrame", background=BG_COLOR)
            style.configure("TLabel", background=BG_COLOR, foreground=TEXT_COLOR)
            style.configure("TButton", background=BG_COLOR, foreground=TEXT_COLOR)
        except:
            pass

        # full-screen toggle key
        self.root.bind("<F11>", lambda e: self.toggle_fullscreen())
        self.root.bind("<Escape>", lambda e: self.exit_fullscreen())

    # ---------- UI callbacks ----------
    def on_start(self):
        # validate domino count
        try:
            n = int(self.domino_count_var.get())
        except Exception:
            messagebox.showerror("Invalid input", f"Please enter a number between {MIN_DOMINOES} and {MAX_DOMINOES}.")
            return
        if n < MIN_DOMINOES or n > MAX_DOMINOES:
            messagebox.showerror("Invalid input", f"Please enter a number between {MIN_DOMINOES} and {MAX_DOMINOES}.")
            return

        mode = self.mode_var.get()
        speed = self.speed_var.get()
        self.anim.start(mode, n, speed)

    def on_pause(self):
        self.anim.pause()
        self.anim.append_log("[INFO] Paused.", "info")

    def on_step(self):
        self.anim.step_once()

    def on_reset(self):
        self.anim.reset()
        self.anim.append_log("[INFO] Reset.", "info")
    
    def back(self):
        root.withdraw()
        os.system("python options.py")
        root.destroy()

    def on_resize(self):
        # recompute canvas and re-layout dominoes if any
        # preserve current domino count setting to rebuild layout only if necessary
        try:
            n = int(self.domino_count_var.get())
            n = max(MIN_DOMINOES, min(MAX_DOMINOES, n))
        except:
            n = DEFAULT_DOMINOES
        # rebuild layout to fit new size, but don't reset animation state
        # We'll preserve fallen angles: capture angles if exist, rebuild dominoes, then restore angles.
        old_angles = []
        for d in self.anim.dominoes:
            old_angles.append(d.angle)
        # create new domino layout
        self.anim.setup_dominoes(n)
        # restore angles as far as possible
        for i, angle in enumerate(old_angles):
            if i < len(self.anim.dominoes):
                self.anim.dominoes[i].set_angle(angle)


# ---------- Run ----------
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.geometry("1100x780")
    root.state("zoomed")
    root.mainloop()
