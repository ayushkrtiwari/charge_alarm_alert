# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['charge_alarm_alert.py'],
    pathex=[],
    binaries=[],
    datas=[('empty_battery.png', '.'), ('battery_50.jpg', '.'), ('battery_80.jpg', '.'), ('battery_90.png', '.'), ('full_battery.jpg', '.'), ('charger_connected.jpg', '.'), ('charger_disconnected.png', '.'), ('siren_80.mp3', '.'), ('siren_90.mp3', '.'), ('siren_100.mp3', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='charge_alarm_alert',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
