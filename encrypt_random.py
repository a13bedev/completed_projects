import sys
import PyPDF2
import random


def enc_rand(p_file: str, file_to_enc: str) -> None:
    with open(p_file, 'r') as pass_file:
        password = random.choice(pass_file.read().splitlines())
        print(f'The password is:{password}')
    with open(file_to_enc, 'rb+') as pdf_file:
        reader = PyPDF2.PdfFileReader(pdf_file)
        writer = PyPDF2.PdfFileWriter()
        for pageNum in range(reader.numPages):
            writer.addPage(reader.getPage(pageNum))
        writer.encrypt(password)
        writer.write(pdf_file)
        pdf_file.truncate()


def main():
    if len(sys.argv) > 2:
        dict_name = sys.argv[1]
        file_name = sys.argv[2]
        enc_rand(dict_name, file_name)
    else:
        print('Arguments not specified.')


if __name__ == '__main__':
    main()
