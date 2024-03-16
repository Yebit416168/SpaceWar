# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['alien_invasion.py'],
    pathex=['alien.py','alien1.py','alien2.py','alienbullet.py','alienbullet1.py','alienbullet2.py','background.py','bomb.py','bullet.py','button.py','gamesprite.py','scoreboard.py','settings.py','ship.py','skill.py'],
    binaries=[],
    datas=[('.\\music\\*.ogg', '.\\music'),('.\\font\\*.ttf', '.\\font'),('.\\images\\spritesheets\\*.png', '.\\images\\spritesheets'),('.\\images\\backgrounds\\*.png', '.\\images\\backgrounds')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)
splash = Splash(
    'images\\spritesheets\\qidong.png',
    binaries=a.binaries,
    datas=a.datas,
    text_pos=None,
    text_size=12,
    minify_script=True,
    always_on_top=True,
)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    splash,
    splash.binaries,
    [],
    name='太空大战',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['pygame.ico'],
)
