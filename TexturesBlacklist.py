#!/usr/bin/env python3

import os.path
from RadixTree import RadixTree

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

BLACKLIST_DIR = 'configs/texture_blacklist.txt'
WHITELIST_DIR = 'configs/texture_whitelist.txt'
FILENAMELIST_DIR = 'configs/filename_config.txt'

BLACKLIST = None
WHITELIST = None
FILENAMES = {}

'''
    Load the blacklist
'''
def load_texture_blacklist(file_dir = BLACKLIST_DIR):
    global BLACKLIST
    BLACKLIST = RadixTree(True)
    with open(os.path.normpath(file_dir), 'r') as file_blacklist:
        lines = file_blacklist.readlines()

        for line in lines:
            if line[0] == '#':
                continue # Comment
            BLACKLIST.add(os.path.normpath(line.replace('\n', '')), False)
    print(BLACKLIST)

'''
    Generate the whitelist of the non-square textures
'''
def load_texture_scale_whitelist(file_dir = WHITELIST_DIR):
    global WHITELIST
    WHITELIST = RadixTree((1,1))
    with open(os.path.normpath(file_dir), 'r') as file_whitelist:
        lines = file_whitelist.readlines()

        for line in lines:
            if line[0] == '#':
                continue  # a Comment
            tmp = line.rsplit()
            file_name = tmp[0]
            tmp = tmp[1].rsplit(',')

            WHITELIST.add(os.path.normpath(file_name), (float(tmp[0]), float(tmp[1])))
    print(WHITELIST)

def load_file_names(file_dir = FILENAMELIST_DIR):
    global FILENAMES
    FILENAMES = {}
    with open(os.path.normpath(file_dir), 'r') as file_whitelist:
        lines = file_whitelist.readlines()

        for line in lines:
            if line[0] == '#':
                continue  # a Comment
            tmp = line.rsplit()
            FILENAMES[tmp[0]] = tmp[1]


def get_texture_scale(name, base_scale):
    global BLACKLIST
    global WHITELIST

    if not BLACKLIST.get_with_wildcard(name):
        print('Skip ', name)
        return None
    tmp = WHITELIST.get_with_wildcard(name)
    return (int(base_scale * tmp[0]), int(base_scale * tmp[1]))

def get_file_name(file_dir, config):
    global FILENAMES
    config_str = config[0] + '-' + config[1]
    if not config_str in FILENAMES:
        return os.path.basename(file_dir) + '_' + config[0] + 'x' + config[1]

    return FILENAMES[config_str]
