from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sys

window = Tk()

# Runs the Main Menu
def main():
    create_background()
    window.state("zoomed")
    window.title("CC 2103 Project")
    icon = PhotoImage(file='hacker06.png')
    window.iconphoto(True, icon)
    window.config(bg='#12245A')

    title = Label(window, text="Learn from Gaming", font=('Fixedsys', 70, 'bold'), fg='#EEEEEE', bg='#12245A')
    title.place(x=350, y=100)

    start_btn = Button(window, text='Start', width=15)
    start_btn.config(font=('Fixedsys', 30, 'bold'),
                    bg='#A9595C',
                    fg='#EEEEEE',
                    activebackground='#12245A',
                    activeforeground='#EEEEEE')
    start_btn.place(x=610, y=400)
    start_btn.config(command=start_pressed)

    member_btn = Button(window, text='Members', width=15)
    member_btn.config(font=('Fixedsys', 30, 'bold'),
                    bg='#60709C',
                    fg='#EEEEEE',
                    activebackground='#12245A',
                    activeforeground='#EEEEEE')
    member_btn.place(x=610, y=500)


    exit_btn = Button(window, text='Exit', width=15)
    exit_btn.config(font=('Fixedsys', 30, 'bold'),
                    bg='#60709C',
                    fg='#EEEEEE',
                    activebackground='#12245A',
                    activeforeground='#EEEEEE')
    exit_btn.place(x=610, y=600)
    exit_btn.config(command=window.destroy)
    
    # Use to run the code
    window.mainloop()

# Example follow-up function to run after clearing the screen
def after_start_action():
    # Choices
    title = Label(window, text="Choose One", font=('Fixedsys', 70, 'bold'), fg='#EEEEEE', bg='#12245A')
    title.place(x=520, y=100)

    # Linked List Button
    recursion_btn = Button(window, text='Recursion', width=15)
    recursion_btn.config(font=('Fixedsys', 30, 'bold'),
                         bg='#60709C',
                         fg='#EEEEEE',
                         activebackground='#12245A',
                         activeforeground='#EEEEEE')
    recursion_btn.place(x=610, y=300)
    recursion_btn.config(command=recursion_window)

    # Linked List Button
    linked_list_btn = Button(window, text='Linked List', width=15)
    linked_list_btn.config(font=('Fixedsys', 30, 'bold'),
                         bg='#60709C',
                         fg='#EEEEEE',
                         activebackground='#12245A',
                         activeforeground='#EEEEEE')
    linked_list_btn.place(x=610, y=400)
    linked_list_btn.config(command=linked_list_window)

    # Stack Button
    stack_btn = Button(window, text='Stack', width=15)
    stack_btn.config(font=('Fixedsys', 30, 'bold'),
                         bg='#60709C',
                         fg='#EEEEEE',
                         activebackground='#12245A',
                         activeforeground='#EEEEEE')
    stack_btn.place(x=610, y=500)
    stack_btn.config(command=stack_window)
    
    back_main()
    
