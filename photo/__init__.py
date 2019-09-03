"""
photo
=====

Provide
    (1) tools to rename photos in a certain path.

Author
------
    Yuhao Zhu

History
-------
    v0.1, 20170425
        Rename the photos in a path with the date_time_id.
    v0.2, 20180423
        Update the program. Now it is .py rather than .ipynb file.
    v0.3, 20190903
        Change the module for more general purposes. Rename is now only a function.
"""

__authors__ = 'Yuhao Zhu'
__version__ = '0.3'

import os
import sys
import exifread
import datetime

# Get the current working directory.
path = os.getcwd()
path = r'{}'.format(path)
path = path.replace('\\', '/')

def pwd(path=path):
    print(path)
    

def rename(path=path):
    _directory, _sub_directory, old_name_list = list(os.walk(path))[0]

    print('The following photos have been renamed.')
    print('---------------------------------------')
    list_name_main = []
    for old_name in old_name_list:
        old_file = '{}/{}'.format(path, old_name)
        # Get the extention of file.
        extention = old_name.split('.')[-1].upper()
        if extention in ['CR2', 'JPG', 'JPEG']:
            read_photo = open(old_file, 'rb')
            tags = exifread.process_file(read_photo)
            try:
                time_taken_str = str(tags['Image DateTime'])
            except:
                time_taken_str = str(tags['EXIF DateTimeOriginal'])
            time_taken = datetime.datetime.strptime(time_taken_str, '%Y:%m:%d %H:%M:%S')
            name_datetime = datetime.datetime.strftime(time_taken, '%Y%m%d_%H%M%S')
            name_main = '{}'.format(name_datetime)
            name_count = 1
            # If the file name does not repeat.
            while (name_main, name_count, extention) in list_name_main:
                name_count += 1
            if (name_main, name_count, extention) not in list_name_main:
                list_name_main.append((name_main, name_count, extention))
                new_name = '{0}_{1:04}.{2}'.format(name_main, name_count, extention)
            new_file = '{}/{}'.format(path, new_name)
            read_photo.close()
            os.rename(old_file, new_file)
            print('{}\t->\t{}'.format(old_name, new_name))

# Run once imported
_directory, _sub_directory, old_name_list = list(os.walk(path))[0]

print('The following photos have been renamed.')
print('---------------------------------------')
list_name_main = []
for old_name in old_name_list:
    old_file = '{}/{}'.format(path, old_name)
    # Get the extention of file.
    extention = old_name.split('.')[-1].upper()
    if extention in ['CR2', 'JPG', 'JPEG']:
        read_photo = open(old_file, 'rb')
        tags = exifread.process_file(read_photo)
        try:
            time_taken_str = str(tags['Image DateTime'])
        except:
            time_taken_str = str(tags['EXIF DateTimeOriginal'])
        time_taken = datetime.datetime.strptime(time_taken_str, '%Y:%m:%d %H:%M:%S')
        name_datetime = datetime.datetime.strftime(time_taken, '%Y%m%d_%H%M%S')
        name_main = '{}'.format(name_datetime)
        name_count = 1
        # If the file name does not repeat.
        while (name_main, name_count, extention) in list_name_main:
            name_count += 1
        if (name_main, name_count, extention) not in list_name_main:
            list_name_main.append((name_main, name_count, extention))
            new_name = '{0}_{1:04}.{2}'.format(name_main, name_count, extention)
        new_file = '{}/{}'.format(path, new_name)
        read_photo.close()
        os.rename(old_file, new_file)
        print('{}\t->\t{}'.format(old_name, new_name))