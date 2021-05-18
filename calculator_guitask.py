from tkinter import *
root= Tk()
root.geometry('400x400')
root.title("Calculator")
root.configure(bg="grey")
#************frame***************#
frame1= Frame(root, height= 40, bg='grey')
#***********ENTRYBOX*************#
num1= Entry(frame1, width=12, justify= CENTER, font=("Times New Roman", 16), borderwidth= 5)
num2= Entry(frame1, width=12, justify= CENTER, font=("Times New Roman", 16), borderwidth= 5)

#***********Buttons*************#
frame2= Frame(root, height=40, bg= 'grey')
f2top= Frame(frame2,height= 50, bg='grey')
addbutton = Button(f2top,width= 8, justify= CENTER,text= '+',font=("Times New Roman", 16),bg= 'orange')
subtractbutton = Button(f2top,width= 8, justify= CENTER,text= '-',font=("Times New Roman", 16),bg= 'orange')



f2center= Frame(frame2,height= 50, bg='grey')
multiplybutton = Button(f2center,width= 8, justify= CENTER,text= '*',font=("Times New Roman", 16),bg= 'orange')
divisionbutton = Button(f2center,width= 8, justify= CENTER,text= '/',font=("Times New Roman", 16),bg= 'orange')



f2bottom= Frame(frame2,height= 50, bg= 'grey')
rembutton = Button(f2bottom,width= 8, justify= CENTER,text= 'Remainder',font=("Times New Roman", 16),bg= 'orange')



frame1.pack(side=TOP, fill=BOTH, expand=1)
num1.pack(side= LEFT, padx=30, pady= 20)
num2.pack(side= LEFT, padx=30, pady= 20)

f2top.pack(side=TOP,fill= BOTH,expand= 1)
addbutton.pack(side= LEFT, padx= 30, pady=20)
subtractbutton.pack(side= LEFT, padx= 30, pady=20)


f2center.pack(side=TOP,fill= BOTH, expand= 1)
multiplybutton.pack(side= LEFT, padx= 30, pady=10)
divisionbutton.pack(side= LEFT, padx= 30, pady=10)

f2bottom.pack(side= TOP, fill= BOTH, expand=1)
rembutton.pack(side= TOP, padx= 30, pady=10)

frame2.pack(side= TOP, fill= BOTH, expand=1)
mainloop()