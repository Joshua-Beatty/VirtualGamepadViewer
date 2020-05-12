from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [], include_files = ['README.md', 'Skins/','icon.png']
	)

import sys
base = 'Win32GUI' if sys.platform=='win32' else None


executables = [
Executable('VirtualGamepadViewer.py',
	base=base,
	icon="icon.ico")
]

setup(name='Virtual Gamepad Viewer',
	version = '1.0',
	description = '',
	options = dict(build_exe = buildOptions),
	executables = executables)
