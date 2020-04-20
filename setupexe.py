#!/usr/bin/env python3

import os, platform

programpath = 'MATE.exe'
if platform.system() == 'Windows':
	commandmv = 'move'
	programname = 'MATE.exe'
else:
	commandmv = 'mv'
	programname = 'MATE'

os.system('pyinstaller -y -F -w "MATE"')
os.system(commandmv + ' ' + os.path.join(os.getcwd(),'dist',programname) + ' ' + os.path.join(os.getcwd(),programpath))
