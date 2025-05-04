import os
import tkinter as tk
from tkinter import filedialog
import pygame

# Initialize Pygame Mixer
pygame.mixer.init()

# Example values
temp_dir = "C:/Users/HP/AppData/Local/Temp"  # Replace this with your actual directory
i = 1  # Replace with the desired index
file_path = os.path.join(temp_dir, f'temp_audio2.mp3')

# GUI
root = tk.Tk()
root.title("Custom MP3 Player")
root.geometry("300x200")

current_file = ""

def play_music():
    if os.path.exists(file_path):
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
    else:
        print("File does not exist:", file_path)

def play_music1():
    if current_file:
        pygame.mixer.music.play()

def pause_music():
    pygame.mixer.music.pause()

def unpause_music():
    pygame.mixer.music.unpause()

def stop_music():
    pygame.mixer.music.stop()

# Buttons
tk.Button(root, text="Load MP3", command=play_music).pack(pady=5)
tk.Button(root, text="Play", command=play_music).pack(pady=5)
tk.Button(root, text="Pause", command=pause_music).pack(pady=5)
tk.Button(root, text="Unpause", command=unpause_music).pack(pady=5)
tk.Button(root, text="Stop", command=stop_music).pack(pady=5)

root.mainloop()
