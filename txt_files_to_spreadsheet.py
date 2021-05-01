"""
This program takes folder with several text files (.txt) as command line argument.
Then read in the contents of files and insert those contents into a spreadsheet,
with one line of text per row.
The lines of the first text file will be in the cells of
column A, the lines of the second text file will be in the cells of column B,
and so on.
"""

import openpyxl
import sys
import os


def create_spreadsheet(path: str) -> None:
    # Create workbook with a spreadsheet
    wb = openpyxl.Workbook()
    ws = wb.active
    # Iterate trough a folder. If extension is .txt start to read lines and write 'em to the sheet.
    file_names = os.listdir(path)
    for filename in file_names:
        if filename.endswith('.txt'):
            with open(filename, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    ws.cell(row=lines.index(line)+1, column=file_names.index(filename)+1).value = line
    # Save book in cwd and close it.
    wb.save("resulting_file.xlsx")
    wb.close()


def main():
    # Take a path to a folder and set it cwd.
    if len(sys.argv) > 1:
        path = sys.argv[1]
        os.chdir(path)
    else:
        print('Argument not specified.')


if __name__ == '__main__':
    main()
