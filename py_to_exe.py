from cx_Freeze import setup
from cx_Freeze import Executable

executables = [
    Executable(
        script='renamer.py',
        targetName='photo_renamer.exe',
    )]

setup(name='photo_renamer',
      version='0.1',
      description='Rename the photos according to the time taken.',
      executables=executables)