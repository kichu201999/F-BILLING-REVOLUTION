# from distutils.cmd import Command
# from logging import root
# import tkinter as tk
# from tkinter import ttk
# from tkinter import *
# import webbrowser
# #from xml.etree.ElementPath import _callback
# import webbrowser

# root=tk.Tk()
# root.geometry('400x500')
# name_var = tk.StringVar()
# name_entry =Entry(root,textvariable = name_var, font=('calibre',10,'normal'))
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
# entry = Entry(root)
# entry.pack(padx=50,pady=40)
# # entry.bind('<Return>', select)
# entry.insert( name_var)


# # from slugify import slugify
# # string = name_entry.selection_get()
# # url = slugify(string)
# # print(url)


# root.mainloop()


# # # from tkinter import 
from lib import tkHyperlinkManager
from tkHyperLinkManager import HyperlinkManager
# # # import webbrowser
# # # from functools import partial

# # # # Create an instance of tkinter frame
# # # win = Tk()
# # # win.geometry("700x350")

# # # # Define a callback function
# # # def callback(url):
# # #    webbrowser.open_new_tab(url)

# # # # Create a Label to display the link
# # # text = Text(win)
# # # text.insert(END,"Hey Folks, Welcome to ")
# # # text.pack()
# # # hyperlink= HyperlinkManager(text)

# # # text.insert(END,
# # # "TutorialsPoint",hyperlink.add(partial(webbrowser.open,"http://www.tutorialspoint.com")))

# # # win.mainloop()
# from tkinter import *

# root = Tk()

# text_value = StringVar()
# value = Entry(root)
# value.pack()

# text_rep_trans = StringVar()
# rep_trans = Text(root)
# rep_trans.pack()

# def set_label(name, index, mode):
#     ret_value = text_value.get()
#     if ret_value == '':
#         pass
#     else:
#         rep_trans.insert(END, ret_value)


# text_rep_trans.trace('w', set_label)
# text_value.trace('w', set_label)
# text_rep_trans.set(' ')
# text_value.set(' ')

# root.mainloop()

# import tkHyperlinkManager
 
# from Tkinter import *
 
# root = Tk()
# root.title("hyperlink-1")
 
# text = Text(root)
# text.pack()
 
# hyperlink = tkHyperlinkManager.HyperlinkManager(text)
 
# def click1():
#     print "click 1"
 
# text.insert(INSERT, "this is a ")
# text.insert(INSERT, "link", hyperlink.add(click1))
# text.insert(INSERT, "\n\n")
 
# def click2():
#     print "click 2"
 
# text.insert(INSERT, "this is another ")
# text.insert(INSERT, "link", hyperlink.add(click2))
# text.insert(INSERT, "\n\n")
 
# mainloop()
