from tkinter import *

# ------------------------
# Linked List Node
# ------------------------
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# ------------------------
# Linked List Structure
# ------------------------
class LinkedList:
    def __init__(self, canvas):
        self.head = None
        self.canvas = canvas
        self.nodes = []  # store node positions for drawing

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

        self.nodes.append(new_node)
        self.draw()

    def draw(self):
        self.canvas.delete("all")  # clear previous drawings
        x, y = 50, 100
        node_width = 60
        spacing = 100

        for i, node in enumerate(self.nodes):
            # Draw rectangle node
            rect = self.canvas.create_rectangle(x, y, x + node_width, y + 40, fill="lightblue")
            # Draw the number
            self.canvas.create_text(x + node_width/2, y + 20, text=str(node.data), font=("Arial", 14, "bold"))

            # Draw arrow to next node
            if i < len(self.nodes) - 1:
                self.canvas.create_line(x + node_width, y + 20, x + spacing, y + 20, arrow=LAST, width=2)

            x += spacing

# ------------------------
# Tkinter App
# ------------------------
def main():
    root = Tk()
    root.title("Linked List Visualizer")
    root.geometry("800x300")

    canvas = Canvas(root, bg="white", width=800, height=200)
    canvas.pack(pady=20)

    ll = LinkedList(canvas)

    # Input and button
    frame = Frame(root)
    frame.pack()

    entry = Entry(frame, width=10, font=("Arial", 14))
    entry.grid(row=0, column=0, padx=5)

    def add_node():
        value = entry.get()
        if value.isdigit():
            ll.insert(int(value))
            entry.delete(0, END)
        else:
            print("Please enter a number")

    btn = Button(frame, text="Insert", command=add_node, font=("Arial", 12))
    btn.grid(row=0, column=1)

    root.mainloop()

if __name__ == "__main__":
    main()