def recursion_window():
    # remove background then clear (so recursion screen has no BG)
    destroy_background()
    clear()
    # --- Configuration ---
    BG_COLOR = "#0D1B2A"  # Dark Blue
    FG_COLOR = "#E0E1DD"  # Light Gray
    BTN_COLOR = "#E76F51" # Red/Orange
    BTN_FG = "#FFFFFF"
    INPUT_BG = "#1B263B"
    TEXT_BG = "#1B263B"

    # Set higher recursion limit for deep computations
    sys.setrecursionlimit(2000)

    # --- Logic for all Recursion Algorithms ---
    # This class demonstrates different STRUCTURES of recursion
    class RecursionLogic:
        def __init__(self):
            self.steps = []

        def _indent(self, level):
            """Helper to create indentation for visualizing the stack."""
            return "  " * level

        # --- 1. Linear Recursion (e.g., Sum of n) ---
        def _linear_recursion(self, n, level):
            indent = self._indent(level)
            if n == 1:
                self.steps.append(f"{indent}Base Case: linear_sum(1) = 1")
                return 1
            else:
                self.steps.append(f"{indent}Call: linear_sum({n}) = {n} + linear_sum({n-1})")
                result = n + self._linear_recursion(n - 1, level + 1)
                self.steps.append(f"{indent}Return: {n} + {result - n} = {result}")
                return result

        # --- 2. Tail Recursion (e.g., Factorial with accumulator) ---
        def _tail_recursion(self, n, acc, level):
            indent = self._indent(level)
            if n == 0:
                self.steps.append(f"{indent}Base Case: tail_fact(0, {acc}) = {acc}")
                return acc
            else:
                self.steps.append(f"{indent}Call: tail_fact({n}, {acc}) -> tail_fact({n-1}, {n} * {acc})")
                result = self._tail_recursion(n - 1, n * acc, level + 1)
                self.steps.append(f"{indent}Return: {result}")
                return result

        # --- 3. Tree Recursion (e.g., Fibonacci) ---
        def _tree_recursion(self, n, level):
            indent = self._indent(level)
            if n <= 1:
                self.steps.append(f"{indent}Base Case: tree_fib({n}) = {n}")
                return n
            else:
                self.steps.append(f"{indent}Call: tree_fib({n}) = tree_fib({n-1}) + tree_fib({n-2})")
                self.steps.append(f"{indent} -> Computing tree_fib({n-1})...")
                res1 = self._tree_recursion(n - 1, level + 1)
                self.steps.append(f"{indent} -> Computing tree_fib({n-2})...")
                res2 = self._tree_recursion(n - 2, level + 1)
                result = res1 + res2
                self.steps.append(f"{indent}Return: tree_fib({n}) = {res1} + {res2} = {result}")
                return result
                
        # --- 4. Nested Recursion (e.g., Ackermann Function) ---
        def _nested_recursion(self, m, n, level):
            indent = self._indent(level)
            self.steps.append(f"{indent}Call: A({m}, {n})")
            if m == 0:
                result = n + 1
                self.steps.append(f"{indent}Base Case 1: A(0, {n}) = {n} + 1 = {result}")
                return result
            elif n == 0:
                self.steps.append(f"{indent}Base Case 2: A({m}, 0) = A({m-1}, 1)")
                result = self._nested_recursion(m - 1, 1, level + 1)
                self.steps.append(f"{indent}Return: {result}")
                return result
            else:
                self.steps.append(f"{indent}Recursive Call: A({m}, {n}) = A({m-1}, A({m}, {n-1}))")
                self.steps.append(f"{indent} -> Inner Call: A({m}, {n-1})")
                inner_result = self._nested_recursion(m, n - 1, level + 1)
                self.steps.append(f"{indent} -> Outer Call: A({m-1}, {inner_result})")
                outer_result = self._nested_recursion(m - 1, inner_result, level + 1)
                self.steps.append(f"{indent}Return: {outer_result}")
                return outer_result

        # --- 5. Mutual Recursion (e.g., IsEven/IsOdd) ---
        def _mutual_is_even(self, n, level):
            indent = self._indent(level)
            self.steps.append(f"{indent}Call: is_even({n})?")
            if n == 0:
                self.steps.append(f"{indent}Base Case: is_even(0) = True")
                return True
            else:
                self.steps.append(f"{indent} -> Call: is_odd({n-1})")
                return self._mutual_is_odd(n - 1, level + 1)

        def _mutual_is_odd(self, n, level):
            indent = self._indent(level)
            self.steps.append(f"{indent}Call: is_odd({n})?")
            if n == 0:
                self.steps.append(f"{indent}Base Case: is_odd(0) = False")
                return False
            else:
                self.steps.append(f"{indent} -> Call: is_even({n-1})")
                return self._mutual_is_even(n - 1, level + 1)

        # --- 6. Indirect Recursion (e.g., A -> B -> C -> A) ---
        def _indirect_A(self, n, level):
            indent = self._indent(level)
            self.steps.append(f"{indent}Call: indirect_A({n})")
            if n > 0:
                self.steps.append(f"{indent} -> Call: indirect_B({n-1})")
                self._indirect_B(n - 1, level + 1)
            self.steps.append(f"{indent}Return: indirect_A({n})")

        def _indirect_B(self, n, level):
            indent = self._indent(level)
            self.steps.append(f"{indent}Call: indirect_B({n})")
            if n > 0:
                self.steps.append(f"{indent} -> Call: indirect_C({n-1})")
                self._indirect_C(n - 1, level + 1)
            self.steps.append(f"{indent}Return: indirect_B({n})")

        def _indirect_C(self, n, level):
            indent = self._indent(level)
            self.steps.append(f"{indent}Call: indirect_C({n})")
            if n > 0:
                self.steps.append(f"{indent} -> Call: indirect_A({n-1})")
                self._indirect_A(n - 1, level + 1)
            self.steps.append(f"{indent}Return: indirect_C({n})")

        # --- 7. Head Recursion (e.g., Print 1-to-n) ---
        def _head_recursion(self, n, level):
            indent = self._indent(level)
            if n == 0:
                self.steps.append(f"{indent}Base Case: head_print(0)")
                return
            else:
                self.steps.append(f"{indent}Call: head_print({n})")
                self.steps.append(f"{indent} -> Recursive Call: head_print({n-1})")
                self._head_recursion(n - 1, level + 1)
                self.steps.append(f"{indent}Return: Processing {n} (e.g., print {n})")
                return
                
        # --- Main Compute Function (Tracing) ---
        def compute(self, algo, val1, val2=None):
            self.steps = []
            try:
                if algo == "Linear":
                    if val1 < 1: self.steps.append("Input must be >= 1"); return self.steps
                    result = self._linear_recursion(val1, 0)
                    self.steps.append(f"\nFinal Result: linear_sum({val1}) = {result}")
                
                elif algo == "Tail":
                    if val1 < 0: self.steps.append("Input must be >= 0"); return self.steps
                    result = self._tail_recursion(val1, 1, 0)
                    self.steps.append(f"\nFinal Result: tail_fact({val1}) = {result}")
                
                elif algo == "Tree":
                    if val1 < 0: self.steps.append("Input must be >= 0"); return self.steps
                    result = self._tree_recursion(val1, 0)
                    self.steps.append(f"\nFinal Result: tree_fib({val1}) = {result}")

                elif algo == "Nested":
                    if val1 < 0 or val2 < 0: self.steps.append("Inputs must be >= 0"); return self.steps
                    result = self._nested_recursion(val1, val2, 0)
                    self.steps.append(f"\nFinal Result: A({val1}, {val2}) = {result}")

                elif algo == "Mutual":
                    if val1 < 0: self.steps.append("Input must be >= 0"); return self.steps
                    result = self._mutual_is_even(val1, 0)
                    self.steps.append(f"\nFinal Result: is_even({val1})? -> {result}")

                elif algo == "Indirect":
                    if val1 < 0: self.steps.append("Input must be >= 0"); return self.steps
                    self._indirect_A(val1, 0)
                    self.steps.append(f"\nFinal Result: Indirect chain for n={val1} complete.")

                elif algo == "Head":
                    if val1 < 0: self.steps.append("Input must be >= 0"); return self.steps
                    self._head_recursion(val1, 0)
                    self.steps.append(f"\nFinal Result: Head processing for n={val1} complete.")

                else:
                    self.steps.append("Error: Please select an algorithm.")
                    
            except RecursionError:
                self.steps.append("\n---!! STACK OVERFLOW !!---")
                self.steps.append(f"Input '{val1}' is too large for this Python recursion limit.")
            except Exception as e:
                self.steps.append(f"\nAn error occurred: {e}")
                
            return self.steps
            
        # --- Fast, non-tracing versions for large numbers ---
        def fast_linear(self, n):
            if n == 1: return 1
            return n + self.fast_linear(n-1)

        def fast_tail(self, n, acc=1):
            if n == 0: return acc
            return self.fast_tail(n-1, n * acc)

        def fast_tree(self, n):
            if n <= 1: return n
            return self.fast_tree(n-1) + self.fast_tree(n-2)
        
        def fast_nested(self, m, n):
            if m == 0: return n + 1
            if n == 0: return self.fast_nested(m - 1, 1)
            # Use a loop-based stack to avoid Python's recursion limit
            stack = [m]
            while stack:
                m = stack.pop()
                if m == 0:
                    n = n + 1
                elif n == 0:
                    stack.append(m - 1)
                    n = 1
                else:
                    stack.append(m - 1)
                    stack.append(m)
                    n = n - 1
            return n

        def fast_mutual_even(self, n):
            if n == 0: return True
            return self.fast_mutual_odd(n-1)
        
        def fast_mutual_odd(self, n):
            if n == 0: return False
            return self.fast_mutual_even(n-1)

    # --- Main Application Class ---
    class App(Frame):
        def __init__(self, master):
            super().__init__(master)
            self.master = master
            self.master.title("Recursion Learning Tool")
            self.master.geometry("900x600")
            self.master.configure(bg=BG_COLOR)

            container = Frame(self.master, bg=BG_COLOR)
            container.pack(side="top", fill="both", expand=True)
            container.grid_rowconfigure(0, weight=1)
            container.grid_columnconfigure(0, weight=1)

            self.frames = {}
            for F in (WelcomeFrame, MainFrame):
                frame = F(container, self)
                self.frames[F] = frame
                frame.grid(row=0, column=0, sticky="nsew")

            self.show_frame(WelcomeFrame)

        def show_frame(self, cont):
            frame = self.frames[cont]
            frame.tkraise()
            if cont == WelcomeFrame:
                frame.start_animation()

    # --- Welcome Screen Frame ---
    class WelcomeFrame(Frame):
        def __init__(self, parent, controller):
            super().__init__(parent, bg=BG_COLOR)
            self.controller = controller
            
            self.label = Label(self, text="Welcome", fg="white", bg=BG_COLOR,
                                font=("Helvetica", 60, "bold"))
            self.label.place(relx=0.5, rely=0.5, anchor="center")
            
            self.label.config(fg=BG_COLOR)
            self.alpha = 0

        def start_animation(self):
            self.alpha = 0
            self.label.config(fg=BG_COLOR)
            self.animate()

        def animate(self):
            if self.alpha < 255:
                self.alpha += 5
                color = f'#{self.alpha:02x}{self.alpha:02x}{self.alpha:02x}'
                if self.alpha > 224: 
                    color = FG_COLOR
                
                self.label.config(fg=color)
                self.after(20, self.animate)
            else:
                self.after(1000, lambda: self.controller.show_frame(MainFrame))

    # --- Main Application Frame ---
    class MainFrame(Frame):
        def __init__(self, parent, controller):
            super().__init__(parent, bg=BG_COLOR)
            self.controller = controller
            self.logic = RecursionLogic()
            
            # --- NEW: State variables for animation control ---
            self.step_animation_id = None 
            self.current_steps = []
            self.current_step_index = 0

            self.descriptions = {
                "Linear": "One recursive call. The function does its processing on the way 'down' or 'up' the stack.",
                "Tail": "One recursive call, which is the VERY last action. Allows for optimization (in some languages).",
                "Tree": "Multiple recursive calls (e.g., two or more). Creates a branching, tree-like structure of calls.",
                "Nested": "A recursive call is passed as an argument to another recursive call. (e.g., Ackermann).",
                "Mutual": "Two or more functions call each other in a cycle.",
                "Indirect": "A function calls another, which calls another... eventually leading back to the first function.",
                "Head": "The recursive call is the first operation. All processing happens *after* the call returns (on the way 'up')."
            }

            # Configure main grid
            self.columnconfigure(0, weight=1, minsize=300)
            self.columnconfigure(1, weight=3)
            self.rowconfigure(0, weight=1)

            # --- Left Panel: Controls ---
            control_frame = Frame(self, bg=BG_COLOR, bd=10)
            control_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
            control_frame.columnconfigure(0, weight=1)

            welcome_label = Label(control_frame, text="Recursion Learning",
                                    font=("Helvetica", 20, "bold"), bg=BG_COLOR, fg=FG_COLOR)
            welcome_label.grid(row=0, column=0, pady=10, sticky="w")
            
            info_label = Label(control_frame,
                                text="Recursion is a process where a function calls itself to solve a smaller version of the problem.",
                                font=("Helvetica", 10), bg=BG_COLOR, fg=FG_COLOR, wraplength=280, justify="left")
            info_label.grid(row=1, column=0, pady=(0, 20), sticky="w")
            
            # Dropdown
            ttk.Label(control_frame, text="Choose a recursion type:").grid(row=2, column=0, sticky="w", pady=(10,0))
            self.algo_list = [
                "Linear", "Tail", "Tree", "Nested",
                "Mutual", "Indirect", "Head"
            ]
            self.algo_var = StringVar()
            self.dropdown = ttk.Combobox(control_frame, textvariable=self.algo_var,
                                        values=self.algo_list, state="readonly", width=30)
            self.dropdown.grid(row=3, column=0, sticky="ew", pady=5)
            self.dropdown.bind("<<ComboboxSelected>>", self.on_algo_select)
            
            self.description_label = Message(control_frame, text="Select a recursion type to see its definition.", 
                                                width=280, font=("Helvetica", 10, "italic"), 
                                                bg=BG_COLOR, fg=FG_COLOR, justify="left")
            self.description_label.grid(row=4, column=0, sticky="ew", pady=(5, 10))

            # --- Input Fields (Dynamic) ---
            self.entry1_label = ttk.Label(control_frame, text="Enter integer 'n':")
            self.entry1_label.grid(row=5, column=0, sticky="w", pady=(10,0))
            self.entry1_var = StringVar()
            self.entry1 = ttk.Entry(control_frame, textvariable=self.entry1_var, width=33)
            self.entry1.grid(row=6, column=0, sticky="ew", pady=5)

            self.entry2_label = ttk.Label(control_frame, text="Enter integer 'n':")
            self.entry2_var = StringVar()
            self.entry2 = ttk.Entry(control_frame, textvariable=self.entry2_var, width=33)
            self.entry2_row = 8 

            # --- NEW: Checkbox for animation ---
            self.show_animation_var = BooleanVar(value=True)
            self.animation_check = ttk.Checkbutton(control_frame, 
                                                text="Show step-by-step animation",
                                                variable=self.show_animation_var,
                                                style="TCheckbutton")
            self.animation_check.grid(row=9, column=0, sticky="w", pady=5)

            # Compute Button
            self.compute_button = ttk.Button(control_frame, text="Compute", 
                                            command=self.start_computation, style="Large.TButton")
            self.compute_button.grid(row=10, column=0, sticky="ew", pady=20)
            
            # Back Button
            back_button = ttk.Button(control_frame, text="Back to Welcome",
                                    command=lambda: controller.show_frame(WelcomeFrame))
            back_button.grid(row=11, column=0, sticky="ew", pady=(50, 0))

            # --- Right Panel: Output ---
            output_frame = Frame(self, bg=BG_COLOR, bd=10)
            output_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
            output_frame.rowconfigure(1, weight=1)
            output_frame.columnconfigure(0, weight=1)

            ttk.Label(output_frame, text="Computation Process:", 
                    font=("Helvetica", 16, "bold")).grid(row=0, column=0, sticky="w", pady=5)
            
            self.process_text = Text(output_frame, height=20, width=60, 
                                        font=("Courier New", 11),
                                        bg=TEXT_BG, fg=FG_COLOR, wrap=NONE,
                                        state='disabled', relief="solid", bd=1)
            
            yscroll = ttk.Scrollbar(output_frame, orient=VERTICAL, command=self.process_text.yview)
            xscroll = ttk.Scrollbar(output_frame, orient=HORIZONTAL, command=self.process_text.xview)
            self.process_text.configure(yscrollcommand=yscroll.set, xscrollcommand=xscroll.set)
            
            self.process_text.grid(row=1, column=0, sticky="nsew")
            yscroll.grid(row=1, column=1, sticky="ns")
            xscroll.grid(row=2, column=0, sticky="ew")

            # --- Style Configuration ---
            self.style_widgets()
            self.on_algo_select(None) 

        def style_widgets(self):
            s = ttk.Style()
            s.theme_use('clam')
            s.configure('.', background=BG_COLOR, foreground=FG_COLOR, fieldbackground=INPUT_BG, bordercolor="#888")
            s.map('.', 
                foreground=[('disabled', '#777'), ('active', FG_COLOR)],
                background=[('disabled', '#444'), ('active', INPUT_BG)],
                fieldbackground=[('disabled', '#444')])
            s.configure('TButton', background=BTN_COLOR, foreground=BTN_FG, 
                        font=('Helvetica', 11, 'bold'), padding=5, borderwidth=0)
            s.map('TButton',
                background=[('active', '#F4A261')],
                foreground=[('active', BTN_FG)])
            s.configure('Large.TButton', font=('Helvetica', 14, 'bold'), padding=10)
            s.configure('TCombobox', font=('Helvetica', 11), padding=5)
            self.option_add('*TCombobox*Listbox.background', INPUT_BG)
            self.option_add('*TCombobox*Listbox.foreground', FG_COLOR)
            self.option_add('*TCombobox*Listbox.selectBackground', BTN_COLOR)
            s.configure('TLabel', font=('Helvetica', 11), padding=2)
            s.configure('TEntry', font=('Helvetica', 11), padding=5, borderwidth=1, relief="solid",
                        foreground=FG_COLOR, insertcolor=FG_COLOR)
            
            # --- NEW: Style for Checkbutton ---
            s.configure('TCheckbutton', font=('Helvetica', 10), padding=5)
            s.map('TCheckbutton',
                indicatorbackground=[('selected', BTN_COLOR), ('!selected', INPUT_BG)],
                indicatorforeground=[('selected', FG_COLOR), ('!selected', FG_COLOR)])
            
        def on_algo_select(self, event):
            """Shows/hides second entry and updates description."""
            algo = self.algo_var.get()
            
            description = self.descriptions.get(algo, "Select a recursion type to see its definition.")
            self.description_label.config(text=description)
            
            if algo == "Nested":
                self.entry1_label.config(text="Enter integer 'm':")
                self.entry2_label.config(text="Enter integer 'n':")
                self.entry2_label.grid(row=self.entry2_row-1, column=0, sticky="w", pady=(10,0))
                self.entry2.grid(row=self.entry2_row, column=0, sticky="ew", pady=5)
            else:
                self.entry1_label.config(text="Enter integer 'n':")
                self.entry2_label.grid_remove()
                self.entry2.grid_remove()

        def start_computation(self):
            """Validates input and starts the step-by-step animation or instant compute."""
            
            # --- MODIFIED: Always stop previous run ---
            self.finish_computation() # Stops any existing animation
                
            self.process_text.config(state='normal')
            self.process_text.delete('1.0', END)
            self.process_text.config(state='disabled')
            
            algo = self.algo_var.get()
            val1_str = self.entry1_var.get()
            val2_str = self.entry2_var.get()
            
            if not algo:
                messagebox.showerror("Input Error", "Please select an algorithm.")
                return
            
            try:
                val1 = int(val1_str)
            except ValueError:
                messagebox.showerror("Input Error", f"Invalid input for first box: '{val1_str}'. Must be an integer.")
                return

            val2 = None
            if algo == "Nested":
                try:
                    val2 = int(val2_str)
                except ValueError:
                    messagebox.showerror("Input Error", f"Invalid input for second box: '{val2_str}'. Must be an integer.")
                    return
                
            # --- Instant Process Logic for large numbers ---
            thresholds = {
                "Linear": 100, "Tail": 100, "Tree": 25,
                "Mutual": 100, "Indirect": 50, "Head": 100
            }
            nested_thresholds = (3, 5) 
            
            is_large = False
            if algo == "Nested":
                m, n = val1, val2
                m_thresh, n_thresh = nested_thresholds
                if (m > m_thresh) or (m == m_thresh and n > n_thresh):
                    is_large = True
            elif algo in thresholds:
                if val1 > thresholds[algo]:
                    is_large = True
            
            if is_large:
                self.process_text.config(state='normal')
                self.process_text.insert(END, f"Input is large. Skipping animation...\nComputing final result instantly.\n\n")
                self.process_text.config(state='disabled')
                self.update_idletasks()
                
                try:
                    result = None
                    if algo == "Linear": result = self.logic.fast_linear(val1)
                    elif algo == "Tail": result = self.logic.fast_tail(val1)
                    elif algo == "Tree": result = self.logic.fast_tree(val1)
                    elif algo == "Nested": result = self.logic.fast_nested(val1, val2)
                    elif algo == "Mutual": result = self.logic.fast_mutual_even(val1)
                    elif algo == "Indirect": result = f"Process for n={val1} is too long to display."
                    elif algo == "Head": result = f"Process for n={val1} is too long to display."
                    
                    self.process_text.config(state='normal')
                    self.process_text.insert(END, f"Final Result: {result}\n")
                    
                except RecursionError:
                    self.process_text.config(state='normal')
                    self.process_text.insert(END, "\n---!! STACK OVERFLOW !!---\nInput is too large.")
                except Exception as e:
                    self.process_text.config(state='normal')
                    self.process_text.insert(END, f"\nAn error occurred: {e}")
                
                self.process_text.config(state='disabled')
                
            else:
                # --- MODIFIED: Animate or Instant-Show for small numbers ---
                steps = self.logic.compute(algo, val1, val2)
                
                if self.show_animation_var.get():
                    # Animate
                    self.current_steps = steps
                    self.current_step_index = 0
                    self.compute_button.config(text="Stop & Show Result", command=self.stop_and_finish_computation)
                    self.animate_steps(steps, 0)
                else:
                    # Show all steps instantly
                    self.process_text.config(state='normal')
                    for step in steps:
                        self.process_text.insert(END, step + "\n")
                    self.process_text.see(END)
                    self.process_text.config(state='disabled')

        def animate_steps(self, steps, index):
            """Recursively calls itself to print one line at a time."""
            if index < len(steps):
                self.current_step_index = index # Update current index
                
                self.process_text.config(state='normal')
                self.process_text.insert(END, steps[index] + "\n")
                self.process_text.see(END)
                self.process_text.config(state='disabled')
                
                self.step_animation_id = self.after(50, self.animate_steps, steps, index + 1)
            else:
                # Animation finished
                self.finish_computation()

        # --- NEW: Function to stop animation and show result ---
        def stop_and_finish_computation(self):
            """Stops the animation and prints all remaining steps."""
            # Cancel the scheduled 'after' call
            if self.step_animation_id:
                self.after_cancel(self.step_animation_id)
                self.step_animation_id = None
                
            # Print all remaining steps
            self.process_text.config(state='normal')
            # Start from the *next* step, since the current one is already printed
            for i in range(self.current_step_index + 1, len(self.current_steps)):
                self.process_text.insert(END, self.current_steps[i] + "\n")
            
            self.process_text.see(END)
            self.process_text.config(state='disabled')
            
            # Reset the UI
            self.finish_computation()

        # --- NEW: Helper to reset the UI after computation ---
        def finish_computation(self):
            """Resets the compute button and clears animation state."""
            self.compute_button.config(text="Compute", command=self.start_computation)
            
            if self.step_animation_id:
                self.after_cancel(self.step_animation_id)
                self.step_animation_id = None
                
            self.current_steps = []
            self.current_step_index = 0
    App(window)
    back_choices()

