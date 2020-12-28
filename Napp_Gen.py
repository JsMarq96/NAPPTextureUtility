import os.path
from TexPackResize import resize_directory, directory_clone
from PackResizer import resize as compress_directory, CMODE
from TexturesBlacklist import load_texture_blacklist, load_texture_scale_whitelist
from TexturesBlacklist import load_file_names, get_file_name

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
    # Load the whitelist and blacklist files
    load_texture_blacklist()
    load_texture_scale_whitelist()
    load_file_names()

    for pack in variations:
        spl_p = pack.split('-')

        dir_name = result_folder #os.path.join(result_folder, str(spl_p[0]) + '_' + spl_p[1] )
        print('Directory res', dir_name)

        new_directory = resize_directory(base_resource_pack, int(spl_p[0]), dir_name, get_file_name(base_resource_pack, spl_p))

        if spl_p[1] != 'None':
            compress_directory(new_directory, COMP_DICT[spl_p[1]])
