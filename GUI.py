import PyPDF2
from PyPDF2 import PdfFileWriter, PdfFileReader
from tkinter import *
# root configuration
root = Tk()
root.title("pdf modifier".upper())
root.geometry("1000x1000")
root.config(background="#dae6f6")


# functions
def seperator():
    inputpdf = PdfFileReader(open(enter_text3.get()+ ".pdf", "rb"))
    for i in range(inputpdf.numPages):
        output = PdfFileWriter()
        output.addPage(inputpdf.getPage(i))
        with open("document-page%s.pdf" % i, "wb") as outputStream:
            output.write(outputStream)
    done = Label(root, text="split is done!!".upper(), font=("Trebuchet Ms", 20), bg="#dae6f6", fg="#000000")
    done.place(x=420, y=890)
    root.after(4000, done.destroy)


def merge():
    f1 = open(f"{enter_text11.get()}.pdf", "rb")
    f2 = open(f"{enter_text12.get()}.pdf", "rb")
    new_file = "merged".upper()
    pdf1 = PyPDF2.PdfFileReader(f1)
    pdf2 = PyPDF2.PdfFileReader(f2)

    list_of_pdf = [pdf1, pdf2]
    merge = PyPDF2.PdfFileMerger()
    for file in list_of_pdf:
        merge.append(file)
    merge.write(f"{new_file}.pdf")
    done = Label(root, text="merge is done!!".upper(), font=("Trebuchet Ms", 20), bg="#dae6f6", fg="#000000")
    done.place(x=420, y=300)
    root.after(4000, done.destroy)
    merge.close()



def extract():
    pdf_name = open(f"{enter_text2.get()}.pdf", "rb")
    pdf = PdfFileReader(pdf_name)
    new_pdf = PdfFileWriter()
    page_num = list(map(int, enter_text21.get().split()))

    for page in page_num:
        new_pdf.addPage(pdf.getPage(page))
    new_pdf_name = "extracted".upper()
    with open(f"{new_pdf_name}.pdf", "wb") as f:
        new_pdf.write(f)
        f.close()
    done = Label(root, text="extracting pages done!!".upper(), font=("Trebuchet Ms", 20), bg="#dae6f6", fg="#000000")
    done.place(x=360, y=600)
    root.after(4000, done.destroy)


# merge function buttons, headings and entries
heading11 = Label(root, text="first file name: ".title(), font=("Trebuchet Ms", 20), bg="#dae6f6", fg="#364971", justify="left")
heading11.place(x=50, y=80)
enter_text11 = Entry(root, justify="center", width=20, font=("timesnewroman",15),bg="white",border=2)
enter_text11.place(x=100, y=150)

heading12 = Label(root, text="second file name: ".title(), font=("Trebuchet Ms", 20), bg="#dae6f6", fg="#364971", justify="left")
heading12.place(x=700, y=80)
enter_text12 = Entry(root, justify="center", width=20, font=("timesnewroman",15),bg="white",border=2)
enter_text12.place(x=750, y=150)

enter_text11.focus()
button11 = Button(root, text="merge".upper(), font=("timesnewroman", 15, "bold"), fg="white", bg= "gray15", command=merge)
button11.place(x=480, y=230)





# extract function button, headings and entries
heading2 = Label(root, text="name of pdf to extract: ".title(), font=("Trebuchet Ms", 20), bg="#dae6f6", fg="#364971", justify="left")
heading2.place(x=50, y=400)
enter_text2 = Entry(root, justify="center", width=20, font=("timesnewroman",15),bg="white",border=2)
enter_text2.place(x=100, y=460)
enter_text2.focus()
button2 = Button(root, text="extract".upper(), font=("timesnewroman", 15, "bold"), fg="white", bg= "gray15", command=extract )
button2.place(x=470, y=550)

heading21 = Label(root, text="pages nums: ".title(), font=("Trebuchet Ms", 20), bg="#dae6f6", fg="#364971", justify="left")
heading21.place(x=700, y=400)
enter_text21 = Entry(root, justify="center", width=20, font=("timesnewroman", 15),bg="white",border=2)
enter_text21.place(x=750, y=460)




# split function button, headings and entries
heading3 = Label(root, text="pdf name you want to split: ".title(), font=("Trebuchet Ms", 20), bg="#dae6f6", fg="#364971", justify="left")
heading3.place(x=340, y=730)
enter_text3 = Entry(root, justify="center", width=20, font=("timesnewroman",15),bg="white",border=2)
enter_text3.place(x=400, y=810)
enter_text3.focus()
button3 = Button(root, text="split".upper(), font=("timesnewroman", 15, "bold"), fg="white", bg= "gray15", command=seperator, )
button3.place(x=480, y=850)



root.mainloop()





