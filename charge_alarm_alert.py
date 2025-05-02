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
        self.alarm_90_triggered = False
        self.alarm_100_triggered = False
        self.charger_disconnected_message_shown = False  
        self.alarm_stopped_due_to_disconnection = False  

        # Path to the directory where the executable will be installed
        base_path = os.path.dirname(os.path.abspath(__file__))
        print(f"Base path: {base_path}")

        # Load images
        try:
            self.battery_images = {
                'empty': Image.open(os.path.join(base_path, "empty_battery.png")),
                '50': Image.open(os.path.join(base_path, "battery_50.jpg")),
                '80': Image.open(os.path.join(base_path, "battery_80.jpg")),
                '90': Image.open(os.path.join(base_path, "battery_90.png")),
                'full': Image.open(os.path.join(base_path, "full_battery.jpg")),
            }
            self.charger_connected_image = Image.open(os.path.join(base_path, "charger_connected.jpg"))
            self.charger_disconnected_image = Image.open(os.path.join(base_path, "charger_disconnected.png"))
            print("Images loaded successfully.")
        except Exception as e:
            print(f"Error loading images: {e}")

        # Bind Ctrl + Enter to stop the alarm
        root.bind('<Control-Return>', lambda event: self.stop_alarm_action())
        print("Ctrl + Enter key binding added.")

        # Bind window close event
        root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def get_battery_percentage(self):
        battery = psutil.sensors_battery()
        return battery.percent

    def is_charger_connected(self):
        battery = psutil.sensors_battery()
        return battery.power_plugged

    def play_alarm(self, sound_file, loop=False):
        pygame.mixer.music.load(sound_file)
        if loop:
            pygame.mixer.music.play(-1)
        else:
            pygame.mixer.music.play()
        self.stop_alarm_button.config(state=tk.NORMAL)
        print("Alarm playing, Stop Alarm button enabled.")

    def stop_alarm_action(self):
        print("Stop Alarm button pressed.")
        self.stop_alarm()
        self.stop_alarm_button.config(state=tk.DISABLED)
        print("Alarm stopped.")

    def stop_alarm(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
            print("Pygame music stopped.")

    def start_monitoring(self):
        self.is_monitoring = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        print("Monitoring started.")
        self.charger_disconnected_message_shown = False  
        self.alarm_stopped_due_to_disconnection = False # initialised false

    