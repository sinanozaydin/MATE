#!/usr/bin/env python3

import os, platform

if platform.system() == 'Windows':
	commandmv = 'move'
else:
	commandmv = 'mv'

os.system('pyinstaller -y -F -w "MATE"')
os.system(commandmv + ' ' + os.path.join(os.getcwd(),'dist','MATE.exe') + ' .')
