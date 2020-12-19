echo on
title NAPP Texture Utility Launcher”
START "XWindowLauncher" "C:\Program Files (x86)\Xming\Xming.exe" :0 -clipboard -multiwindow
ubuntu2004 run DISPLAY=:0 python3 GUI.py
exit
