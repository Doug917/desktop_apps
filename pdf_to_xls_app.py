def pdftoxls(pdfname):

	import re

	# importing required modules
	import PyPDF2
  
	# creating a pdf file object
	pdfFileObj = open(pdfname, 'rb')
  
	# creating a pdf reader object
	p = PyPDF2.PdfReader(pdfFileObj)

	#Create output text file.
	output = open(pdfname + ".txt", "w")

	n = len(p.pages)
  
	for i in range(0,n):
		# creating a page object
		pageObj = p.pages[i]
  
		# extracting text from page
		s = pageObj.extract_text()

		output.write(s)

	# closing the pdf file object
	pdfFileObj.close()
	output.close()

	#Now, fill a list with all data.
	skus = []
	units = []
	f = open(pdfname + ".txt", 'r')
	for line in f.readlines():
		try:
			begin = re.search("[A-Z][A-Z][A-Z][0-9]", line).start()
			end = line.find(' ', begin)
			skus.append(line[begin:end])
			units.append(line[-2])
		except:
			pass

	f.close()
	f = open(pdfname + ".txt",'a')
	L = len(skus)
	f.write("\n")
	for i in range(0,L):
		f.write(skus[i]+"\n")
	for i in range(0,L):
		f.write(units[i]+"\n")

	f.close()

	import xlwt
	from xlwt import Workbook
  
	# Workbook is created
	wb = Workbook()
  
	# add_sheet is used to create sheet.
	sheet1 = wb.add_sheet('Sheet 1')

	for i in range(0,L):
		sheet1.write(i, 0, skus[i])
		sheet1.write(i, 1, units[i])
  
	wb.save(pdfname + '.xls')

#------------------------------------------------------------------------------

# Import Module
from tkinter import *
 
# create root window
root = Tk()
 
# root window title and dimension
root.title("PDF_order_extract")
# Set geometry (widthxheight)
root.geometry('500x200')

#adding a label to the root window
lbl = Label(root, text = "Key in name of PDF.")
lbl.grid()

# adding Entry Field
txt = Entry(root, width=50)
txt.grid(column =1, row =0)

# function to display user text when
# button is clicked
def clicked():
 
    res = txt.get()
    pdftoxls(res)
 
# button widget with red color text inside
btn = Button(root, text = "Run" ,
             fg = "black", command=clicked)
# Set Button Grid
btn.grid(column=2, row=0)
 
# all widgets will be here
# Execute Tkinter
root.mainloop()

