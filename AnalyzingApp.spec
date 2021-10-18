# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['AnalyzingApp.py', 'MyModules\\__init__.py','MyModules\\advancedData.py','MyModules\\Aj.py','MyModules\\AllanBill.py','MyModules\\art.py','MyModules\\doTheMath.py','MyModules\\ranking.py','MyModules\\ranking.py','MyModules\\readFiles.py','MyModules\\regularData.py','MyModules\\TimerLoadBar.py','MyModules\\typingData.py'],
             pathex=['C:\\Users\\dovilivob\\Desktop\\pyexe_test'],
             binaries=[],
             datas=[],
             hiddenimports=['cython','pymysql','pandas._libs.tslibs.timedeltas','sklearn.neighbors.typedefs','sklearn.utils.typedefs','_bootlocale'],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=['_bootlocale'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='AnalyzingApp',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
