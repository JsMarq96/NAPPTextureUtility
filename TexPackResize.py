import shutil
import os.path
from PIL import Image
from DirectoryTransversal import file_search
from TexturesBlacklist import get_texture_scale
from multiprocessing import Pool, cpu_count

IMAGE_TYPES = ('.png', '.jpg')


'''
        Texture pack resize utility by Juan S. Marquerie
        Using the PIL library, apply bicubic interpolation in order to escale,
        or downscale the directory
'''

'''
   Function to scale a single image, and save it
'''
def image_scale(img_adress, result_img_adress, new_size):
    img = Image.open(img_adress).convert('RGBA')
    img.resize(new_size, Image.BICUBIC).save(result_img_adress)

def img_scale_adapter(x):
    if x[1] == None:
        return
    image_scale(x[0], x[0], x[1])

def file_dir_crop(x):
    if 'assets' in x:
        return 'assets' + x.rsplit('assets')[1]
    return x

'''
    Function to clone a full folder directory, in order to scale it
'''
def directory_clone(directory, location='', file_name=''):
    new_dir_name = os.path.join(location, file_name)
    print(new_dir_name)
    shutil.copytree(directory, new_dir_name)
        
    return new_dir_name

'''
        Iterate throught a directory, and scale all the images
        to the selected size
'''
def scale_directory(directory, img_types, scale):
    images_in_directory = file_search(img_types, directory)
    images_in_directory = [(x, get_texture_scale(file_dir_crop(x), scale)) for x in images_in_directory]

    print('Scalling ' + str(len(images_in_directory)) + ' on ' + directory +' images...')
    with Pool(processes=cpu_count()) as pool:
        pool.map(img_scale_adapter, images_in_directory)

'''
    (Main function)
     Duplicates a directory and then scales it
'''
def resize_directory(directory, scale, address='', folder_name='', img_types = IMAGE_TYPES):
    new_dir = directory_clone(directory, address, folder_name)
    new_file_direction = os.path.join(address,new_dir)
    scale_directory(new_file_direction, img_types, scale)
    return new_file_direction

'''
    Command interface
'''
if __name__ == '__main__':
    directory = input('Enter Texpack direcction: ')
    new_dim_raw = input('Enter the new texture dimensions with format "W,H: "')

    w = int(new_dim_raw.split(',')[0])
    h = int(new_dim_raw.split(',')[1])

    scaler = TexPackResize((w,h))

    scaler.resize_directory(directory)
