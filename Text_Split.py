import numpy as np
from PIL import Image


def split_text(text_source, split_nums, save_dir='', img_format='.png'):
    for suffix in ['', '_n', '_s']:
        img = np.asarray(Image.open(text_source + suffix + '.png').convert('RGB'))
        w, h, dims = img.shape
        n_w = int(w/int(split_nums))
        n_h = int(h/int(split_nums))

        for e_i, i in enumerate(range(0, w, n_w)):
            for e_j, j in enumerate(range(0, h, n_h)):
                slice_img = img[i:i+n_w, j:j+n_h, 0:dims]
                file_name = save_dir + str((e_i * 16) + (e_j)) + suffix + '.png'
                Image.fromarray(slice_img.astype(np.uint8)).save(file_name)


if __name__ == '__main__':
    split_text('t/stone', 4)
