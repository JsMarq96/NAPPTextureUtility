import os.path
import numpy as np 
from PIL import Image, ImageFilter
from multiprocessing import Pool, cpu_count

from AddSub import add_sub

def generate_normal_address(address, destination_folder):
    base_name = os.path.basename(address)
    return os.path.join(destination_folder, base_name)


def strength_single_normal(params):
    normal_dir, address_result = params
    normal_dir = normal_dir[1:]
    print(normal_dir, params)

    normal = np.asarray(Image.open(normal_dir).convert('RGBA'))
    #Image.fromarray(add_sub(normal)).filter(ImageFilter.BoxBlur(1)).save(address_result)
    Image.fromarray(add_sub(normal)).save(address_result)


def strength_normal_list(normal_list, destination_folder):
    '''
        Given a destination and a list of pngs, strenght the normals
    '''
    full_normal_list = [(x, generate_normal_address(x, destination_folder)) for x in normal_list]

    with Pool(processes=cpu_count()) as pool:
        pool.map(strength_single_normal, full_normal_list)


if __name__ == '__main__':
    tmp = ['spruce_log_n.png', 'spruce_log_n_BEFORE.png', 'test.png']

    strength_normal_list(tmp, 'testi/')