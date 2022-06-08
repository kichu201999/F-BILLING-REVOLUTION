memaiframe=Text(emailmessage_Frame,font=('arial 17'),undo=True,width=130,height=400)
  memaiframe.pack(padx=0,pady=28,expand=False)


  scrollbar1 = Scrollbar(eighttab,orient=VERTICAL)
  scrollbar2= Scrollbar(memaiframe,orient=HORIZONTAL,command=memaiframe.xview,width=10)
  scrollbar2.pack(fill=X,expand=True,side=BOTTOM,padx=490,pady=500)
  memaiframe.config(xscrollcommand=scrollbar2.set)
  
  scrollbar1.config(command=memaiframe.yview)
  scrollbar1.place(x =1040, y=120, height=396)
  scrollbar2.config(command=memaiframe.xview)




  ###########################

  meframe = StringVar()
  memaiframe=ScrolledText(emailmessage_Frame, width=130, bg="white",undo=True,height=400)
  if not emdata:
    pass
  else:
    memaiframe.insert('1.0', emdata[53])
  memaiframe.place(y=28,x=9)

  scrollbar = Scrollbar(eighttab)
  scrollbar.place(x=1048, y=120, height=396)