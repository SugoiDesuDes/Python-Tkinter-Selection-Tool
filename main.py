# README 
# INSTALLATION: -must install pdf2image with poppler in PATH
# HOW TO USE: set SINGLE_PDF_PATH, run main.py, SelectedRegion will be initailized and printed to console 
# TODO integrate this into the main program as a pop-up when the regions are verified

# Importing required modules
from telnetlib import PRAGMA_HEARTBEAT
from tkinter import *
import tkinter
from tkinter.messagebox import askyesno
from turtle import right
from unittest.case import DIFF_OMITTED
from xml.etree.ElementTree import tostring
from PIL import Image,ImageTk
from pdf2image import convert_from_path
from PyPDF2 import PdfFileReader
from SnipTool import * 
import Models 

selected_region = Models.SelectedRegion() 
SINGLEPAGE_PDF_PATH = r"CLR_Berlin_Problem_Children/lab_formula_inci_supplier_-1-421.001.09-1-probiotic_smart_aging_cream-2017-5-29.pdf"
PDF_HEIGHT = 800 #make sure it fits in a single screen WITHOUT scrolling #TODO support scrolling 

##MULTIPAGE_PDF_PATH = r"148_002_01_magic_bb_cream.pdf" #TODO not currently supported
## SNIPTOOL_PATH = r"C:\Windows\system32\SnippingTool.exe" #deprecated? can we delete this ? 

#region Tkinker Setup 

# Creating Tk container
root = Tk()

# Creating the frame for PDF Viewer
main_frame = Frame(root)
pdf_frame = main_frame.pack(fill=BOTH,expand=0, side = TOP) #TODO pdf_frame is actually none?? 



#cropButton = tkinter.Button(pdf_frame, text="Crop Tool", command=WindowsSnip(SNIPTOOL_PATH))
#cropButton.pack(expand = 0,  side = "left")


# Adding ScrollbarS to the PDF frame
scrol_y = Scrollbar(pdf_frame,orient=VERTICAL)
scrol_x = Scrollbar(pdf_frame, orient=HORIZONTAL)

# Adding text widget for inserting images
pdf = Text(pdf_frame,xscrollcommand=scrol_x.set, yscrollcommand=scrol_y.set,bg="grey")

# Setting the scrollbar to the right side
scrol_y.pack(side=RIGHT,fill=Y)
scrol_x.pack(side=BOTTOM, fill=X)
scrol_y.config(command=pdf.yview)
scrol_x.config(command=pdf.xview)

# Finally packing the text widget
pdf.pack(fill=BOTH ,expand=TRUE, side=TOP)

# Here the PDF is converted to list of images#
pages = convert_from_path(SINGLEPAGE_PDF_PATH, size=(None, PDF_HEIGHT))

# Empty list for storing images
photos = []

# Storing the converted images into list
for i in range(len(pages)):
  photos.append(ImageTk.PhotoImage(pages[i]))

# Adding all the images to the text widget
for photo in photos:
  h = photo.height()
  w = photo.width()

  pdf.image_create(END,image=photo) 


  # For Seperating the pages
  pdf.insert(END,'\n')

root.geometry(str(w) + "x1000")

#if askyesno(title="confirmation", message="Would you like to take a screenshot?"):
#  print("this thing works!!")
#  bruh = subprocess.run([SNIPTOOL_PATH])
# PIL.ImageGrab.grabclipboard()
#img2 = photo.crop([left, upper, right, lower])


#endregion 

#region Mouse Coordinate Retrieval Logic 
px = []
py = []

def onmouse(event):
        #clear px, py if size gets larger than 3 
        if(len(px) == 2): 
          px.clear()
          py.clear()

        px.append(event.x)
        py.append(event.y)


        if(len(px) == 1): 
          print(f"Selected top_left: {event.x} {event.y}")
        else:
          print(f"Selected bottom_right: {event.x} {event.y}")

        width = pages[0].width
        height = PDF_HEIGHT

        #store values in percentages when 2 points have been clicked
        if(len(px) == 2): 
          selected_region.pdf_name = SINGLEPAGE_PDF_PATH #TODO get the filename better idk
          selected_region.top_left = (px[0]/width, px[0]/height) 
          selected_region.bottom_right = (px[1]/width, py[1]/height) 
          print(selected_region)

pdf.bind('<Button-1>',onmouse)

#endregion


mainloop()