def linked_list_window():
    destroy_background()
    clear()
    class SinglyNode:
        def __init__(self, data):
            self.data = data
            self.next = None

    class DoublyNode:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None

    class CircularlyNode:
        def __init__(self, data):
            self.data = data
            self.next = None

    class SinglyLinkedList:
        def __init__(self):
            self.head = None

        def append(self, data):
            new_node = SinglyNode(data)
            if not self.head:
                self.head = new_node
                return
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

        def print_list(self):
            current = self.head
            data_list = []
            while current:
                data_list.append(current.data)
                current = current.next
            return data_list
        
    class DoublyLinkedList:
        def __init__(self):
            self.head = None
            self.tail = None

        def append(self, data):
            new_node = DoublyNode(data)
            if not self.head:
                self.head = new_node
                self.tail = new_node
                return
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        def print_list(self):
            current = self.head
            data_list = []
            while current:
                data_list.append(current.data)
                current = current.next
            return data_list
        
    class CircularlyLinkedList:
        def __init__(self):
            self.head = None

        def append(self, data):
            new_node = CircularlyNode(data)
            if not self.head:
                self.head = new_node
                new_node.next = self.head
                return
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

        def print_list(self):
            current = self.head
            data_list = []
            if self.head is None:
                return data_list
            data_list.append(current.data)
            current = current.next
            while current != self.head:
                data_list.append(current.data)
                current = current.next
            return data_list
        
    class LinkedListUI:
        def __init__(self, window):
            self.window = window
            self.window.title("Linked List UI")
            self.window.geometry("800x600")
            self.linked_list_type = StringVar()
            self. linked_list_type.set("Singly Linked List")
            self.linked_list = SinglyLinkedList()
            self.create_widgets()

        def create_widgets(self):
            self.frame1 = Frame(self.window)
            self.frame1.pack(pady=20)
            self.frame2 = Frame(self.window)
            self.frame2.pack(pady=20)
            self.frame3 = Frame(self.window)
            self.frame3.pack(pady=20)
            self.data_label = Label(self.frame1, text="Data:", font=("Arial", 16))
            self.data_label.pack(side=LEFT, padx=10)
            self.data_entry = Entry(self.frame1, font=("Arial", 16), width=20)
            self.data_entry.pack(side=LEFT, padx=10)
            self.append_button = Button(self.frame2, text="Append", command=self.append_data, font=("Arial", 16))
            self.append_button.pack(side=LEFT, padx=10)
            self.print_button = Button(self.frame2, text="Clear", command=self.clear_data, font=("Arial", 16))
            self.print_button.pack(side=LEFT, padx=10)
            self.linked_list_type_label = Label(self.frame3, text="Linked List Type:", font=("Arial", 16))
            self.linked_list_type_label.pack(side=LEFT, padx=10)
            self.linked_list_type_menu = OptionMenu(self.frame3, self.linked_list_type, "Singly Linked List", "Doubly Linked List", "Circularly Linked List", command=self.change_linked_list_type)
            self.linked_list_type_menu.config(font=("Arial", 16))
            self.linked_list_type_menu.pack(side=LEFT, padx=10)
            self.text_box = Text(self.window, height=15, width=60, font=("Arial", 16))
            self.text_box.pack(pady=20)

        def append_data(self):
            data = self.data_entry.get()
            self.linked_list.append(data)
            self.data_entry.delete(0, END)
            self.print_list()
            messagebox.showinfo("Success", "Data appended successfully")

        def print_list(self):
            self.text_box.delete('1.0', END)
            data_list = self.linked_list.print_list()
            for i, data in enumerate(data_list):
                if isinstance(self.linked_list, CircularlyLinkedList) and i == len(data_list) - 1:
                    self.text_box.insert(END, f"{data}\n↻\n")
                elif i == len(data_list) - 1:
                    self.text_box.insert(END, f"{data}\n↓\nNone\n")
                else:
                    self.text_box.insert(END, f"{data}\n↓\n")

        def clear_data(self):
            if isinstance(self.linked_list, SinglyLinkedList):
                self.linked_list = SinglyLinkedList()
            elif isinstance(self.linked_list, DoublyLinkedList):
                self.linked_list = DoublyLinkedList()
            elif isinstance(self.linked_list, CircularlyLinkedList):
                self.linked_list = CircularlyLinkedList()
            self.text_box.delete('1.0', END)

        def change_linked_list_type(self, value):
            if value == "Singly Linked List":
                self.linked_list = SinglyLinkedList()
            elif value == "Doubly Linked List":
                self.linked_list = DoublyLinkedList()
            elif value == "Circularly Linked List":
                self.linked_list = CircularlyLinkedList()
            self.text_box.delete('1.0', END)

    linked_list_ui = LinkedListUI(window)

    back_choices()

