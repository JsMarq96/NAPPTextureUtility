import os.path
from TexPackResize import resize_directory, directory_clone
from PackResizer import resize as compress_directory, CMODE

def resize(origin_folder, result_folder, scale):
    return resize_directory(origin_folder, result_folder, scale)


def compress(origin_folder, result_folder, comp_dict):
    #result_dir = directory_clone(origin_folder, result_folder, '_Zero')
    compress_directory(result_folder, comp_dict)

COMP_DICT = { 'Light': { 'COLOR': CMODE.LIGHT,
                         'NORM': CMODE.LIGHT,
                         'SPEC': CMODE.LIGHT},
               'Hard': { 'COLOR': CMODE.HEAVY,
                         'NORM': CMODE.HEAVY,
                         'SPEC': CMODE.HEAVY},
               'Light w/Hard Speculars': { 'COLOR': CMODE.LIGHT,
                                           'NORM': CMODE.LIGHT,
                                           'SPEC': CMODE.HEAVY}
             }

def generate_resourcepacks(base_resource_pack, variations, result_folder):
    for pack in variations:
        spl_p = pack.split('-')

        resize(base_resource_pack, int(spl_p[0]), os.path.join(result_folder, str(spl_p[0]) + '_' + spl_p[1] ))

        if spl_p[1] != 'None':
            compress(base_resource_pack, result_folder, COMP_DICT[spl_p[1]])
