from tkinter.constants import PAGES
from PyPDF2 import PdfFileWriter, PdfFileReader
import tkinter as tk
from tkinter import filedialog
import ntpath
import os


output_pdf = PdfFileWriter()

# grab the location of the file path sent
def path_leaf(path):
    head, tail = ntpath.split(path)
    return head

# graphical file selection
def grab_file_path():
    # use dialog to select file
    file_dialog_window = tk.Tk()
    file_dialog_window.withdraw()  # hides the tk.TK() window
    # use dialog to select file
    grabbed_file_path = filedialog.askopenfilename()
    return grabbed_file_path


# file to be reversed
filePath = grab_file_path()

# open file and read
with open(filePath, 'rb') as readfile:
    input_pdf = PdfFileReader(readfile)

    output_pdf.addPage(input_pdf.getPage(0))
    output_pdf.addPage(input_pdf.getPage(11))
    output_pdf.addPage(input_pdf.getPage(12))
    output_pdf.addPage(input_pdf.getPage(13))
    output_pdf.addPage(input_pdf.getPage(14))
    output_pdf.addPage(input_pdf.getPage(15))
    output_pdf.addPage(input_pdf.getPage(16))
    output_pdf.addPage(input_pdf.getPage(17))
    output_pdf.addPage(input_pdf.getPage(18))
    output_pdf.addPage(input_pdf.getPage(19))
    output_pdf.addPage(input_pdf.getPage(8))
    output_pdf.addPage(input_pdf.getPage(3))
    output_pdf.addPage(input_pdf.getPage(4))
    output_pdf.addPage(input_pdf.getPage(9))
    output_pdf.addPage(input_pdf.getPage(10))
    output_pdf.addPage(input_pdf.getPage(5))
    output_pdf.addPage(input_pdf.getPage(6))
    output_pdf.addPage(input_pdf.getPage(1))
    output_pdf.addPage(input_pdf.getPage(2))
    output_pdf.addPage(input_pdf.getPage(7))

    # reverse order one page at time
    #for page in reversed(input_pdf.pages):
    #    output_pdf.addPage(page)

    # graphical way to get where to select file starting at input file location
    dirOfFileToBeSaved = path_leaf(filePath)
    locationOfFileToBeSaved=filedialog.asksaveasfilename(initialdir=dirOfFileToBeSaved, initialfile='name of reversed file.pdf',title="Select or type file name and location", filetypes=[("pdf files", "*.pdf")])
    # write the file created
    with open(locationOfFileToBeSaved, "wb") as writefile:
        output_pdf.write(writefile)

# open the file when done
#os.startfile(locationOfFileToBeSaved)