import zlib
import zipfile
import os
from PIL import Image
from TexPackResize import resize_directory
from PackResizer import resize as compress_directory, CMODE
from TexturesBlacklist import load_texture_blacklist, load_texture_scale_whitelist
from TexturesBlacklist import load_file_names, get_file_name
from TextureReplacment import get_replacement_list, load_replacements

'''
    TODO cleanup the Texture replacement: refactor names, and cleanup... inda nasty
'''


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


def generate_resourcepacks(base_resource_pack, variations, result_folder, name_subst = '', zip_it=False):
    # Load the whitelist and blacklist files
    load_texture_blacklist()
    load_texture_scale_whitelist()
    load_file_names()
    load_replacements()

    for pack in variations:
        spl_p = pack

        dir_name = result_folder #os.path.join(result_folder, str(spl_p[0]) + '_' + spl_p[1] )
        print('Directory res', dir_name)

        # Texture pack replacement
        pack_export_name = get_file_name(base_resource_pack, spl_p)
        if '@' in pack_export_name:
            tmp = pack_export_name.split('@')
            pack_export_name = tmp[0] + name_subst + tmp[1]

        new_directory = resize_directory(base_resource_pack, int(spl_p[0]), dir_name, pack_export_name)

        if spl_p[1] != 'None':
            compress_directory(new_directory, COMP_DICT[spl_p[1]])

        file_replacement_dict = get_replacement_list(pack)

        if not file_replacement_dict is None:
            for texture_dest in file_replacement_dict:
                text_to_replace = Image.open(file_replacement_dict[texture_dest])
                text_to_replace.save(os.path.join(new_directory, texture_dest))
                print('TO REPLACE', new_directory, texture_dest)

        if zip_it:
            folder_name = os.path.basename(new_directory)
            zip_name = new_directory + '.zip'
            zip_file = zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED)
            for root, _, files in os.walk(new_directory):
                for file in files:
                    name_str = os.path.join(root, file)

                    zip_name = name_str.split(folder_name)[1]

                    zip_file.write(name_str, arcname=zip_name)

            zip_file.close()
