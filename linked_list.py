from tkinter import *
from tkinter import ttk
import os

root = Tk()
root.title("Linked List App")
root.configure(bg="#12245A")
root.state("zoomed")
logo = PhotoImage(file='image/hacker06.png')
root.iconphoto(True, logo)

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
    linked_list_type = StringVar()
    linked_list_type.set("Singly Linked List")

    frame1 = Frame(root, bg="#12245A")
    frame1.pack(pady=20)

    frame2 = Frame(root, bg="#12245A")
    frame2.pack(pady=20)

    frame3 = Frame(root, bg="#12245A")
    frame3.pack(pady=20)

    data_label = Label(frame1, text="Data:", bg="#60709C", fg="#EEEEEE")
    data_label.pack(side=LEFT, padx=10)

    data_entry = Entry(frame1, bg="#60709C", fg="#EEEEEE")
    data_entry.pack(side=LEFT, padx=10)

    list_text = Text(root, height=10, width=40, fg="black")
    list_text.pack(pady=20)

    def append_data():
        data = data_entry.get()
        linked_list[0].append(data)
        data_entry.delete(0, END)

    def print_list():
        list_text.delete('1.0', END)
        data_list = linked_list[0].print_list()
        if isinstance(linked_list[0], SinglyLinkedList):
            for i, data in enumerate(data_list):
                if i == len(data_list) - 1:
                    list_text.insert(END, str(data) + "\n")
                else:
                    list_text.insert(END, str(data) + " -> ")
        elif isinstance(linked_list[0], DoublyLinkedList):
            list_text.insert(END, "None <-> ")
            for i, data in enumerate(data_list):
                list_text.insert(END, str(data))
                if i == len(data_list) - 1:
                    list_text.insert(END, "\n")
                else:
                    list_text.insert(END, " <-> ")
        elif isinstance(linked_list[0], CircularlyLinkedList):
            for i, data in enumerate(data_list):
                list_text.insert(END, str(data))
                if i == len(data_list) - 1:
                    list_text.insert(END, " ↻ " + str(data_list[0]) + "\n")
                else:
                    list_text.insert(END, " -> ")

    def change_linked_list_type(value):
        if value == "Singly Linked List":
            linked_list[0] = SinglyLinkedList()
        elif value == "Doubly Linked List":
            linked_list[0] = DoublyLinkedList()
        elif value == "Circularly Linked List":
            linked_list[0] = CircularlyLinkedList()
        list_text.delete('1.0', END)

    append_button = Button(frame2, text="Append", command=append_data, bg="#60709C", fg="#EEEEEE")
    append_button.pack(side=LEFT, padx=10)

    print_button = Button(frame2, text="Print", command=print_list, bg="#60709C", fg="#EEEEEE")
    print_button.pack(side=LEFT, padx=10)

    linked_list_type_label = Label(frame3, text="Linked List Type:", bg="#60709C", fg="#EEEEEE")
    linked_list_type_label.pack(side=LEFT, padx=10)

    linked_list_type_menu = OptionMenu(frame3, linked_list_type, "Singly Linked List", "Doubly Linked List", "Circularly Linked List", command=change_linked_list_type)
    linked_list_type_menu.config(bg="#60709C", fg="#EEEEEE")
    linked_list_type_menu.pack(side=LEFT, padx=10)

def back():
    root.withdraw()
    os.system("python project.py")
    root.destroy()

back_button = Button(root, text='Back', width=15)
back_button.config(font=('Fixedsys', 30, 'bold'),
            bg='#A9595C',
            fg='#EEEEEE',
            activebackground='#12245A',
            activeforeground='#EEEEEE',
            command=back)
back_button.place(x=610, y=700)


create_widgets(root)
root.mainloop()