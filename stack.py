from tkinter import *
from tkinter import messagebox, ttk
import os

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

# Peek top item
def peek_item():
    if stack:
        top_item = stack[-1]
        messagebox.showinfo("Top Item", f"The top item is: {top_item}")
    else:
        messagebox.showwarning("Empty Stack", "Stack is empty! Nothing to peek.")

# Remove all items
def remove_all_items():
    if stack:
        confirm = messagebox.askyesno("Confirm", "Are you sure you want to remove all items?")
        if confirm:
            stack.clear()
            update_stack_display()
            messagebox.showinfo("Cleared", "All items have been removed from the stack.")
    else:
        messagebox.showwarning("Empty Stack", "Stack is already empty!")

# Update display
def update_stack_display():
    stack_display.delete(*stack_display.get_children())
    for i, item in enumerate(reversed(stack), 1):
        stack_display.insert("", "end", values=(i, item))

# Create main window
window = Tk()
window.state("zoomed")
window.title("Stack Program")
logo = PhotoImage(file='image/hacker06.png')
window.iconphoto(True, logo)
window.configure(bg='#12245A')

# Title label
title = Label(window, text="Stack Program", font=("Segoe UI", 18, "bold"), bg="#12245A", fg='#EEEEEE')
title.pack(pady=15)

# Input field
entry_frame = Frame(window, bg="#12245A")
entry_frame.pack(pady=10)
entry = Entry(entry_frame, width=28, font=("Segoe UI", 11))
entry.grid(row=0, column=0, padx=5)

# Button style
style = ttk.Style()
style.configure("TButton",
                font=("Segoe UI", 10, "bold"),
                padding=6,
                relief="flat")
style.map("TButton",
          background=[("active", "#12245A")],
          foreground=[("active", "#EEEEEE")])

# Buttons
button_frame = Frame(window, bg="#12245A")
button_frame.pack(pady=5)
Button(button_frame, text="Push", bg="#60709C", fg="#EEEEEE", command=push_item).grid(row=0, column=0, padx=5)
Button(button_frame, text="Pop", bg="#60709C", fg="#EEEEEE", command=pop_item).grid(row=0, column=1, padx=5)
Button(button_frame, text="Peek", bg="#60709C", fg="#EEEEEE", command=peek_item).grid(row=0, column=2, padx=5)
Button(button_frame, text="Remove All", bg="#60709C", fg="#EEEEEE", command=remove_all_items).grid(row=0, column=3, padx=5)

# Table for stack display
columns = ("#", "Item")
stack_display = ttk.Treeview(window, columns=columns, show="headings", height=10)
stack_display.heading("#", text="Position")
stack_display.heading("Item", text="Item")
stack_display.column("#", width=80, anchor="center")
stack_display.column("Item", width=200, anchor="center")
stack_display.pack(pady=15)

# Footer
footer = Label(window, text="Top item is shown first (Max size: 10)", font=("Segoe UI", 9), bg="#12245A", fg="#EEEEEE")
footer.pack(side="bottom", pady=30)

def back():
    window.withdraw()
    os.system("python project.py")
    window.destroy()

back_button = Button(window, text='Back', width=15)
back_button.config(font=('Fixedsys', 30, 'bold'),
            bg='#A9595C',
            fg='#EEEEEE',
            activebackground='#12245A',
            activeforeground='#EEEEEE',
            command=back)
back_button.pack(side="bottom", pady=10)

# Stack display
update_stack_display()
window.mainloop()
