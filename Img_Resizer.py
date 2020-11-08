#!/usr/bin/env python3

from PIL import Image
from enum import Enum


class CMODE(Enum):
    NONE  = 0
    LIGHT = 1,
    HEAVY = 2

   
def img_compress(file_dir='', mode=CMODE.NONE):
    imgs = Image.open(file_dir)
    print(file_dir, mode)
    if mode == CMODE.LIGHT:
        imgs.quantize(256, method=3, dither=0).save(file_dir)
    elif mode == CMODE.HEAVY:
        imgs.quantize(256, method=2, dither=0).save(file_dir)

    i = 0
