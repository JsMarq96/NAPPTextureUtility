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
    image_scale(x[0], x[0], x[1])

    '''
        Function to clone a full folder directory, in order to scale it
    '''
def directory_clone(directory, location='', add_on=''):
    print(directory, 'add on: ', add_on)
    new_dir_name = os.path.join(location, os.path.basename(directory+ '_' + str(add_on)))
    print(new_dir_name)
    shutil.copytree(directory, new_dir_name)
        
    return new_dir_name

'''
        Iterate throught a directory, and scale all the images
        to the selected size
'''
def scale_directory(directory, img_types, scale):
    images_in_directory = file_search(img_types, directory)
    images_in_directory = [(x, get_texture_scale(x, scale)) for x in images_in_directory]

    print('Scalling ' + str(len(images_in_directory)) + ' images...')
    with Pool(processes=cpu_count()) as pool:
        pool.map(img_scale_adapter, images_in_directory)

'''
    (Main function)
     Duplicates a directory and then scales it
'''
def resize_directory(directory, scale, address='', img_types = IMAGE_TYPES):
    print(scale)
    new_dir = directory_clone(directory, address, str(scale) + 'x')
    scale_directory(os.path.join(address,new_dir), img_types, (scale, scale))


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
