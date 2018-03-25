
# coding: utf-8

# In[1]:

"""
Purpose:
    Rename the photos in a path with the time taken.

Author:
    Yuhao Zhu

Versions:
    20170425: Rename the photos in a path with the date_time_id.
"""

import os
import sys
import exifread
cwd = os.getcwd()
import datetime


# In[2]:

# Imput the path of the folder.
path = input("Input path\n")
path = r'{}'.format(path)
path = path.replace('\\', '/')
directory, sub_directory, file_list = list(os.walk(path))[0]
for i in range(len(file_list)):
    file_list[i] = '{}/{}'.format(path, file_list[i])


# In[3]:

list_name_main = []
for file in file_list:
    extention = file.split('.')[-1]
    if extention in ['CR2', 'JPG']:
        read_photo = open(file, 'rb')
        tags = exifread.process_file(read_photo)
        try:
            time_taken_str = str(tags['Image DateTime'])
        except:
            time_taken_str = str(tags['EXIF DateTimeOriginal'])
        time_taken = datetime.datetime.strptime(time_taken_str, '%Y:%m:%d %H:%M:%S')
        name_datetime = datetime.datetime.strftime(time_taken, '%Y%m%d_%H%M%S')
        name_main = '{}_0001'.format(name_datetime)
        # If the file name does not repeat.
        while name_main in list_name_main:
            name_main_split = name_main.split('_')
            name_main_split[-1] = int(name_main_split[-1]) + 1
            name_main = '{0}_{1}_{2:04}'.format(name_main_split[0], name_main_split[1], name_main_split[2])
            name = '{}.{}'.format(name_main, extention)
        if name_main not in list_name_main:
            list_name_main.append(name_main)
            name = '{}.{}'.format(name_main, extention)
        new_name = '{}/{}'.format(path, name)
        read_photo.close()
#     print(file)
#     print(new_name)
        os.rename(file, new_name)


# In[ ]:



