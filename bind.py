 #from ast import pattern
from calendar import c
from cgitb import enable, text
from distutils import command
from itertools import count
from pydoc import describe
from secrets import choice
from sqlite3 import enable_callback_tracebacks
import string
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.font import BOLD
from urllib.parse import parse_qs
from xml.dom.minidom import Entity
from PIL import ImageTk, Image, ImageFile
from matplotlib.font_manager import json_dump
from numpy import choose, empty, place
import pandas as pd
from tkinter.messagebox import showinfo
import tkinter.scrolledtext as scrolledtext
from tkinter.filedialog import askopenfilename
import os
import webbrowser
from pip import main
from tkcalendar import Calendar
from tkcalendar import DateEntry
from datetime import date
from tkinter import filedialog
import subprocess
import mysql.connector
import io
from openpyxl.workbook import Workbook
from openpyxl import load_workbook
import shutil
import csv
import json
from tkinter import font,colorchooser

fbilldb = mysql.connector.connect(
    host="localhost", user="root", password="", database="fbillingsintgrtd5", port="3306"
)
fbcursor = fbilldb.cursor()

ImageFile.LOAD_TRUNCATED_IMAGES = True

def reset():
  global root
  root.destroy()


# root.title("F-Billing Revolution 2022(FREE version) | Company database:fbillingdb | User:Administrator")

    
  
invoices= PhotoImage(file="images/invoice.png")
orders = PhotoImage(file="images/order.png")
estimates = PhotoImage(file="images/estimate.png")
recurring = PhotoImage(file="images/recurring.png")
purchase = PhotoImage(file="images/purchase.png")
expenses = PhotoImage(file="images/expense.png")
customer = PhotoImage(file="images/customer.png")
product = PhotoImage(file="images/package.png")
reports = PhotoImage(file="images/report.png")
setting = PhotoImage(file="images/setting.png")
tick = PhotoImage(file="images/check.png")
warnin = PhotoImage(file="images/sign_warning.png")
cancel = PhotoImage(file="images/close.png")
saves = PhotoImage(file="images/save.png")
folder = PhotoImage(file="images/folder-black.png")
photo11 = PhotoImage(file = "images/invoice-pvt.png")
customer = PhotoImage(file="images/customer.png")
smslog = PhotoImage(file = "images/smslog.png")
video = PhotoImage(file = "images/video.png")
mark1 = PhotoImage(file="images/mark.png")
mark2 = PhotoImage(file="images/mark2.png")
photo10 = PhotoImage(file = "images/text-message.png")
addnew = PhotoImage(file="images/plus.png")
delete = PhotoImage(file="images/delete_E.png")

selectall = PhotoImage(file="images/table_select_all.png")
cut = PhotoImage(file="images/cut.png")
copy = PhotoImage(file="images/copy.png")
paste = PhotoImage(file="images/paste.png")

undo = PhotoImage(file="images/undo.png")
redo = PhotoImage(file="images/redo.png")
bold = PhotoImage(file="images/bold.png")

italics = PhotoImage(file="images/italics.png")
underline = PhotoImage(file="images/underline.png")
left = PhotoImage(file="images/left.png")
  
right = PhotoImage(file="images/right.png")
center = PhotoImage(file="images/center.png")
hyperlink = PhotoImage(file="images/hyperlink.png")
color = PhotoImage(file="images/font_color.png")
remove = PhotoImage(file="images/eraser.png")
  
  
photo = PhotoImage(file = "images/plus.png")
photo1 = PhotoImage(file = "images/edit.png")
photo2 = PhotoImage(file = "images/delete_E.png")
photo3 = PhotoImage(file = "images/export-file.png")
photo4 = PhotoImage(file = "images/seo.png")
photo5 = PhotoImage(file = "images/printer.png")
photo6 = PhotoImage(file = "images/gmail.png")
photo7 = PhotoImage(file = "images/priewok.png")
photo8 = PhotoImage(file = "images/refresh_E.png")
photo9 = PhotoImage(file = "images/sum.png")
photo10 = PhotoImage(file = "images/text-message.png")

