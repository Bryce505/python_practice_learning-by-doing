#! python3
# combine_pdfs.py --combines all the current working directory into a single pdf

from PyPDF2 import PdfFileReader, PdfFileWriter
from os import listdir

def get_all_files():
    # get all the pdf filenames
    pdf_files = []
    for file_name in listdir('.'):
        if file_name.endswith('.pdf'):
            pdf_files.append(file_name)
    pdf_files.sort(key=str.lower)
    return pdf_files

def add_pages(pdf_files):
    # loop through all the pages
    pdf_writer = PdfFileWriter()
    for file_name in pdf_files:
        pdf_file_obj = open(file_name,'rb')
        pdf_reader = PdfFileReader(pdf_file_obj)
        # loop through all the pages(except the first) and add them
        for page_num in range(1,pdf_reader.numPages):
            page_obj = pdf_reader.getPage(page_num)
            pdf_writer.addPage(page_obj)
    pdf_file_obj.close()
    return pdf_writer
def save_file(pdf_writer):
    # save the resulting pdf to a file
    with open('combine_pdfs.pdf','wb') as pdf_output:
        pdf_writer.write(pdf_output)

if __name__ == '__main__':
    pdf_files = get_all_files()
    pdf_writer = add_pages(pdf_files)
    save_file(pdf_writer)









