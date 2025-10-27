from tkinter import *

# ------------------------
# Stack Class
# ------------------------
class Stack:
    def __init__(self, canvas):
        self.canvas = canvas
        self.items = []  # Store stack elements

    def push(self, value):
        self.items.append(value)
        self.draw()

    def pop(self):
        if self.items:
            self.items.pop()
            self.draw()

    def draw(self):
        self.canvas.delete("all")  # Clear canvas
        x, y = 150, 250             # Starting position (bottom)
        width, height = 100, 40     # Shape size
        spacing = 10                # Gap between rectangles

        for value in reversed(self.items):  # Draw from bottom to top
            # Draw rectangle for stack item
            rect = self.canvas.create_rectangle(x, y - height, x + width, y, fill="lightgreen", outline="black")
            self.canvas.create_text(x + width/2, y - height/2, text=str(value), font=("Arial", 14, "bold"))
            y -= (height + spacing)

# ------------------------
# Tkinter GUI
# ------------------------
def main():
    root = Tk()
    root.title("Stack Visualizer")
    root.geometry("400x400")

    canvas = Canvas(root, bg="white", width=400, height=300)
    canvas.pack(pady=10)

    stack = Stack(canvas)

    # Input + Buttons
    frame = Frame(root)
    frame.pack()

    entry = Entry(frame, width=10, font=("Arial", 14))
    entry.grid(row=0, column=0, padx=5)

    def push_value():
        val = entry.get()
        if val.isdigit():
            stack.push(int(val))
            entry.delete(0, END)
        else:
            print("Please enter a number")

    def pop_value():
        stack.pop()

    Button(frame, text="Push", command=push_value, font=("Arial", 12)).grid(row=0, column=1, padx=5)
    Button(frame, text="Pop", command=pop_value, font=("Arial", 12)).grid(row=0, column=2, padx=5)

    root.mainloop()

if __name__ == "__main__":
    main()