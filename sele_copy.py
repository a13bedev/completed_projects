#! /usr/bin/python3
# Program walks through a folder tree and searches for files with a certain file extension (such as .pdf or .jpg).
# Copy these files from whatever location they are in to a new folder.

import sys
import os
import shutil
from typing import List


def create_new_dir(directory: str) -> str:
    path = os.path.join(directory, os.path.basename(directory))
    if not os.path.exists(path):
        os.mkdir(path)
        return path
    else:
        print('Error. Path already exists.')
        return ''


def copy_files(directory: str, destination: str, extensions: List[str]) -> None:
    for root, dirs, files in os.walk(directory):
        for fi in files:
            if fi.endswith(tuple(extensions)):
                try:
                    shutil.copyfile(os.path.join(root, fi), os.path.join(destination, fi))
                except shutil.SameFileError:
                    continue


def main():
    orig_dir = sys.argv[1]
    extensions = sys.argv[2:]
    if extensions:
        new_dir = create_new_dir(orig_dir)
        print(f'\nAbs path to a new directory is:\n{new_dir}')
        copy_files(orig_dir, new_dir, extensions)
        print('')
    else:
        print('Error. Extensions not specified.')


if __name__ == '__main__':
    main()
