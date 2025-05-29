;INNO SETUP SCRIPT FILE
;REFER TO DOCUMENTATION FOR MORE DETAIL: "https://jrsoftware.org/ishelp.php"

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{YOUR-GUID-HERE}}
AppName=Charge Alarm
AppVersion=1.0
DefaultDirName={pf}\Charge Alarm
DefaultGroupName=Charge Alarm
OutputDir=.
OutputBaseFilename=ChargeAlarmSetup
Compression=lzma
SolidCompression=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Files]
Source: "dist\charge_alarm_alert.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "empty_battery.png"; DestDir: "{app}"; Flags: ignoreversion
Source: "battery_50.jpg"; DestDir: "{app}"; Flags: ignoreversion
Source: "battery_80.jpg"; DestDir: "{app}"; Flags: ignoreversion
Source: "battery_90.png"; DestDir: "{app}"; Flags: ignoreversion
Source: "full_battery.jpg"; DestDir: "{app}"; Flags: ignoreversion
Source: "charger_connected.jpg"; DestDir: "{app}"; Flags: ignoreversion
Source: "charger_disconnected.png"; DestDir: "{app}"; Flags: ignoreversion
Source: "siren_80.mp3"; DestDir: "{app}"; Flags: ignoreversion
Source: "siren_90.mp3"; DestDir: "{app}"; Flags: ignoreversion
Source: "siren_100.mp3"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\Charge Alarm"; Filename: "{app}\charge_alarm_alert.exe"
