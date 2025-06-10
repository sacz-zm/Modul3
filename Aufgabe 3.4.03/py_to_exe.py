

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Meine Exe")
window.geometry("450x450")

image = Image.open("echse.jpg").resize((400, 400))
photo = ImageTk.PhotoImage(image)

label1 = ttk.Label(window, image=photo)
label1.pack()

window.mainloop()
