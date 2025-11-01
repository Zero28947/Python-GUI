import tkinter as tk
from tkinter import messagebox

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
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
        new_node = Node(data)
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
        new_node = Node(data)
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
    
def create_widgets(root):
    linked_list = [SinglyLinkedList()]
    linked_list_type = tk.StringVar()
    linked_list_type.set("Singly Linked List")
    frame1 = tk.Frame(root, bg="black")
    frame1.pack(anchor=tk.W, padx=20, pady=20)
    frame2 = tk.Frame(root, bg="black")
    frame2.pack(anchor=tk.W, padx=20, pady=20)
    frame3 = tk.Frame(root, bg="black")
    frame3.pack(anchor=tk.W, padx=20, pady=20)
    data_label = tk.Label(frame1, text="Data:", bg="black", fg="white")
    data_label.pack(side=tk.LEFT, padx=10)
    data_entry = tk.Entry(frame1, bg="white", fg="black")
    data_entry.pack(side=tk.LEFT, padx=10)
    canvas = tk.Canvas(root, width=800, height=200, bg="black")
    canvas.pack()
    pacman_x = 50
    pacman_y = 100

    def draw_pacman():
        canvas.delete("pacman")
        canvas.create_oval(pacman_x, pacman_y, pacman_x+20, pacman_y+20, fill="yellow", tag="pacman")
        canvas.create_polygon(pacman_x+10, pacman_y+10, pacman_x+15, pacman_y+5, pacman_x+15, pacman_y+15, fill="black", tag="pacman")

    def animate_pacman(data):
        nonlocal pacman_x
        draw_pacman()
        for i in range(10):
            pacman_x += 5
            canvas.move("pacman", 5, 0)
            canvas.update_idletasks()
            canvas.after(50)
        linked_list[0].append(data)
        print_list()
        for i in range(10):
            pacman_x -= 5
            canvas.move("pacman", -5, 0)
            canvas.update_idletasks()
            canvas.after(50)

    def append_data():
        data = data_entry.get()
        animate_pacman(data)
        data_entry.delete(0, tk.END)

    def print_list():
        canvas.delete("all")
        data_list = linked_list[0].print_list()
        x = 50
        y = 50
        for i, data in enumerate(data_list):
            # Draw data box
            canvas.create_rectangle(x, y, x+50, y+30, fill="white")
            canvas.create_text(x+25, y+15, text=str(data))
            
            # Draw arrows
            if isinstance(linked_list[0], SinglyLinkedList):
                if i < len(data_list) - 1:
                    canvas.create_line(x+50, y+15, x+70, y+15, arrow=tk.LAST)
            elif isinstance(linked_list[0], DoublyLinkedList):
                if i < len(data_list) - 1:
                    canvas.create_line(x+50, y+15, x+70, y+15, arrow=tk.LAST)
                if i > 0:
                    canvas.create_line(x, y+15, x-20, y+15, arrow=tk.LAST)
            elif isinstance(linked_list[0], CircularlyLinkedList):
                if i < len(data_list) - 1:
                    canvas.create_line(x+50, y+15, x+70, y+15, arrow=tk.LAST)
                if i == len(data_list) - 1:
                    canvas.create_line(x+50, y+15, x-20, y+15, arrow=tk.LAST)
            
            x += 70
    def change_linked_list_type(value):
        if value == "Singly Linked List":
            linked_list[0] = SinglyLinkedList()
        elif value == "Doubly Linked List":
            linked_list[0] = DoublyLinkedList()
        elif value == "Circularly Linked List":
            linked_list[0] = CircularlyLinkedList()
        canvas.delete("all")
    append_button = tk.Button(frame2, text="Append", command=append_data, fg="black", bg="red")
    append_button.pack(side=tk.LEFT, padx=10)
    print_button = tk.Button(frame2, text="Print", command=print_list, fg="black", bg="Blue")
    print_button.pack(side=tk.LEFT, padx=10)
    linked_list_type_label = tk.Label(frame3, text="Linked List Type:", bg="black", fg="yellow")
    linked_list_type_label.pack(side=tk.LEFT, padx=10)
    linked_list_type_menu = tk.OptionMenu(frame3, linked_list_type, "Singly Linked List", "Doubly Linked List", "Circularly Linked List", command=change_linked_list_type)
    linked_list_type_menu.config(bg="green", fg="black")
    linked_list_type_menu.pack(side=tk.LEFT, padx=10)
root = tk.Tk()
root.title("Linked List App")
root.configure(bg="black")
root.state("zoomed")
create_widgets(root)
root.mainloop()