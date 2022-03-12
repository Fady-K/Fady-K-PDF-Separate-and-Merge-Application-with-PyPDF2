import PyPDF2
from PyPDF2 import PdfFileReader
from PyPDF2 import PdfFileWriter
programme_running = True
choice = None
first_time = True
def display():
    global choice, first_time
    if first_time:
        print("!! welcome !!".upper())
    print(f"1- Merge two files\n2- Extract a page from a file\n3- Split file into separate pages\n4- Exit")
    choice = int(input("what do you want to do?".title()))
    first_time = False
    return choice


def merge():
    f1 = open(f"{input('first_file_name_: ')}.pdf", "rb")
    f2 = open(f"{input('second_file_name: ')}.pdf", "rb")
    new_file = input("new_File_name: ")
    pdf1 = PyPDF2.PdfFileReader(f1)
    pdf2 = PyPDF2.PdfFileReader(f2)

    list_of_pdf = [pdf1, pdf2]
    merge = PyPDF2.PdfFileMerger()
    for file in list_of_pdf:
        merge.append(file)
    merge.write(f"{new_file}.pdf")
    print("!!merging done!\n".upper())
    merge.close()





def extract():
    pdf_name = open(f"{input('Please enter the name of pdf file: ')}.pdf", "rb")
    pdf = PdfFileReader(pdf_name)
    new_pdf = PdfFileWriter()
    page_num = list(map(int, input("Please enter the number of pages you want to extract: ").split()))

    for page in page_num:
        new_pdf.addPage(pdf.getPage(page))
    new_pdf_name = input("please enter the new name of your pdf: ")
    with open(f"{new_pdf_name}.pdf", "wb") as f:
        new_pdf.write(f)
        f.close()
    print("Extratcting pages done!!!\n".upper())




def split():
   my_pdf = PdfFileReader(open(input("enter the pdf name: ".title())+".pdf", "rb"))
   for page in range(my_pdf.numPages):
       pdf_writer = PyPDF2.PdfFileWriter()
       pdf_writer.addPage(my_pdf.getPage(page))
       with open("document-page%s.pdf" % page, "wb") as f:
           pdf_writer.write(f)
           f.close()
   print("split done!!!\n".upper())

display()
while programme_running:
    if choice == 1:
        merge()

    elif choice == 2:
        extract()

    elif choice == 3:
        split()

    elif choice == 4:
        quit()
    display()

