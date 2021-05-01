"""
Program goes through every PDF in a folder (and its subfolders) and decrypt the PDFs
using a password provided on the command line.
Command line arguments: first for path to a folder, second for password.
"""

import PyPDF2
import os
import sys


def decrypt_pdf(path: str, password: str) -> None:
    # Walk through the folder and it's subfolders.
    for curr_folder, subfolder, file_names in os.walk(path):
        for filename in file_names:
            # Check if file is correct.
            if filename.endswith('.pdf'):
                with open(os.path.join(curr_folder, filename), 'rb') as original_file:
                    pdf_reader = PyPDF2.PdfFileReader(original_file)
                    pdf_writer = PyPDF2.PdfFileWriter()
                    if pdf_reader.isEncrypted:
                        if pdf_reader.decrypt(password):
                            for pageNum in range(pdf_reader.numPages):
                                pdf_writer.addPage(pdf_reader.getPage(pageNum))
                            new_name = filename[:-4] + '_decrypted' + filename[-4:]  # Since length of .pdf is 4.
                            with open(os.path.join(curr_folder, new_name), 'wb') as decrypted_file:
                                pdf_writer.write(decrypted_file)
                            # Delete encrypted file.
                            os.unlink(os.path.join(curr_folder, filename))
                        else:
                            print('Wrong password!')


def main():
    path = sys.argv[1]
    password = sys.argv[2]
    decrypt_pdf(path, password)


if __name__ == '__main__':
    main()
