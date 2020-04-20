#!/usr/bin/env python3

import os, platform

if platform.system() == 'Windows':
	commandmv = 'move'
	commandrm = 'rd /s /q'
else:
	commandmv = 'mv'
	commandrm = 'rm -r'

os.system('pyinstaller -y -F -w "MATE"')
os.system('cd dist')
if platform.system() != 'Windows':
	os.system(commandmv + ' MATE MATE.exe')
os.system(commandmv + ' MATE.exe ..')
os.system('cd  ..')
os.system(commandrm + ' build')
os.system(commandrm + ' dist')
