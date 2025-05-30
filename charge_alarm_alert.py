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
        self.alarm_stopped_due_to_disconnection = False 
        self.monitor_battery()  # Start the monitoring process immediately

    def stop_monitoring(self):
        self.is_monitoring = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.stop_alarm()
        self.alarm_80_triggered = False
        self.alarm_90_triggered = False
        self.alarm_100_triggered = False
        self.charger_disconnected_message_shown = False  # Reset the flag
        self.alarm_stopped_due_to_disconnection = False  # Reset the flag
        print("Monitoring stopped.")

    def resize_image(self, image, max_width, max_height):
        width, height = image.size
        ratio = min(max_width / width, max_height / height)
        return image.resize((int(width * ratio), int(height * ratio)), Image.LANCZOS)

    def update_battery_image(self, battery_percentage, charger_connected):
        if charger_connected:
            img = self.charger_connected_image
        else:
            if battery_percentage >= 100:
                img = self.battery_images['full']
            elif battery_percentage >= 90:
                img = self.battery_images['90']
            elif battery_percentage >= 80:
                img = self.battery_images['80']
            elif battery_percentage >= 50:
                img = self.battery_images['50']
            else:
                img = self.battery_images['empty']

        resized_img = self.resize_image(img, 420, 620)
        photo_img = ImageTk.PhotoImage(resized_img)
        self.battery_image_label.config(image=photo_img)
        self.battery_image_label.image = photo_img  # Keep a reference to avoid garbage collection
        print(f"Updated battery image: {battery_percentage}%")

    def monitor_battery(self):
        if self.is_monitoring:
            try:
                print("Checking battery status...")
                battery_percentage = self.get_battery_percentage()
                charger_connected = self.is_charger_connected()
                self.battery_label.config(text=f"Current Battery Percentage: {battery_percentage}%\nCharger Connected: {charger_connected}")
                self.progress['value'] = battery_percentage
                self.update_battery_image(battery_percentage, charger_connected)

                if not charger_connected:
                    if self.alarm_80_triggered or self.alarm_90_triggered or self.alarm_100_triggered:
                        self.stop_alarm()
                        if not self.charger_disconnected_message_shown:
                            messagebox.showinfo("Charger Status", "Charger disconnected.\nStopped alarm.")
                            self.charger_disconnected_message_shown = True  # Flag updated
                        self.alarm_stopped_due_to_disconnection = True  # Flag updated to prevent Alarm Repetition
                    self.alarm_80_triggered = False
                    self.alarm_90_triggered = False
                    self.alarm_100_triggered = False
                else:
                    self.charger_disconnected_message_shown = False  # Reset the flag when charger is connected
                    self.alarm_stopped_due_to_disconnection = False  # Reset the flag when charger is connected
                    if battery_percentage >= 100 and not self.alarm_100_triggered:
                        self.play_alarm('siren_100.mp3', loop=True)
                        self.alarm_100_triggered = True
                        self.root.after(500, lambda: messagebox.showwarning("Battery Full", "Battery 100%! Disconnect charger.\nPress Ctrl+Enter to stop alarm."))
                    elif battery_percentage >= 90 and battery_percentage < 100 and not self.alarm_90_triggered and not self.alarm_stopped_due_to_disconnection:
                        self.play_alarm('siren_90.mp3')
                        self.alarm_90_triggered = True
                        self.root.after(500, lambda: messagebox.showwarning("Battery Alert", "Battery above 90%! Disconnect charger.\nPress Ctrl+Enter to stop alarm."))
                    elif battery_percentage >= 80 and battery_percentage < 90 and not self.alarm_80_triggered and not self.alarm_stopped_due_to_disconnection:
                        self.play_alarm('siren_80.mp3')
                        self.alarm_80_triggered = True
                        self.root.after(500, lambda: messagebox.showinfo("Battery Info", "Battery above 80%. Disconnect charger.\nPress Ctrl+Enter to stop alarm."))
            except Exception as e:
                print(f"Error in monitoring battery: {e}")

            # Schedule the next battery check after 5 seconds
            self.root.after(5000, self.monitor_battery)

    def on_closing(self):
        print("Application closing...")
        self.stop_alarm()  # Stop the alarm when the application is closed
        self.root.destroy()  # Close the application

if __name__ == "__main__":
    root = tk.Tk()
    app = ChargeAlarmApp(root)
    root.mainloop()

# Author: Ayush Kumar Tiwari , IIIT Bhagalpur
# Save this file as charge_alarm_alert.py
# Run below line in terminal 
# pyinstaller --onefile --add-data "empty_battery.png;." --add-data "battery_50.jpg;." --add-data "battery_80.jpg;." --add-data "battery_90.png;." --add-data "full_battery.jpg;." --add-data "charger_connected.jpg;." --add-data "charger_disconnected.png;." --add-data "siren_80.mp3;." --add-data "siren_90.mp3;." --add-data "siren_100.mp3;." charge_alarm_alert.py
