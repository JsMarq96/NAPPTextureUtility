#!/usr/bin/env python3

import os.path.normpath

'''
    Loads the blacklist of texutres/images that you dont need to
    resize
    by Juan S. Marquerie

    Blacklist Format:
        List of texture names and dirs, relative to the folder
    Whitelist formal
        texture/dir 1.0,2.0

    TODO: Externalice the config dirs
'''

BLACKLIST_DIR = 'texture_blacklist.txt'
WHITELIST_DIR = 'texture_whitelist.txt'

BLACKLIST = []
WHITELIST = {}

'''
    Load the blacklist
'''
def load_texture_blacklist(file_dir = BLACKLIST_DIR):
    global BLACKLIST
    BLACKLIST = []
    with open(file_dir, 'r') as file_blacklist:
        lines = file_blacklist.readlines()

        for line in lines:
            if line[0] == '#':
                continue # Comment
            BLACKLIST.append(os.path.normpath(line.replace('\n', '')))

    print(BLACKLIST)

'''
    Generate the whitelist of the non-square textures
'''
def load_texture_scale_whitelist(file_dir = WHITELIST_DIR):
    global WHITELIST
    WHITELIST = {}
    with open(file_dir, 'r') as file_whitelist:
        lines = file_whitelist.readlines()

        for line in lines:
            if line[0] == '#':
                continue  # a Comment
            tmp = line.rsplit()
            file_name = tmp[0]
            tmp = tmp[1].rsplit(',')

            WHITELIST[os.path.normpath(file_name)] = (float(tmp[0]), float(tmp[1]))
    print(WHITELIST)

def get_texture_scale(name, base_scale):
    global BLACKLIST
    global WHITELIST
    if name in BLACKLIST:
        return None
    if name in WHITELIST.keys():
        tmp = WHITELIST[name]
        return (int(tmp[0] * base_scale), int(tmp[1] * base_scale))
    else:
        return (base_scale, base_scale)
