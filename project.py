from tkinter import * 
from PIL import ImageTk, Image
import os

window = Tk()
def main():
    window.state("zoomed")
    icon = PhotoImage(file='image/hacker06.png')
    window.iconphoto(True, icon)
    create_background()
    window.title("CC 2103 Project")
    window.config(bg='#12245A')

    title = Label(window, text="Learnify", font=('Fixedsys', 70, 'bold'), fg='#EEEEEE', bg='#12245A')
    title.place(x=570, y=100)

    start_btn = Button(window, text='Start', width=15)
    start_btn.config(font=('Fixedsys', 30, 'bold'),
                    bg='#A9595C',
                    fg='#EEEEEE',
                    activebackground='#12245A',
                    activeforeground='#EEEEEE',
                    command=start_pressed)
    start_btn.place(x=610, y=400)

    member_btn = Button(window, text='Creator', width=15)
    member_btn.config(font=('Fixedsys', 30, 'bold'),
                    bg='#60709C',
                    fg='#EEEEEE',
                    activebackground='#12245A',
                    activeforeground='#EEEEEE',
                    command=author)
    member_btn.place(x=610, y=500)


    exit_btn = Button(window, text='Exit', width=15)
    exit_btn.config(font=('Fixedsys', 30, 'bold'),
                    bg='#60709C',
                    fg='#EEEEEE',
                    activebackground='#12245A',
                    activeforeground='#EEEEEE',
                    command=window.destroy)
    exit_btn.place(x=610, y=600)
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
    window.withdraw()
    os.system("python recursion.py")
    window.destroy()

def linked_list_window():
    window.withdraw()
    os.system("python linked_list.py")
    window.destroy()

def stack_window():
    window.withdraw()
    os.system("python stack.py")
    window.destroy()

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

def author():
    clear_screen()   
    leader = Label(window, text="Leader: Erlander Guiang", font=('Fixedsys', 40, 'bold'), fg='#EEEEEE', bg='#12245A')
    leader.place(x=200, y=100)

    member1 = Label(window, text="Linked List: Melvin Molenilla", font=('Fixedsys', 30, 'bold'), fg='#EEEEEE', bg='#12245A')
    member1.place(x=200, y=250)

    member2 = Label(window, text="Recursion: Frinz Jordan", font=('Fixedsys', 30, 'bold'), fg='#EEEEEE', bg='#12245A')
    member2.place(x=200, y=400)

    member3 = Label(window, text="Stack: Clarence Pajo", font=('Fixedsys', 30, 'bold'), fg='#EEEEEE', bg='#12245A')
    member3.place(x=200, y=550)
    back_main()

# Create the background image and also keep it reference in the window
def create_background():
    window.bg_img = PhotoImage(file='image/Cityscape.png')
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

if __name__ == "__main__":
    main()
