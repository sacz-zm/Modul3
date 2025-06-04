import os
import pygame
import tkinter as tk
from tkinter import filedialog as fd, messagebox as mb
from tkinter import ttk
from PIL import Image, ImageTk, ImageSequence

def show_gif():
    gif = tk.Toplevel()
    
    label = tk.Label(gif)
    label.grid()

    gif.update()
    width = gif.winfo_width()
    height = gif.winfo_height()
    gif.geometry = (f"{width}x{height}")

    img = Image.open("giphy.gif")

    frames = [ImageTk.PhotoImage(frame.copy().convert("RGBA")) for frame in ImageSequence.Iterator(img)]

    def update(ind):
        frame = frames[ind]
        label.config(image=frame)
        ind = (ind + 1) % len(frames)
        gif.after(100, update, ind)
    update(0)

def play_sound():
    pygame.mixer.music.load("./Sounds/file_example_MP3_700KB.mp3")
    pygame.mixer.music.play()

def quit_app(root):
    pygame.mixer.quit()
    root.quit()

def play_game():
    game_window = tk.Toplevel()
    game_window.title("Game")
    game_window.geometry("600x300")
    tk.Label(game_window)
    tk.Button(game_window, text="Quit", command=game_window.destroy).grid()
