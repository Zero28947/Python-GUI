from tkinter import *
import os

# Variables
stack_data = []
MAX_SIZE = 15
ITEM_HEIGHT = 40
ITEM_WIDTH = 400
STACK_X = 370
stack_blocks = []

retro_colors = ["#00bcd4", "#ff4081", "#8bc34a", "#ffeb3b", "#ff5722", "#9c27b0"]
color_counter = 0  # color tracker


# Retro Popup
def show_message(title, message, color="#111", confirm=False, on_confirm=None, highlight=None):
    message_box = Toplevel(main_window)
    message_box.title(title)
    message_box.geometry("320x170")
    message_box.configure(bg=color)
    message_box.resizable(False, False)
    message_box.attributes('-topmost', True)

    Frame(message_box, bg="#00ff99", height=5).pack(fill=X)
    Label(message_box, text=title, font=("Consolas", 11, "bold"), fg="#00ff99", bg=color).pack(pady=(15, 5))

    msg_frame = Frame(message_box, bg=color)
    msg_frame.pack(pady=5)
    Label(msg_frame, text=message, font=("Consolas", 10), fg="#ffffff", bg=color).pack()

    if highlight:
        Label(msg_frame, text=f"> {highlight} <", font=("Consolas", 11, "bold"), fg="#00ffff", bg=color).pack(pady=(5, 0))

    btn_frame = Frame(message_box, bg=color)
    btn_frame.pack(pady=10)

    if confirm:
        def yes_action():
            message_box.destroy()
            if on_confirm:
                on_confirm()

        Button(btn_frame, text="YES", command=yes_action, font=("Consolas", 10, "bold"),
               bg="#00ff99", fg="#000", activebackground="#00cc88", relief="flat", width=8).pack(side=LEFT, padx=5)
        Button(btn_frame, text="NO", command=message_box.destroy, font=("Consolas", 10, "bold"),
               bg="#ff2e63", fg="#fff", activebackground="#ff507f", relief="flat", width=8).pack(side=LEFT, padx=5)
    else:
        Button(message_box, text="OK", command=message_box.destroy, font=("Consolas", 10, "bold"),
               bg="#00ff99", fg="#000", activebackground="#00cc88", relief="flat", width=8).pack(pady=5)

    Frame(message_box, bg="#00ff99", height=5).pack(fill=X)
    message_box.grab_set()


# Stack Operations
def push_item():
    global color_counter
    item = entry_box.get().strip()
    if item:
        if len(stack_data) < MAX_SIZE:
            stack_data.append(item)
            entry_box.delete(0, END)
            color_counter = (color_counter + 1) % len(retro_colors)
            animate_push(len(stack_data) - 1, retro_colors[color_counter])
        else:
            show_message("OVERFLOW", "Stack is full!")
    else:
        show_message("WARNING", "Enter an item!")


def pop_item():
    if stack_data:
        popped = stack_data.pop()
        animate_pop()
        show_message("ITEM POPPED", "Removed item:", highlight=popped)
    else:
        show_message("UNDERFLOW", "Stack is empty!")


def peek_item():
    if stack_data:
        top_item = stack_data[-1]
        show_message("TOP ITEM", "Currently at top:", highlight=top_item)
    else:
        show_message("EMPTY", "Stack is empty!")


def remove_all_items():
    if stack_data:
        show_message("CONFIRM", "Are you sure you want to delete all?",
                    confirm=True, on_confirm=confirm_remove_all)
    else:
        show_message("EMPTY", "Nothing to clear!")


def confirm_remove_all():
    if stack_data:
        stack_data.clear()
        animate_remove_all()
        show_message("CLEARED", "All items removed!")


# Animation
def animate_push(index, color):
    y = stack_canvas.winfo_height() - ITEM_HEIGHT * (index + 1) - 10
    rect = stack_canvas.create_rectangle(STACK_X - ITEM_WIDTH // 2, 0,
                                         STACK_X + ITEM_WIDTH // 2, ITEM_HEIGHT,
                                         fill=color, outline="#222", width=2)
    text = stack_canvas.create_text(STACK_X, ITEM_HEIGHT // 2,
                                    text=stack_data[index], fill="white",
                                    font=("Consolas", 11, "bold"))

    def move_step(current_y):
        if current_y < y:
            stack_canvas.move(rect, 0, 5)
            stack_canvas.move(text, 0, 5)
            stack_canvas.after(10, lambda: move_step(current_y + 5))
        else:
            stack_blocks.append((rect, text))

    move_step(0)


def animate_pop():
    if stack_blocks:
        rect, text = stack_blocks.pop()

        def flash(count=0):
            if count < 6:
                color = "#f1c40f" if count % 2 == 0 else "#9b59b6"
                stack_canvas.itemconfig(rect, fill=color)
                stack_canvas.after(80, lambda: flash(count + 1))
            else:
                stack_canvas.delete(rect)
                stack_canvas.delete(text)

        flash()

def back():
    main_window.withdraw()
    os.system("python options.py")
    main_window.destroy()

