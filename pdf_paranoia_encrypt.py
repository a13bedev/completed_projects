"""
Program goes through every PDF in a folder (and its subfolders) and encrypt the PDFs
using a password provided on the command line.
Command line arguments: first for path to a folder, second for password.
"""

import PyPDF2
import os
import sys


def encrypt_pdf(path: str, password: str) -> None:
    # Walk through the folder and it's subfolders.
    for curr_folder, subfolder, file_names in os.walk(path):
        for filename in file_names:
            # Check if an extension of a file is correct.
            if filename.endswith('.pdf'):
                with open(os.path.join(curr_folder, filename), 'rb') as original_file:
                    pdf_reader = PyPDF2.PdfFileReader(original_file)
                    pdf_writer = PyPDF2.PdfFileWriter()
                    # Copy pages from reader to writer.
                    if not pdf_reader.isEncrypted:
                        for pageNum in range(pdf_reader.numPages):
                            pdf_writer.addPage(pdf_reader.getPage(pageNum))
                        # Encrypt writer obj.
                        pdf_writer.encrypt(password)
                        # Save encrypted file with new name.
                        new_name = filename[:-4] + '_encrypted' + filename[-4:]  # Since length of .pdf is 4.
                        with open(os.path.join(curr_folder, new_name), 'wb') as encrypted_file:
                            pdf_writer.write(encrypted_file)
                        # Safety check. Decrypt encrypted file if possible. If so delete the original one.
                        with open(os.path.join(curr_folder, new_name), 'rb') as check_file:
                            pdf_reader_enc = PyPDF2.PdfFileReader(check_file)
                            if pdf_reader_enc.decrypt(password):
                                os.unlink(os.path.join(curr_folder, filename))
                            else:
                                print("Decryption failure! Can't delete original file!")


def main():
    path = sys.argv[1]
    password = sys.argv[2]
    encrypt_pdf(path, password)


if __name__ == '__main__':
    main()
