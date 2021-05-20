from tkinter import *
from calculator_guitask import*
class login:
    def __init__(self,root):
        self.root=root
        root.geometry=('400x400')
        root.maxsize(400,400)
        root.minsize(400,400)
        root.configure(bg='grey')
        root.title("login")
        loglabel = Label(root, width=30, justify=CENTER, text='Log In!', font=('Times New Roman', 15, 'bold',), bg='grey')

        f1= Frame(root, height=20,width=20,bg='grey')
        username_label= Label(f1, width=10, justify=CENTER, text='User Name:', font=('Times New Roman', 15, 'bold'), bg='grey')
        self.username_entry= Entry(f1, width=20, justify=CENTER,  font=('Times New Roman', 15, 'bold'))

        f2 = Frame(root, height=20,width=20, bg='grey')
        password_label = Label(f2, width=10, justify=CENTER, text='Password:', font=('Times New Roman', 15, 'bold'),bg='grey')
        self.password_entry = Entry(f2, width=20, justify=CENTER, font=('Times New Roman', 15, 'bold'))

        f3 = Frame(root, height=150, width=50, bg='grey')
        login_button= Button(f3,width=10, justify=CENTER, text= 'Log In!',font=('Times New Roman', 15, 'bold'),bg='orange',command= lambda:self.log(self.username_entry.get(),self.password_entry.get()))
        signup_button = Button(f3, width=10, justify=CENTER, text='Sign Up!', font=('Times New Roman', 15, 'bold'), bg='orange')


        loglabel.pack(side= TOP,pady= 10, padx=100)
        f1.pack(side=TOP,fill= BOTH, expand=1)
        username_label.pack(side= LEFT,pady=5,padx=10)
        self.username_entry.pack(side= LEFT,pady=5,padx= 10)

        f2.pack(side=TOP, fill=BOTH, expand=1)
        password_label.pack(side= LEFT,pady=5,padx=10)
        self.password_entry.pack(side= LEFT,pady=5,padx= 10)

        f3.pack(side=TOP, fill=BOTH, expand=1)
        login_button.pack(side=LEFT, pady=20, padx=30)
        signup_button.pack(side=LEFT, pady=20, padx=30)

    def erase(self):
        self.username_entry.delete(0,END)
        self.password_entry.delete(0,END)

    def log(self,name,password):
        if name == 'Moattar':
            self.erase()
            if password == '1234':
               self.erase()
               root.destroy()
               calgui()
            else:
                print("Wrong Password! Try Again.")
        else:
            print("Wrong Username! Try Again.")


root= Tk()
obj= login(root)
mainloop()