def animate_remove_all():
    if stack_blocks:
        rect, text = stack_blocks.pop()

        def move_step(current_y):
            if current_y > -ITEM_HEIGHT:
                stack_canvas.move(rect, 0, -5)
                stack_canvas.move(text, 0, -5)
                stack_canvas.after(5, lambda: move_step(current_y - 5))
            else:
                stack_canvas.delete(rect)
                stack_canvas.delete(text)
                animate_remove_all()

        move_step(stack_canvas.coords(rect)[1])


# Hover effect
def on_enter(e, hover_color):
    e.widget['bg'] = hover_color


def on_leave(e, base_color):
    e.widget['bg'] = base_color


# Window Setup
main_window = Tk()
main_window.title("Stack Program")
main_window.configure(bg="#0d0d0d")
main_window.state("zoomed")
main_window.resizable(False, False)

# Title
title_label = Label(main_window, text="STACK PROGRAM",
                    font=("Segoe UI", 18, "bold"),
                    fg="#00FFFF", bg="#0d0d0d")
title_label.pack(pady=10)

# Entry Box
entry_box = Entry(main_window, font=("Consolas", 12, "bold"),
                  bg="#1a1a1a", fg="#00ff99",
                  insertbackground="#00ff99",
                  relief=FLAT, justify=CENTER)
entry_box.pack(pady=10, padx=20, fill=X)

# Buttons
btn_frame = Frame(main_window, bg="#0d0d0d")
btn_frame.pack(pady=10, padx=20, fill=X)

btn_base = "#00adb5"
btn_hover = "#00ffcc"

btn_push_item = Button(btn_frame, text="Push", command=push_item,
                       bg=btn_base, fg="black", relief=FLAT,
                       font=("Consolas", 10, "bold"))
btn_pop_item = Button(btn_frame, text="Pop", command=pop_item,
                      bg="#ff2e63", fg="white", relief=FLAT,
                      font=("Consolas", 10, "bold"))
btn_peek_item = Button(btn_frame, text="Peek", command=peek_item,
                       bg=btn_base, fg="black", relief=FLAT,
                       font=("Consolas", 10, "bold"))
btn_remove_all = Button(btn_frame, text="Remove All", command=remove_all_items,
                        bg="#393e46", fg="white", relief=FLAT,
                        font=("Consolas", 10, "bold"))
btn_back = Button(btn_frame, text="Back", command=back,
                        bg="#393e46", fg="white", relief=FLAT,
                        font=("Consolas", 10, "bold"))

for btn in [btn_push_item, btn_pop_item, btn_peek_item, btn_remove_all, btn_back]:
    btn.pack(side=LEFT, expand=True, fill=X, padx=5)
    btn.bind("<Enter>", lambda e, hc=btn_hover: on_enter(e, hc))
    btn.bind("<Leave>", lambda e, bc=btn['bg']: on_leave(e, bc))

# --- Canvas ---
stack_canvas = Canvas(main_window, bg="#0d0d0d")
stack_canvas.pack(side='right', fill=BOTH, expand=True, padx=20, pady=10)


def draw_grid():
    for x in range(0, 1000, 40):
        stack_canvas.create_line(x, 0, x, 1000, fill="#262626", width=1)
    for y in range(0, 1000, 40):
        stack_canvas.create_line(0, y, 1000, y, fill="#262626", width=1)

# --- Message Box Container ---
message_box_frame = Frame(main_window, bg="#0d0d0d")
message_box_frame.pack(pady=10, padx=20, fill=X)

message_box = Text(message_box_frame, height=20, width=60, wrap="word",
                   bg="#1a1a1a", fg="#00ff99", font=("Consolas", 10, "bold"))
message_box.pack(fill=X)

def show_message(title, message, highlight=None, confirm=False, on_confirm=None):
    """Display messages inside the message box with optional confirmation buttons."""
    # Enable editing the Text widget
    message_box.configure(state='normal')
    message_box.delete(1.0, END)  # clear old message
    message_box.insert(END, f"[{title}]\n{message}\n")
    if highlight:
        message_box.insert(END, f"> {highlight} <\n")
    message_box.configure(state='disabled')

    if confirm:
        # Create a small frame just below the message box for buttons
        confirm_frame = Frame(message_box_frame, bg="#0d0d0d")
        confirm_frame.pack(pady=5)

        def yes_action():
            confirm_frame.destroy()
            if on_confirm:
                on_confirm()

        def no_action():
            confirm_frame.destroy()

        Button(confirm_frame, text="YES", command=yes_action,
               font=("Consolas", 10, "bold"), bg="#00ff99", fg="#000",
               activebackground="#00cc88", relief="flat", width=8).pack(side=LEFT, padx=5)
        Button(confirm_frame, text="NO", command=no_action,
               font=("Consolas", 10, "bold"), bg="#ff2e63", fg="#fff",
               activebackground="#ff507f", relief="flat", width=8).pack(side=LEFT, padx=5)
        
draw_grid()

main_window.mainloop()
