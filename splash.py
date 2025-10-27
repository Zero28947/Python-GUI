from tkinter import *
from tkinter import ttk
from tkinter.ttk import Progressbar
from PIL import Image, ImageTk
import os

# --- SPLASH SCREEN SETUP ---
splash_root = Tk()
splash_root.title("Splash Screen")

# Center window
screen_width = splash_root.winfo_screenwidth()
screen_height = splash_root.winfo_screenheight()
app_width = 500
app_height = 400
x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)
splash_root.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
splash_root.overrideredirect(True)
splash_root.config(bg="black")

# --- GIF LOADING ---
gif_frames = []
frame_delay = 0

def ready_gif():
    gif_file = Image.open('gif/giff.gif')
    for r in range(0, gif_file.n_frames):
        gif_file.seek(r)
        gif_frames.append(ImageTk.PhotoImage(gif_file.copy()))
    return gif_file.info["duration"]

frame_delay = ready_gif()
frame_index = 0

def play_gif():
    global frame_index
    gif_lb.config(image=gif_frames[frame_index])  
    frame_index = (frame_index + 1) % len(gif_frames)
    splash_root.after(frame_delay, play_gif)

gif_lb = Label(splash_root, bg="black")
gif_lb.pack(pady=20)

# --- PROGRESS BAR ---
progress_label = Label(splash_root, text="Loading.....", font=("Trebuchet Ms", 15, "bold"), fg="white", bg="black")
progress_label.pack(pady=10)

progress = ttk.Style()
progress.theme_use('clam')
progress.configure("red.Horizontal.TProgessbar", background="#108cff")

progress = Progressbar(splash_root, orient=HORIZONTAL, length=400, mode='determinate', style="red.Horizontal.TProgressbar")
progress.pack(pady=10)

def top():
    splash_root.withdraw()
    os.system("python project.py")
    splash_root.destroy()

i = 0
def load():
    global i
    if i <= 100:
        progress_label.config(text=f"Loading... {i}%")
        progress['value'] = i
        i += 10
        splash_root.after(500, load)
    else:
        top()

play_gif()
load()
splash_root.mainloop()
