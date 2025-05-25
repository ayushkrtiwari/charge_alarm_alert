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
Source: "dist\charge_alarm_alert.exe"; DestDir: "{app}"
