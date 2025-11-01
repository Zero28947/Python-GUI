from tkinter import *
from tkinter import ttk
from tkinter.ttk import Progressbar
from tkinter import font
from PIL import Image, ImageTk
import winsound
import os

# --- SPLASH SCREEN SETUP ---
splash_root = Tk()
splash_root.title("Splash Screen")

# Centers the splash
screen_width = splash_root.winfo_screenwidth()
screen_height = splash_root.winfo_screenheight()
app_width = 500
app_height = 400
x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)
splash_root.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
splash_root.overrideredirect(True)
splash_root.config(bg="#F0EAD2")

# --- GIF LOADING ---
gif_frames = []
frame_delay = 0

def ready_gif():
    gif_file = Image.open('gif/relax.gif')
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

# ===== TITLE BAR =====
title_font = font.Font(family="Fixedsys", size=20, weight='bold')
text = "Welcome to Learnify"
title_label = Label(splash_root, text="", font=title_font, fg="#6C584C", bg="#F0EAD2")
title_label.pack(pady=5)

def typing_effect(i=0):
    if i < len(text):
        title_label.config(text=text[:i+1])
        splash_root.after(250, typing_effect, i+1)
    else:
        title_label.config(text=text)


# --- PROGRESS BAR ---
style = ttk.Style()
style.theme_use('clam')
style.configure("Custom.Horizontal.TProgressbar", troughcolor="#F0EAD2", background="#A98467", thickness=8, bordercolor="#F0EAD2", lightcolor="#A98467", darkcolor="#A98467")

progress = Progressbar(splash_root, orient=HORIZONTAL, length=500, mode='determinate', style="Custom.Horizontal.TProgressbar")

custom_font = font.Font(family="Fixedsys", size=15, weight="normal", slant="roman")
progress_label = Label(splash_root, text="Loading.....", font=custom_font, fg="#6C584C", bg="#F0EAD2")

progress_label.pack(side='bottom', fill='x', pady=5)
progress.pack(side='bottom', fill='x')

def top():
    splash_root.withdraw()
    os.system("python menu.py")
    splash_root.destroy()

i = 0
def load():
    global i
    if i <= 100:
        progress_label.config(text=f"Loading... {i}%")
        progress['value'] = i
        i += 2
        splash_root.after(100, load)
    else:
        progress_label.config(text="Launching.....")
        splash_root.after(700, top)

winsound.PlaySound("sound/typing.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
play_gif()
typing_effect()
load()
splash_root.mainloop()
