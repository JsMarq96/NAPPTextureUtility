#!/usr/bin/env python3

import os.path

'''
    utility for substituing some textures according to the resolution
    by Juan S. Marquerie
'''

REPLACEMENTLIST_DIR = 'configs/substitution_list.txt'

REPLACEMENTLIST = None

def load_replacements(file_dir = REPLACEMENTLIST_DIR):
    global REPLACEMENTLIST
    REPLACEMENTLIST = {}
    with open(os.path.normpath(file_dir), 'r') as file_replacements:
        lines = file_replacements.readlines()

        for line in lines:
            if line[0] == '#':
                continue # a comment
            tmp = line.rsplit()
            if not tmp[0] in REPLACEMENTLIST:
                REPLACEMENTLIST[tmp[0]] = {}

            REPLACEMENTLIST[tmp[0]][tmp[1]] = tmp[2]


def get_replacement_texture(resolution, text_name):
    global REPLACEMENTLIST

    if not resolution in REPLACEMENTLIST:
        if not text_name in REPLACEMENTLIST[resolution]:
            return None
    return REPLACEMENTLIST[resolution][text_name]

def get_replacement_list(resolution):
    global  REPLACEMENTLIST

    if not resolution in REPLACEMENTLIST:
        return None
    return REPLACEMENTLIST[resolution]
