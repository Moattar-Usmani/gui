from tkinter import *
def calgui():
    class calculator:
        def __init__(self,root):
            self.root= root
            root.geometry('500x500')
            root.maxsize(500, 500)
            root.minsize(500, 500)
            root.title("Calculator")
            root.configure(bg="grey")
            wellabel = Label(root, width=30, justify=CENTER, text='Welcome to Calculator!', font=('Times New Roman', 15, 'bold',),bg='grey')
#************frame***************#
            frame1= Frame(root, height= 40, bg='grey')
#***********ENTRYBOX*************#
            self.num1= Entry(frame1, width=12, justify= CENTER, font=("Times New Roman", 16), borderwidth= 5)
            self.num2= Entry(frame1, width=12, justify= CENTER, font=("Times New Roman", 16), borderwidth= 5)

#***********Buttons*************#
            frame2= Frame(root, height=40, bg= 'grey')
            f2top= Frame(frame2,height= 50, bg='grey')
            addbutton = Button(f2top,width= 8, justify= CENTER,text= '+',font=("Times New Roman", 16),bg= 'orange',activebackground='red',command = lambda : [self.result(int(1)),self.earse()])
            subtractbutton = Button(f2top,width= 8, justify= CENTER,text= '-',font=("Times New Roman", 16),bg= 'orange',activebackground='red', command = lambda : [self.result(int(2)),self.earse()])



            f2center= Frame(frame2,height= 50, bg='grey')
            multiplybutton = Button(f2center,width= 8, justify= CENTER,text= '*',font=("Times New Roman", 16),bg= 'orange',activebackground='red', command = lambda : [self.result(int(3)),self.earse()])
            divisionbutton = Button(f2center,width= 8, justify= CENTER,text= '/',font=("Times New Roman", 16),bg= 'orange',activebackground='red', command = lambda : [self.result(int(4)),self.earse()])



            f2bottom= Frame(frame2,height= 50, bg= 'grey')
            rembutton = Button(f2bottom,width= 8, justify= CENTER,text= 'Remainder',font=("Times New Roman", 16),bg= 'orange',activebackground='red', command = lambda : [self.result(int(5)),self.earse()])


            self.frame3 = Frame(root, height=50, bg="grey")
            self.resultlabel = Label(self.frame3,width= 20, justify=CENTER,text= 'answer',font=("Times New Roman", 16),bg= 'white')

            wellabel.pack(side=TOP, pady=10, padx=100)
            frame1.pack(side=TOP, fill=BOTH, expand=1)
            self.num1.pack(side= LEFT, padx=30, pady= 20)
            self.num2.pack(side= RIGHT, padx=30, pady= 20)

            f2top.pack(side=TOP,fill= BOTH,expand= 1)
            addbutton.pack(side= LEFT, padx= 30, pady=30)
            subtractbutton.pack(side= RIGHT, padx= 30, pady=30)


            f2center.pack(side=TOP,fill= BOTH, expand= 1)
            multiplybutton.pack(side= LEFT, padx= 30, pady=10)
            divisionbutton.pack(side= RIGHT, padx= 30, pady=30)

            f2bottom.pack(side= TOP, fill= BOTH, expand=1)
            rembutton.pack(side= TOP, padx= 30, pady=30)

            frame2.pack(side= TOP, fill= BOTH, expand=1)

            self.frame3.pack(side=TOP, fill=BOTH)
            self.resultlabel.pack(side=TOP, pady=20, padx=10)


        def add(self,num1,num2):
            result= int(num1)+int(num2)
            self.resultlabel = Label(self.frame3, width=15, height=2, font=("arial", 12, "bold"), justify=CENTER, text=result)
            self.resultlabel.pack(side=TOP, pady=20, padx=10)

        def sub(self,num1,num2):
            result= int(num1)-int(num2)
            self.resultlabel = Label(self.frame3, width=15, height=2, font=("arial", 12, "bold"), justify=CENTER, text=result)
            self.resultlabel.pack(side=LEFT, pady=20, padx=10)

        def multiply(self,num1,num2):
            result= int(num1)*int(num2)
            self.resultlabel = Label(self.frame3, width=15, height=2, font=("arial", 12, "bold"), justify=CENTER, text=result)
            self.resultlabel.pack(side=LEFT, pady=20, padx=10)

        def divide(self,num1,num2):
            result= int(num1)/int(num2)
            self.resultlabel = Label(self.frame3, width=15, height=2, font=("arial", 12, "bold"), justify=CENTER, text=result)
            self.resultlabel.pack(side=LEFT, pady=20, padx=10)

        def rem(self,num1,num2):
            result= int(num1)%int(num2)
            self.resultlabel = Label(self.frame3, width=15, height=2, font=("arial", 12, "bold"), justify=CENTER, text=result)
            self.resultlabel.pack(side=LEFT, pady=20, padx=10)

        def result(self, condition):
            self.con = condition
            if self.con == 1:
                self.vanish()
                return self.add(self.num1.get(), self.num2.get())
            elif self.con == 2:
                self.vanish()
                return self.sub(self.num1.get(), self.num2.get())
            elif self.con == 3:
                self.vanish()
                return self.multiply(self.num1.get(), self.num2.get())
            elif self.con == 4:
                self.vanish()
                return self.divide(self.num1.get(), self.num2.get())
            elif self.con == 5:
                self.vanish()
                return self.rem(self.num1.get(), self.num2.get())
            else:
                pass

        def earse(self):
            self.num1.delete(0, END)
            self.num2.delete(0, END)

        def vanish(self):
            self.resultlabel.destroy()

    root = Tk()
    calculator(root)
    mainloop()

