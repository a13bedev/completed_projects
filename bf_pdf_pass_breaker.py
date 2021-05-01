"""
This program decrypts the PDF by trying every possible english word until it finds one
that works and prints the hacked password.
"""

import PyPDF2
import sys


def bf_breaker(dic_file: str, pdf_file: str) -> None:
    with open('dictionary.txt', 'r') as pass_file, open('test2.pdf', 'rb') as pdf_file:
        reader = PyPDF2.PdfFileReader(pdf_file)
        if reader.isEncrypted:
            for word in pass_file.read().splitlines():
                if reader.decrypt(word) or reader.decrypt(word.lower()):
                    sys.exit('Hacked password is: %s' % word)
            print('Password is not found!')
        else:
            print('File is not encrypted!')


def main():
    if len(sys.argv) > 2:
        dict_of_words = sys.argv[1]
        f_to_break = sys.argv[2]
        bf_breaker(dict_of_words, f_to_break)
    else:
        print('Arguments not provided.')


if __name__ == '__main__':
    main()
