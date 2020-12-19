sudo apt update
sudo apt upgrade
sudo apt install 
sudo apt install  python3-pip libimagequant-dev zlib1g-dev libjpeg-dev libpng-dev python3-tk
pip3 install libimagequant
pip3 install pypng
git clone https://github.com/python-pillow/Pillow.git
cd Pillow
sudo MAX_CONCURRENCY=1 python3 Pillow/setup.py build_ext --enable-imagequant install
sudo rm -rf Pillow/