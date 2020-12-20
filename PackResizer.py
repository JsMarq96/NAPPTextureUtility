#!/usr/bin/env python3

from Img_Resizer import CMODE, img_compress
from DirectoryTransversal import file_search
from multiprocessing import Pool, cpu_count
from PIL import Image


def resize_img(file_dir):
    img_compress(file_dir[0], file_dir[1])

       
def resize(pack_dir='.', file_term={}):
    print('############# ' + pack_dir)
    file_dirs = file_search(('.png'), pack_dir)
    file_dirs_tuple= []

    for f_dir in file_dirs:
        if '_n' in f_dir:
            type_data = file_term['NORM']
        elif '_s' in f_dir:
            type_data = file_term['SPEC']
        else:
            type_data = file_term['COLOR']

        file_dirs_tuple.append((f_dir, type_data))

    with Pool(processes=cpu_count()) as pool:
        pool.map(resize_img, file_dirs_tuple)



if __name__ == '__main__':
    file_modes = { 'COLOR': CMODE.LIGHT,
                   'NORM': CMODE.LIGHT,
                   'SPEC':CMODE.HEAVY
                  }
    resize('/home/js/.minecraft/resourcepacks/NAPP_1024x_1.4.1_red/assets/minecraft', file_modes)
    print('finished')
