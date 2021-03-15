# NAPP Texture Utility
A utility for resizing and (color) comppressing a Minecraft reource pack (or any folder of images), and exporting it to diferent resoultions.<br/>
Now, it includes a blacklist functionality, that states the textures that can not be reduced (GUI and stuff), and a whitelist functionality, that keeps the aspect ratio of non-square textures, acording to their respective files.
## Functionality
- Batch scale up and down of a folder of images or texture pack, duplicating all the underliying files.
- Blacklist to avoid scalling some images.
- Whitelist to scale to a not standart (1:1) aspect ratio.
- Whitelist to scale to non-standart sizes but based on texture type.
- Export directly to zip.
- Tool to sthenght normal maps, based on the Add/Sub operation of Substance designer.
- Add export names for some configs.
## Depedencies
- libimagequant (pip)
- PyQt5
- Pillow
- multiprocessing
## Linux installation guide
If you are on Ubuntu/debian based distro, you should be able to run the .sh script on the isntaller folder
## Windows installation guide
For now, the program is running on the MYSYS2 instead than on vainilla Windows.
1) Get and install MYSYS2 from https://www.msys2.org/.
2) Then run the windows_installer.bat, wait a bit, press Y when needed.
3) You are ready to go.
