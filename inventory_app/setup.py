from cx_Freeze import setup, Executable

build_options = {
    'packages': [],
    'excludes': [],
    'include_files': ['inventory.db']
}

setup(
    name="InventoryApp",
    version="1.0",
    description="Aplikasi Manajemen Inventory",
    options={'build_exe': build_options},
    executables=[Executable('run.py', base='Win32GUI')]
)