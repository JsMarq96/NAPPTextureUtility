import numpy as np 


def add_sub(rgba_img):
    '''
        Custom implementation of the add/sub operation of substance 3D
        based on the investigation of: https://forum.substance3d.com/index.php?topic=6341.msg30658#msg30658
    '''
    rgb_img = rgba_img[:, :, 0:2]
    alpha_img = rgba_img[:, :, 3]

    # Add/sub operation
    rgb_img = np.clip(rgb_img + (rgb_img - 127.5), 0.0, 255.0)
    rgb_img = np.clip(rgb_img + (rgb_img - 127.5), 0.0, 255.0)
    rgb_img = np.clip(rgb_img + (rgb_img - 127.5), 0.0, 255.0)

    result = np.copy(rgba_img)
    result[:, :, 0:2] = rgb_img
    
    return result


if __name__ == '__main__':
    from PIL import Image

    img = np.asarray(Image.open('spruce_log_n_BEFORE.png').convert('RGBA'))

    Image.fromarray(add_sub(img)).save('test.png')