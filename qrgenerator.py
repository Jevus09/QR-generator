import pyqrcode
import PIL.Image
from tkinter import *

root = Tk()
root.title("QR Generator")

#Create a Label widget
e = Entry(root, width=40, borderwidth=10)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
e.insert(0, "enter the url")

#Define a functino to create and open qr code
def button_open():
    link = e.get()
    qr_code = pyqrcode.create(link)
    qr_code.png(f"{e.get().replace('.com', '')}.png", scale= 10)
    im = PIL.Image.open(f"{e.get().replace('.com', '')}.png")
    im.show()
    e.delete(0, END)
    e.insert(0, "enter the url")

#Define a function to clear the content of the text widget
def click(event):
   e.configure(state=NORMAL)
   e.delete(0, END)
   e.unbind('<Button-1>', clicked)


#Bind the Entry widget with Mouse Button to clear the content
clicked = e.bind('<Button-1>', click)


#Create and set button
download = Button(root, text="Generate", padx=40, pady=20, command=button_open)
download.grid(row=4, column=0,  columnspan=3)


root.mainloop()
