from TexPackResize import resize_directory, directory_clone
from PackResizer import resize as compress_directory, CMODE

def resize(origin_folder, result_folder, scale):
    resize_directory(origin_folder, result_folder, scale)


def compress(origin_folder, result_folder):
    result_dir = directory_clone(origin_folder, result_folder, '_Zero')
    compress_directory(result_dir,  { 'COLOR': CMODE.LIGHT,
                                       'NORN': CMODE.LIGHT,
                                       'SPEC': CMODE.HEAVY
                                     })


def generate_resource_packs(base_resource_pack, variations, result_folder):
    for var in variations:
        if var.scale:
            resize(base_resource_pack, result_folder, var.scale)

        if var.compress:
            compress(base_resource_pack, result_folder)
