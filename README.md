# NAPP Texture Utility
A utility for resizing and (color) comppressing a Minecraft reource pack (or any folder of images), and exporting it to diferent resoultions.<br/>
Now, it includes a blacklist functionality, that states the textures that can not be reduced (GUI and stuff), and a whitelist functionality, that keeps the aspect ratio of non-square textures, acording to their respective files.
## Functionality
- Batch scale up and down of a folder of images or texture pack, duplicating all the underliying files.
- Blacklist to avoid scalling some images.
- Whitelist to scale to a not standart (1:1) aspect ratio.
- Export directly to zip.
- Add export names for some configs.
## Depedencies
- libimagequant (pip)
- tkinter
- Pillow
- multiprocessing
## Linux installation guide
If you are on Ubuntu/debian based distro, you should be able to run the .sh scrip on the isntaller folder
## Windows installation guide
For now, the program is running on the Windows Linux Subsystem instead than on vainilla Windows.
1) On the Turn Windows Features On or Off pannel, select to enable Windows Subsystem fro Linux and reboot your computer.
2) Install the Ubuntu 20.04 program from the Microsoft store.
3) Launch it and wait for the installation, and set up you user and password of you tiny Linux installation.
4) Install Xming, a X server windows manager, in order to get a GUI from the Ubuntu install; from https://sourceforge.net/projects/xming/.
5) Then run the WSL_installer.bat on the installer folder, accept the downloads and you are ready to go!
