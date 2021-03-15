echo on
title NAPP Texture utility installer on MSYS2"
C:\msys64\msys2_shell.cmd -mingw64 -here -c './linux_installer.sh; read -t 10 -n 1'
pip3 install pyqt5 Pillow numpy
exit