def stack_window():
    destroy_background()
    clear()
    stack = []
    MAX_SIZE = 10  # Maximum number of items allowed in the stack

    # Push an item
    def push_item():
        item = entry.get().strip()
        if item:
            if len(stack) < MAX_SIZE:  # Check for overflow
                stack.append(item)
                entry.delete(0, END)
                update_stack_display()
            else:
                messagebox.showwarning("Overflow", "Stack is full! Cannot push more items.")
        else:
            messagebox.showwarning("Warning", "Please enter an item to push.")

    # Pop the last item
    def pop_item():
        if stack:
            popped = stack.pop()
            update_stack_display()
            messagebox.showinfo("Item Popped", f"Popped item: {popped}")
        else:
            messagebox.showwarning("Underflow", "Stack is empty!")  # Underflow message

    # Update display
    def update_stack_display():
        stack_display.delete(*stack_display.get_children())
        for i, item in enumerate(reversed(stack), 1):
            stack_display.insert("", "end", values=(i, item))

    # Title label
    title = Label(window, text="Stack Program", font=("Segoe UI", 18, "bold"), bg="#f7f9fb", fg="#333")
    title.pack(pady=15)

    # Input field
    entry_frame = Frame(window, bg="#f7f9fb")
    entry_frame.pack(pady=10)
    entry = ttk.Entry(entry_frame, width=28, font=("Segoe UI", 11))
    entry.grid(row=0, column=0, padx=5)

    # Button styling
    style = ttk.Style()
    style.configure("TButton",
                    font=("Segoe UI", 10, "bold"),
                    padding=6,
                    relief="flat")
    style.map("TButton",
            background=[("active", "#e1ecf4")],
            foreground=[("active", "#000")])

    # Buttons
    button_frame = Frame(window, bg="#f7f9fb")
    button_frame.pack(pady=5)
    ttk.Button(button_frame, text="Push", command=push_item).grid(row=0, column=0, padx=5)
    ttk.Button(button_frame, text="Pop", command=pop_item).grid(row=0, column=1, padx=5)

    # Table for stack display
    columns = ("#", "Item")
    stack_display = ttk.Treeview(window, columns=columns, show="headings", height=10)
    stack_display.heading("#", text="Position")
    stack_display.heading("Item", text="Item")
    stack_display.column("#", width=80, anchor="center")
    stack_display.column("Item", width=200, anchor="center")
    stack_display.pack(pady=15)

    # Footer
    footer = Label(window, text="Top item is shown first (Max size: 6)", font=("Segoe UI", 9), bg="#f7f9fb", fg="#777")
    footer.place(x = 665, y = 430)

    # Initialize stack display
    update_stack_display()
    back_choices()

