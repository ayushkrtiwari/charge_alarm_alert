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

        self.battery_image_label = tk.Label(root)
        self.battery_image_label.pack(pady=10)

        self.battery_label = tk.Label(root, text="", font=("Helvetica", 14))
        self.battery_label.pack(pady=10)
        
        self.progress = Progressbar(root, orient=tk.HORIZONTAL, length=300, mode='determinate')
        self.progress.pack(pady=10)
        
        self.start_button = tk.Button(root, text="Start Monitoring", command=self.start_monitoring, font=("Helvetica", 12))
        self.start_button.pack(pady=5)

        self.stop_button = tk.Button(root, text="Stop Monitoring", command=self.stop_monitoring, state=tk.DISABLED, font=("Helvetica", 12))
        self.stop_button.pack(pady=5)
        
        self.stop_alarm_button = tk.Button(root, text="Ctrl+Enter", state=tk.DISABLED, font=("Helvetica", 12))
        self.stop_alarm_button.pack(pady=5)
        
        self.is_monitoring = False
        self.alarm_80_triggered = False
        self.alarm_90_triggered 
        