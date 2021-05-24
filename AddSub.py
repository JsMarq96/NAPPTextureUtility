import numpy as np 

def add_sub(rgba_img):
    '''
        Custom implementation of the add/sub operation of substance 3D
        based on the investigation of: https://forum.substance3d.com/index.php?topic=6341.msg30658#msg30658
    '''
    rgb_img = np.copy(rgba_img[:, :, 0:2])
    alpha_img = rgba_img[:, :, 3]

    # Add/sub operation
    rgb_img2 = rgb_img + ((rgb_img - 127.5))
    rgb_img2 = rgb_img2 + ((rgb_img2 - 127.5))
    rgb_img = rgb_img + ((rgb_img - 127.5) * 2.0)
    rgb_img = rgb_img + ((rgb_img - 127.5) * 2.0)
    #rgb_img = np.clip(rgb_img + ((rgb_img - 127.5) * 1), 0.0, 255.0)
    #rg_img = rg_img + ((rg_img - 127.5))
    #rgb_img = rgb_img + ((rgb_img - 127.5)) + ((rgb_img - 127.5))
    #rgb_img = rgb_img + ((rgb_img - 127.5))
    rgb_img = np.clip(rgb_img, 0.0, 255.0)

    result = np.copy(rgba_img)
    result[:, :, 0:1] = rgb_img[:, :, 0:1]
    result[:, :, 2:2] = rgb_img2[:, :, 2:2]
    #result[:, :, 2] = rgb_img2[:, :, 2]
    
    return result


if __name__ == '__main__':
    from PIL import Image

    img = np.asarray(Image.open('spruce_log_n_BEFORE.png').convert('RGBA'))

    Image.fromarray(add_sub(img)).save('test.png')