#! /usr/bin/python3
# backup_to_zip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments. Place ZIP file into provided folder.
import sys
import os
import shutil


def bu_to_zip(folder: str) -> None:
    folder = os.path.abspath(folder)
    # Create file name with increment
    count = 1
    while True:
        zip_file_name = os.path.basename(folder) + '_' + str(count) + '.zip'
        if not os.path.exists(zip_file_name):
            break
        count += 1
    # Create zip file of provided folder
    shutil.make_archive(zip_file_name, 'zip', folder)


def main():
    if len(sys.argv) > 1:
        directory = sys.argv[1]
        bu_to_zip(directory)
    else:
        print('Argument not specified.')


if __name__ == "__main__":
    main()
