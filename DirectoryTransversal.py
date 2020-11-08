import os

'''
    Directory Transversal
    by Juan S. Marquerie
    Here are the functions for transversing a nested
    folder structure, in search for a type of file
'''

'''
    Recursivelly search the inputed directory, in order
    to find the inputed file extensions
'''
def file_search(file_extensions = (''), root_dir = '.'):
    files_dir = []

    seperator = '/'
    if os.name == 'nt':
        seperator = '\\'

    for element in os.listdir(root_dir):
        elem_dir = root_dir + seperator + element

        # Add to the list if it is an image, and if it
        # is a folder, recursivelly read its contents
        if os.path.isfile(elem_dir):
            if elem_dir.endswith(file_extensions):
                files_dir.append(elem_dir)
        else:
            files_dir = files_dir + file_search(file_extensions, elem_dir)

    return files_dir


if __name__ == '__main__':
    # Test the function
    print(file_search(('.png')))