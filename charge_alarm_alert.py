import os
import time  # Import the time module
from PIL import Image, ImageTk
import tkinter as tk # Control display, positioning, control of widgets. TK is top level widget.
from tkinter import messagebox
from tkinter.ttk import Progressbar
import psutil
import pygame

# Initialize pygame mixer
pygame.mixer.init()

class ChargeAlarmApp:
    def __init__(self, root):
        self.root = root         
        self.root.title("Charge Alarm")

        self.label = tk.Label(root, text="Battery Monitor", font=("Helvetica", 16))
        self.label.pack(pady=10)

        # Now Image Graphics Improvement