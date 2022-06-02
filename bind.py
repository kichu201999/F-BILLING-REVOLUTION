#from distutils.cmd import Command
# from logging import root
# import tkinter as tk
# from tkinter import *
# from tkinter import Web_Browser
# #from xml.etree.ElementPath import _callback
# import webbrowser

# root=tk.Tk()
# root.geometry('400x500')
# name_var = tk.StringVar()
# name_entry = tk.Entry(root,textvariable = name_var, font=('calibre',10,'normal'))
# name_entry.pack(padx=15,pady=20)
# # name_entry.selection_get()
# # print(name_var)
# # name_entry.bind("<<Button-1>>",lambda e:callback("www.tutorialspoint.com"))

# def callback(url):
#     webbrowser.open_new(url)

# b1=tk.Button(root, text= "get selection",command=lambda:select())
# b1.pack()
# def select():
#    cotent = name_entry.selection_get()
#    #cotent.bind("<<Button-1>>",lambda e:callback("www.tutorialspoint.com"))
#    print(cotent)




# root.mainloop()



# from slugify import slugify
# string = "how to convert string to hyperlink"
# url = slugify(string)
# print(url)

from tkinter import *
from tkHyperLinkManager import HyperlinkManager
import webbrowser
from functools import partial

# Create an instance of tkinter frame
win = Tk()
win.geometry("700x350")

# Define a callback function
def callback(url):
   webbrowser.open_new_tab(url)

# Create a Label to display the link
text = Text(win)
text.insert(END,"Hey Folks, Welcome to ")
text.pack()
hyperlink= HyperlinkManager(text)

text.insert(END,
"TutorialsPoint",hyperlink.add(partial(webbrowser.open,"http://www.tutorialspoint.com")))

win.mainloop()