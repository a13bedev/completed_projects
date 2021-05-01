"""
Program takes two integers and a filename
string as command line arguments.
Let’s call the first integer N and the second integer M.
Starting at row N, the program inserts M blank rows into the spreadsheet.
First argument for N, second for M, third for file name.
"""

import openpyxl
import sys


def create_rows(n: int, m: int, file_name: str) -> None:
    # Get active worksheet from given file.
    wb = openpyxl.load_workbook(file_name)
    ws = wb.active
    # Insert M blank rows starting at row N.
    ws.insert_rows(n, m)
    wb.save(file_name)
    wb.close()


def main():
    if len(sys.argv) > 3:
        n = int(sys.argv[1])
        m = int(sys.argv[2])
        file_name = sys.argv[3]
        create_rows(n, m, file_name)
    else:
        print('Arguments not provided.')


if __name__ == '__main__':
    print(main)
