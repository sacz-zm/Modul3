import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageSequence

root = tk.Tk()
root.geometry("400x300")

gif = tk.Toplevel()
gif.geometry("400x300")

label = tk.Label(gif)
label.pack()

# Gif

img = Image.open("giphy.gif")

label = tk.Label()
label.pack()

frames = [ImageTk.PhotoImage(frame.copy().convert("RGBA")) for frame in ImageSequence.Iterator(img)]

def update(ind):
    frame = frames[ind]
    label.config(image=frame)
    ind = (ind + 1) % len(frames)
    gif.after(100, update, ind)
update(0)

root.mainloop()