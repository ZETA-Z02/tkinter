# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['catalogo_peliculas.py'],
    pathex=['/home/zeta/Escritorio/proyectos/tkinter/catalogo-peliculas/catalogo_peliculas.py'],
    binaries=[],
    datas=[('./database/*.db','database')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='catalogo_peliculas',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='catalogo_peliculas',
)
