# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['bilibili_title_extractor.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('title_parser.py', '.'),
    ],
    hiddenimports=['PyQt5.QtCore', 'PyQt5.QtGui', 'PyQt5.QtWidgets', 'requests', 'urllib3', 'charset_normalizer', 'idna', 'certifi'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='B站标题提取器',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=True,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='B站标题提取器',
)
app = BUNDLE(
    coll,
    name='B站标题提取器.app',
    bundle_identifier='com.biligui.titleextractor',
    info_plist={
        'CFBundleShortVersionString': '1.0.0',
        'NSHighResolutionCapable': 'True',
        'LSUIElement': 'False',
    },
) 