## Charge Alarm v 1.0

OS based Application for battery features and overcharging alarm alert


### INSTALLATION : For End Users

Download the latest version from:
[Releases](https://github.com/ayushkrtiwari/charge_alarm_alert/releases/tag/v1.0)


### USAGE MANUAL : For Developers

Disable Firewall or Antivirus software. 
Download the files.

#### Using PYINSTALLER: Portable (No Installation)
- Install `pyinstaller` using: `pip install pyinstaller` on `CLI`
- Run on pyinstaller: 
```
    pyinstaller --onefile --add-data "empty_battery.png;." --add-data "battery_50.jpg;." --add-data "battery_80.jpg;." --add-data "battery_90.png;." --add-data "full_battery.jpg;." --add-data                          "charger_connected.jpg;." --add-data "charger_disconnected.png;." --add-data "siren_80.mp3;." --add-data "siren_90.mp3;." --add-data "siren_100.mp3;." charge_alarm_alert.py
```
- You will get `.exe` executable file under /dist directory.
- Run the file `charge_alarm_alert.exe`

#### Using INNO Setup Compiler: Full Installation

    Copy paste the given `.iss` script: `charge_alarm_script.iss` into INNO Setup Compiler
    Generate AppID in Tools -> Generate GUID 
    Place generated GUID into AppID
    Run the script
    Follow the instructions
    Run Application `ChargeAlarmAlert.exe` 


### FEATURES:

    Alarm Alerts prior to full charge
    Monitoring Mode options
    Multithreading, multitasking
    Sleep Cycle, Yield, efficient CPU cycles


### BACKGROUND

This alarm is solely for purpose for overcharging batteries leading to overheating and reduced 
battery life, hence it helps out in increasing battery life cycle. The inspiration for creation 
of the app was for my personal purpose with the reason as stated above. Personally, due to this
cause, the device battery got dead multiple times.


### FOREGROUND

Many versions of this app will be launched in future with each of them aiming to optimize the
functioning and reduce load over the device. GUI is not the case for system apps since the
sole purpose of this app is to avoid overcharging, keeping in fact to reduce number of machine
cycles used, ensure least memory and CPU usage, running on multiple threads for multithreading,etc.


### AIM

Other than the stated facts, this application aims to maximize efficiency per CPU cycle and 
better synchronization with concurrent running applications.


### Future Updates

The near future updates aim to introduce following concepts:

    Mandatory Full Volume
    Alarm rings until battery disconnects, optional settings
    Reduced CPU usage and least GUI update
    Firewall bypass
    Granted Administrator Access and execute when device charging starts
    Sleep delay between cycles to reduce CPU usage and avoid busy-waiting
    Improved multithreading concurrently with simultaneously running applications
    Prevent excessive thread usage in case of contention using sleep cycles
    Throttling: Optimize to control the speed of thread execution along with other applications
    Based on user's feedbacks, will customize application for other purposes