# est_logo = PhotoImage(file = "images/company_logo.png")

def mainpage():
  root.iconify()
  main = Toplevel()
  main.geometry("1360x730")
  p1 = PhotoImage(file = 'images/fbicon.png')
  main.iconphoto(False, p1)
  main.title("F-Billing Revolution 2022(FREE version) | Company database:fbillingdb | User:Administrator")
  s = ttk.Style()
  s.theme_use('default')
  s.configure('TNotebook.Tab', background="#999999", width=20, padding=10)
  tabControl = ttk.Notebook(main)
  tab1 = ttk.Frame(tabControl)
  tab2 = ttk.Frame(tabControl)
  tab3=  ttk.Frame(tabControl)
  tab4 = ttk.Frame(tabControl)
  tab5 = ttk.Frame(tabControl)
  tab6=  ttk.Frame(tabControl)
  tab7 = ttk.Frame(tabControl)
  tab8 = ttk.Frame(tabControl)
  tab9 =  ttk.Frame(tabControl)
  tab10=  ttk.Frame(tabControl)
  tabControl.add(tab1,image=invoices,compound = LEFT, text ='Invoices',)
  tabControl.add(tab2,image=orders,compound = LEFT, text ='Orders')
  tabControl.add(tab3,image=estimates,compound = LEFT, text ='Estimates')
  tabControl.add(tab4,image=recurring,compound = LEFT, text ='Recurring')
  tabControl.add(tab5,image=purchase,compound = LEFT, text ='Purchase Orders') 
  tabControl.add(tab6,image=expenses,compound = LEFT, text ='Expenses')
  tabControl.add(tab7,image=customer,compound = LEFT, text ='Customers')
  tabControl.add(tab8,image=product,compound = LEFT, text ='Product/Services')
  tabControl.add(tab9,image=reports,compound = LEFT, text ='Report')
  tabControl.add(tab10,image=setting,compound = LEFT, text ='Settings')
  tabControl.pack(expand = 1, fill ="both")
  
  

  
  # def log():
  #   global user_name1
  #   user_name1=username1.get()
  #   passwd1=password1.get()
  #   if user_name1=="" or passwd1=="":
  #       Label(screen2,text='Plz enter both username and password',fg='red').place(x=85,y=260)
  #   else:
  #       sql='SELECT * FROM users WHERE username=%s AND password=%s'
  #       val=(user_name1,passwd1,)
  #       fbcursor.execute(sql,val)
  #       if fbcursor.fetchone()is not None:
  #           root(user_name1)
  #       else:
  #           messagebox.showinfo('Acess denied','Acess denied')
  
  # sql = "select * from users"
  # fbcursor.execute(sql)
  # user_log = fbcursor.fetchall()
  # if not user_log:
  #   pass
  # else:
  #     screen2=Toplevel()
  #     screen2.title('LOGIN')
  #     screen2.geometry('400x300')
  
  #     username1=StringVar()
  #     password1=StringVar()
  
  #     Label(screen2,text='Login Here').pack()
  #     uss1=Label(screen2,text='Username').place(x=50,y=70)
  #     ee1 = Entry(screen2,textvariable=username1).place(x=140,y=70)
  
  #     pss1=Label(screen2,text='Password').place(x=50,y=110)
  #     ee2=Entry(screen2,textvariable=password1).place(x=140,y=110)
  
  #     submitbtn1=Button(screen2,text='Login', width=20,height=2,command=log).place(x=70,y=200)
  
  # def check_empty() :
  #      if entry.get():
  #         pass     #your function where you want to jump
  #      else:
  #         messagebox.showinfo("Information", "Required entry")
  
  
  ######################## FRONT PAGE OF CUSTOMER SECTION   #######################################################################
  
      
  settingsframe=Frame(tab10, relief=GROOVE, bg="#f8f8f2")
  settingsframe.pack(side="top", fill=BOTH)
  
  settframe=Frame(settingsframe, bg="#f5f3f2", height=60)
  settframe.pack(side="top", fill=X)
  
  pn = Canvas(settframe, width=1, height=65, bg="#b3b3b3", bd=0)
  pn.pack(side="left", padx=(5, 2))
  pn = Canvas(settframe, width=1, height=65, bg="#b3b3b3", bd=0)
  pn.pack(side="left", padx=(0, 5))
  # def upload_filelogo():
  #   global imglogo,filename
  #   f_types =[('Png files','*.png'),('Jpg Files', '*.jpg')]
  #   filena = filedialog.askopenfilename(filetypes=f_types)
  #   shutil.copyfile(filena, os.getcwd()+'/images/'+filena.split('/')[-1])
  #   print(filena.split('/')[-1])
  #   image = Image.open(filena)
  #   resize_image = image.resize((280, 160))
  #   imglogo = ImageTk.PhotoImage(resize_image)
    # b2 = Button(secondtab,image=img)
    # b2.place(x=130, y=80)
  
    # btlogo = Button(secondtab,width=280,height=160,image=imglogo)
    # btlogo.place(x=580,y=280)
  global filename
  filename = ""
  def save_company():
    pord_prefix = prefix_str.get()
    pord_spin = spin2.get()
    pord_header = win_menu.get()
    pord_text1 = pord_str1.get()
    pord_text2 = pord_str2.get()
    pord_text3 = pord_str3.get()
    pord_text4 = pord_str4.get()
    pord_text5 = pord_str5.get()
    pord_text6 = pord_str6.get()
    pord_text7 = pord_str7.get()
    pord_predefind = pord_str8.get()
   
    # var = json.dumps(child)
    sql = "select image from company"
    fbcursor.execute(sql)
    im = fbcursor.fetchone()
    sql = "select * from company"
    fbcursor.execute(sql)
    i = fbcursor.fetchall()
    if not i:
      if filename == "":
        print(12)
        sql = 'insert into company(  porder_prefix,headrebox_color,starting_porderno,text_label1,text_label2,text_label3,text_label4,text_label5,text_label6,text_label7,predefindterms_porder,email_template) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        val = (pord_prefix,pord_spin,pord_header,pord_text1,pord_text2,pord_text3,pord_text4,pord_text5,pord_text6,pord_text7,pord_predefind)
        fbcursor.execute(sql, val)
        fbilldb.commit()
      else:
        shutil.copyfile(filename, os.getcwd()+'/images/'+filename.split('/')[-1])
        sql = 'insert into company(porder_prefix,headrebox_color,starting_porderno,text_label1,text_label2,text_label3,text_label4,text_label5,text_label6,text_label7,predefindterms_porder,email_template) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        val = (pord_prefix,pord_spin,pord_header,pord_text1,pord_text2,pord_text3,pord_text4,pord_text5,pord_text6,pord_text7,pord_predefind)
        fbcursor.execute(sql, val)
        fbilldb.commit()
    else:
      if filename == "":
        sql = "update company set porder_prefix=%s,headrebox_color=%s,starting_porderno=%s,text_label1=%s,text_label2=%s,text_label3=%s,text_label4=%s,text_label5=%s,text_label6=%s,text_label7=%s,predefindterms_porder=%s,email_template=%s"
        val = (pord_prefix,pord_spin,pord_header,pord_text1,pord_text2,pord_text3,pord_text4,pord_text5,pord_text6,pord_text7,pord_predefind)
        fbcursor.execute(sql, val)
        fbilldb.commit()
      else:
        shutil.copyfile(filename, os.getcwd()+'/images/'+filename.split('/')[-1])
        sql = "update company set porder_prefix=%s,headrebox_color=%s,starting_porderno=%s,text_label1=%s,text_label2=%s,text_label3=%s,text_label4=%s,text_label5=%s,text_label6=%s,text_label7=%s,predefindterms_porder=%s,email_template=%s"
        val = (pord_prefix,pord_spin,pord_header,pord_text1,pord_text2,pord_text3,pord_text4,pord_text5,pord_text6,pord_text7,pord_predefind)
        fbcursor.execute(sql, val)
        fbilldb.commit()
      
 ################### tab010 ###################################

  tentab1=Frame(tab010, relief=GROOVE, bg="#f8f8f2")
  tentab1.pack(side="top", fill=BOTH)

  tentab=Frame(tentab1, bg="#f5f3f2", height=700)
  tentab.pack(side="top", fill=BOTH)


  sql = "select * from company"
  fbcursor.execute(sql)
  podata = fbcursor.fetchone()
  

  ver = Label(tentab,text="Purchase order# prefix")
  ver.place(x=15,y=25)

  prefix_str = StringVar()
  pre_entry = Entry(tentab,textvariable=prefix_str)
  pre_entry.place(x=16,y=50)
  if not podata:
    prefix_str.set('P.ORD')
  else:
    pre_entry.insert(0, podata[41])


  ver1 = Label(tentab,text="Starting purchase order number")
  ver1.place(x=15,y=75)

  def spincall(input):
        
    if input.isdigit():
      print(input)
      return True

    elif input is  "":
      print(input)
      return True

    else:
      print(input)
      return False
    

  spin2 = Spinbox(tentab,from_=0,to=1000000,width=16)
  regi = tentab.register(spincall)

  spin2.config(validate = "key",
               validatecommand = (regi, '%S'))
  if not podata:
    pass
  else:
    spin2.delete(0,END)
    spin2.insert(0,podata[43])
    spin2.place(x=16,y=100)

    
              

  ver2 = Label(tentab,text="Header box background color")
  ver2.place(x=15,y=140)

  pwin_menu = StringVar()
  colbox = ttk.Combobox(tentab,textvariable=pwin_menu,width=27)
  colbox.place(x=15 ,y=160)
  pord_win = pwin_menu.get()
  colbox['values'] = ('Default','Black','Maroon','Green','Olive','Navy','Purple','Teal','Gray','Silver','Red','Lime','Yellow','Blue','Fuchsia','Aqua','White','ScrollBar','Background','ActiveCaption','InactiveCaption','Menu','Window','WindowFrame','MenuText','WindowText','CaptionText','ActiveBorder','InactiveBorder','AppWorkSpace','Highlight','HighlightText','BtnFace','InactiveCaptionText','BtnHighlight','3DDkShadow','3DLight','InfoText','InfoBk','Custom')
  if not podata:
    colbox.current(0)
  else:
    colbox.insert(0, podata[42])

  ver3 = Label(tentab,text="Customize purchase order text labels")
  ver3.place(x=15,y=190)

  pord_str1 = StringVar() 
  pord_lbx1 = Entry(tentab, width=30,textvariable=pord_str1)
  pord_lbx1.place(x=15,y=220)
  if not podata:
    pord_str1.set('Purchase Order')
  else:
    pord_lbx1.insert(0, podata[44])

  pord_str2 = StringVar() 
  pord_lbx2 = Entry(tentab, width=30,textvariable=pord_str2)
  pord_lbx2.place(x=15,y=240)
  if not podata:
    pord_str2.set('P.Order#')
  else:
    pord_lbx2.insert(0, podata[45])

  pord_str3 = StringVar() 
  pord_lbx3 = Entry(tentab,width=30,textvariable=pord_str3)
  pord_lbx3.place(x=15,y=260)
  if not podata:
    pord_str3.set('P.Order Date')
  else:
    pord_lbx3.insert(0, podata[46])

  pord_str4 = StringVar() 
  pord_lbx4 = Entry(tentab,width=30,
  textvariable=pord_str4)
  pord_lbx4.place(x=15,y=280)
  if not podata:
    pord_str4.set('Due date')
  else:
    pord_lbx4.insert(0, podata[47])

  pord_str5 = StringVar() 
  pord_lbx5 = Entry(tentab,width=30,textvariable=pord_str5)
  pord_lbx5.place(x=15,y=300)
  if not podata:
    pord_str5.set('Vendor')
  else:
    pord_lbx5.insert(0, podata[48])

  pord_str6 = StringVar() 
  pord_lbx6 = Entry(tentab, width=30,textvariable=pord_str6)
  pord_lbx6.place(x=15,y=320)
  if not podata:
    pord_str6.set('Delivery to')
  else:
    pord_lbx6.insert(0, podata[49])

  pord_str7 = StringVar() 
  pord_lbx7 = Entry(tentab, width=30,textvariable=pord_str7)
  pord_lbx7.place(x=15,y=340)
  if not podata:
    pord_str7.set('P.Order total')
  else:
    pord_lbx7.insert(0, podata[50])


  messagelbframe=LabelFrame(tentab,text="Predefined terms and conditions text for purchase orders", height=100, width=980)
  messagelbframe.place(x=248, y=380)

  # txt = scrolledtext.ScrolledText(tentab, undo=True,width=115,height=4)
  # txt.place(x=260,y=405)

  pord_str8 = StringVar() 
  entry2=Entry(tentab, width=155,textvariable=pord_str8)
  entry2.place(x=260, y=400,height=65)
  if not podata:
    pass
  else:
    entry2.insert(0, podata[51])


  def restore_default_pord():
        pord_lbx1.delete(0, 'end')
        pord_lbx1.insert(0, 'Purchase Order')
        pord_lbx2.delete(0, 'end')
        pord_lbx2.insert(0, 'P.Order#')
        pord_lbx3.delete(0, 'end')
        pord_lbx3.insert(0, 'P.Order Date')
        pord_lbx4.delete(0, 'end')
        pord_lbx4.insert(0, 'Due date')
        pord_lbx5.delete(0, 'end')
        pord_lbx5.insert(0, 'Vendor')
        pord_lbx6.delete(0, 'end')
        pord_lbx6.insert(0, 'Delivery to')
        pord_lbx7.delete(0, 'end')
        pord_lbx7.insert(0, 'P.Order total')



  bttermadd1 = Button(tentab,text="Restore defaults",command=restore_default_pord)
  bttermadd1.place(x=45,y=430)

  savebtn = Button(tentab,text="Refresh",width=15)
  savebtn.place(x=1090,y=10)

  frame = Frame(tentab, width=953, height=300)
  frame.pack(expand=True, fill=BOTH)
  frame.place(x=247,y=50)
  canvas=Canvas(frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))
              
  vertibar=Scrollbar(frame, orient=VERTICAL)
  vertibar.pack(side=RIGHT,fill=Y)
  vertibar.config(command=canvas.yview)
          
  canvas.config(width=953,height=300)
  canvas.config(yscrollcommand=vertibar.set)
  canvas.pack(expand=True,side=LEFT,fill=BOTH)
  canvas.create_rectangle(100, 8, 850, 687 , outline='yellow',fill='white')
  canvas.create_text(500, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))
  try:
    pord_image = Image.open("images/"+podata[13])
    pord_resize_image = pord_image.resize((200,100))
    pord_image = ImageTk.PhotoImage(pord_resize_image)

    pord_btlogo = Label(canvas,width=200,height=100,image = pord_image) 
    window_image = canvas.create_window(175, 45, anchor="nw", window=pord_btlogo)
    pord_btlogo.photo = pord_image
  except:
    pass  
  canvas.create_text(202, 160, text=""+pord_str2.get(), fill="black", font=('Helvetica 11'))
  canvas.create_text(215, 180, text=""+pord_str3.get(), fill="black", font=('Helvetica 11'))
  canvas.create_text(200, 200, text=""+pord_str4.get(), fill="black", font=('Helvetica 11'))
  canvas.create_text(191, 220, text="Terms", fill="black", font=('Helvetica 11'))
  canvas.create_text(205, 240, text="Order ref.#", fill="black", font=('Helvetica 11'))
  canvas.create_text(350, 160, text="P.ORD/2022", fill="black", font=('Helvetica 11'))
  canvas.create_text(350, 180, text="05-05-2022", fill="black", font=('Helvetica 11'))
  canvas.create_text(350, 200, text="20-05-2022", fill="black", font=('Helvetica 11'))
  canvas.create_text(340, 220, text="NET 15", fill="black", font=('Helvetica 11'))

  canvas.create_text(720, 60, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
  canvas.create_text(700, 175, text=""+caddent.get('1.0', 'end-1c'), fill="black", font=('Helvetica 10'), width=125)
  canvas.create_text(695, 180, text=" "+comsalestax.get(), fill="black", font=('Helvetica 10'))
  canvas.create_text(700, 205, text=" "+pord_str1.get(), fill="black", font=('Helvetica 14 bold'))
  canvas.create_text(706, 225, text="TAX EXEMPTED", fill="black", font=('Helvetica 10'))
          
  canvas.create_text(210, 260, text=""+pord_str5.get(), fill="black", font=('Helvetica 10 underline'))
  canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
  canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
  canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
  canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
  canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
  canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
  canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
  canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
  canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))
      
  s = ttk.Style()
  s.configure('mystyle_1.Treeview.Heading', background=''+pwin_menu.get(),State='DISABLE')

  tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_1.Treeview')

  tree.column("# 1", anchor=E, stretch=NO, width=100)
  tree.heading("# 1", text="ID/SKU")
  tree.column("# 2", anchor=E, stretch=NO, width=350)
  tree.heading("# 2", text="Product/Service - Description")
  tree.column("# 3", anchor=E, stretch=NO, width=80)
  tree.heading("# 3", text="Quantity")
  tree.column("# 4", anchor=E, stretch=NO, width=90)
  tree.heading("# 4", text="Unit Price")
  tree.column("# 5", anchor=E, stretch=NO, width=80)
  tree.heading("# 5", text="Price")
          
  window = canvas.create_window(120, 340, anchor="nw", window=tree)

  canvas.create_line(120, 390, 820, 390 )
  canvas.create_line(120, 340, 120, 365 )
  canvas.create_line(120, 365, 120, 390 )
  canvas.create_line(820, 340, 820, 540 )
  canvas.create_line(740, 340, 740, 540 )
  canvas.create_line(570, 340, 570, 540 )
  canvas.create_line(570, 415, 820, 415 )
  canvas.create_line(570, 440, 820, 440 )
  canvas.create_line(570, 465, 820, 465 )
  canvas.create_line(570, 490, 820, 490 )
  canvas.create_line(570, 515, 820, 515 )
  canvas.create_line(650, 340, 650, 390 )
  canvas.create_line(220, 340, 220, 390 )
  canvas.create_line(570, 540, 820, 540 )

  canvas.create_text(165, 372, text="PROD-0001", fill="black", font=('Helvetica 10'))
  canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
  canvas.create_text(610, 372, text="1", fill="black", font=('Helvetica 10'))
    
  if comcursignpla.get() == "before amount":
    canvas.create_text(704, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

  elif comcursignpla.get() == "after amount":
    canvas.create_text(704, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))

  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(704, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(704, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))

  else:
    pass
        # canvas.create_text(704, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  if comcursignpla.get() == "before amount":
    canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

  elif comcursignpla.get() == "after amount":
    canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))

  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(784, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass
        # canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

  canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))
  if comcursignpla.get() == "before amount":
    canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))

  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(784, 404, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass
        # canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

  canvas.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))

  if comcursignpla.get() == "before amount":
    canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(786, 428, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass
        # canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

  canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))
        
  if comcursignpla.get() == "before amount":
    canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(786, 454, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass

        # canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

  if comcursignpla.get() == "before amount":
    canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10 bold'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(784, 479, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10 bold'))
  else:
    pass

        # canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
  canvas.create_text(650, 479, text=""+pord_str6.get(), fill="black", font=('Helvetica 10 bold'))
  if comcursignpla.get() == "before amount":
    canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(784, 502, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass

        # canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  canvas.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))
        
  if comcursignpla.get() == "before amount":
    canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(784, 526, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass
        # canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  canvas.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

  canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
  canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
  canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
  canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))
          
  canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
  canvas.create_line(150, 620, 795, 620)
  canvas.create_text(280, 640, text= ""+pord_str8.get(), fill="black", font=('Helvetica 10')) 

  canvas.create_text(280, 655, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
  canvas.create_text(720, 655, text="Page 1 of 1", fill="black", font=('Helvetica 10'))

    


root.mainloop()