# Handles what happen after clicking the back button
def back_pressed():
    create_background()
    clear_screen()
    main()

# Handles what happen after clicking the start button
def start_pressed():
    create_background()
    clear_screen()
    after_start_action()

# Create the background image and also keep it reference in the window
def create_background():
    window.bg_img = PhotoImage(file='Cityscape.png')
    window.bg_label = Label(window, image=window.bg_img)
    window.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Delete the background image if the label is present and reference
def destroy_background():
    try:
        if hasattr(window, 'bg_label') and window.bg_label:
            window.bg_label.destroy()
    except Exception:
        pass
    window.bg_img = None
# Helps delete all the widget except the background image
def clear_screen():
    for widget in window.winfo_children():
        if hasattr(window, 'bg_label') and widget is getattr(window, 'bg_label'):
            continue
        try:
            widget.destroy()
        except Exception:
            pass

# Clears all the widget including the background image
def clear():
    for widget in window.winfo_children():
        try:
            widget.destroy()
        except Exception:
            pass

def back_choices():
    back = Button(window, text='Back', width=15)
    back.config(font=('Fixedsys', 30, 'bold'),
                bg='#A9595C',
                fg='#EEEEEE',
                activebackground='#12245A',
                activeforeground='#EEEEEE',
                command=start_pressed)
    back.place(x=610, y=700)

def back_main():
    back = Button(window, text='Back', width=15)
    back.config(font=('Fixedsys', 30, 'bold'),
                bg='#A9595C',
                fg='#EEEEEE',
                activebackground='#12245A',
                activeforeground='#EEEEEE',
                command=back_pressed)
    back.place(x=610, y=700)

# Runs the program
if __name__ == "__main__":
    main()