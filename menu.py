from tkinter import * 
from tkinter import font
import winsound
import os

window = Tk()
# Fonts Use
button_font = font.Font(family="Fixedsys", size=30, weight='bold')
title_font = font.Font(family="Fixedsys", size=150, weight='bold')
winsound.MessageBeep(winsound.MB_ICONASTERISK)
window.attributes("-alpha", 0.0)

def main():
    window.state("zoomed")
    icon = PhotoImage(file='image/hacker06.png')
    window.iconphoto(True, icon)
    window.title("CC 2103 Project")
    window.config(bg='#F0EAD2')
    if window.attributes("-alpha") == 0.0:
        fade_in()

    title_label = Label(window, text="Learnify", font=title_font, fg='#6C584C', bg='#F0EAD2')
    title_label.pack(pady=60)

    button_frame = Frame(window, bg='#F0EAD2')
    button_frame.pack(expand=True)

    start_btn = Button(window, text='Start', width=15)
    start_btn.config(font=button_font,
                    bg='#ADC178',
                    fg='#4A3F35',
                    activebackground='#DDE5B6',
                    activeforeground='#4A3F35',
                    command=start_pressed)
    start_btn.pack(pady=20)
    start_btn.bind("<Enter>", on_enter) 
    start_btn.bind("<Leave>", on_leave)

    member_btn = Button(window, text='Member', width=15)
    member_btn.config(font=button_font,
                    bg='#ADC178',
                    fg='#4A3F35',
                    activebackground='#DDE5B6',
                    activeforeground='#4A3F35',
                    command=author)
    member_btn.pack(pady=20)
    member_btn.bind("<Enter>", on_enter) 
    member_btn.bind("<Leave>", on_leave)


    exit_btn = Button(window, text='Exit', width=15)
    exit_btn.config(font=button_font,
                    bg='#ADC178',
                    fg='#4A3F35',
                    activebackground='#DDE5B6',
                    activeforeground='#ADC178',
                    command=window.destroy)
    exit_btn.pack(pady=20)
    exit_btn.bind("<Enter>", on_enter) 
    exit_btn.bind("<Leave>", on_leave)
    window.mainloop()

# Example follow-up function to run after clearing the screen
def after_start_action():
    # Choices
    title = Label(window, text="Choose One", font=title_font, fg='#6C584C', bg='#F0EAD2')
    title.pack(pady=60)

    button_frame = Frame(window, bg='#F0EAD2')
    button_frame.pack(expand=True)

    # Linked List Button
    recursion_btn = Button(window, text='Recursion', width=15)
    recursion_btn.config(font=button_font,
                         bg='#ADC178',
                         fg='#4A3F35',
                         activebackground='#DDE5B6',
                         activeforeground='#ADC178')
    recursion_btn.pack(pady=20)
    recursion_btn.config(command=recursion_window)
    recursion_btn.bind("<Enter>", on_enter) 
    recursion_btn.bind("<Leave>", on_leave)

    # Linked List Button
    linked_list_btn = Button(window, text='Linked List', width=15)
    linked_list_btn.config(font=button_font,
                         bg='#ADC178',
                         fg='#4A3F35',
                         activebackground='#DDE5B6',
                         activeforeground='#ADC178')
    linked_list_btn.pack(pady=20)
    linked_list_btn.config(command=linked_list_window)
    linked_list_btn.bind("<Enter>", on_enter) 
    linked_list_btn.bind("<Leave>", on_leave)

    # Stack Button
    stack_btn = Button(window, text='Stack', width=15)
    stack_btn.config(font=button_font,
                         bg='#ADC178',
                         fg='#4A3F35',
                         activebackground='#DDE5B6',
                         activeforeground='#ADC178')
    stack_btn.pack(pady=20)
    stack_btn.config(command=stack_window)
    stack_btn.bind("<Enter>", on_enter) 
    stack_btn.bind("<Leave>", on_leave)
    back_main()
    
def recursion_window():
    window.withdraw()
    os.system("python module/recursion.py")
    window.destroy()

def linked_list_window():
    window.withdraw()
    os.system("python module/linked_list.py")
    window.destroy()

def stack_window():
    window.withdraw()
    os.system("python module/stack.py")
    window.destroy()

# Handles what happen after clicking the back start_btn
def back_pressed():
    clear()
    main()

# Handles what happen after clicking the start start_btn
def start_pressed():
    clear()
    after_start_action()

def author():
    clear()   
    leader = Label(window, 
                   text="LEADER", 
                   font=button_font, 
                   bg='#F0EAD2',
                   fg='#4A3F35',)
    leader.pack(pady=(20, 5))

    leader = Label(window, 
                   text="Erlander Guiang", 
                   font=button_font, 
                   bg='#F0EAD2',
                   fg='#4A3F35',)
    leader.pack(pady=(0, 20))

    leader = Label(window, 
                   text="MEMBERS", 
                   font=button_font, 
                   bg='#F0EAD2',
                   fg='#4A3F35',)
    leader.pack(pady=(10, 5))

    member1 = Label(window, 
                    text="LINKED LIST", 
                    font=button_font, 
                    bg='#F0EAD2',
                    fg='#4A3F35',)
    member1.pack(pady=(0, 5))

    member1 = Label(window, 
                    text="Melvin Molenilla", 
                    font=button_font, 
                    bg='#F0EAD2',
                    fg='#4A3F35',)
    member1.pack(pady=(0, 15))

    member2 = Label(window, 
                    text="Recursion", 
                    font=button_font, 
                    bg='#F0EAD2',
                    fg='#4A3F35',)
    member2.pack(pady=(0, 5))

    member2 = Label(window, 
                    text="Frinz Jordan", 
                    font=button_font, 
                    bg='#F0EAD2',
                    fg='#4A3F35',)
    member2.pack(pady=(0, 15))

    member3 = Label(window, 
                    text="Stack", 
                    font=button_font,
                    bg='#F0EAD2',
                    fg='#4A3F35',)
    member3.pack(pady=(0, 5))

    member3 = Label(window, 
                    text="Clarence Pajo", 
                    font=button_font,
                    bg='#F0EAD2',
                    fg='#4A3F35',)
    member3.pack(pady=(0, 15))
    back_main()

# Clears all the widget including the background image
def clear():
    for widget in window.winfo_children():
        try:
            widget.destroy()
        except Exception:
            pass

def back_main():
    back = Button(window, text='Back', width=15)
    back.config(font=button_font,
                bg='#ADC178',
                fg='#4A3F35',
                activebackground='#DDE5B6',
                activeforeground='#ADC178',
                command=back_pressed)
    back.pack(pady=(20, 10), side="bottom")
    back.bind("<Enter>", on_enter) 
    back.bind("<Leave>", on_leave)

def on_enter(event):
    event.widget.config(bg='#7B6C5D', relief=SUNKEN)

def on_leave(event):
    event.widget.config(bg='#ADC178', relief=RAISED)

def fade_in(alpha = 0):
    if alpha < 1.0:
        window.attributes("-alpha", alpha)
        window.after(50, fade_in, alpha + 0.05)


if __name__ == "__main__":
    main()