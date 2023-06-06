from tkinter import *
import mysql.connector
import tkinter.messagebox as msg

class ATM:
    def __init__(self):
        root=Tk()
        root.title("ATM Window")
        root.config(bg="Blue")
        root.geometry("500x500")
        Registration=Button(root,text="REGISTER",fg="White",bg="Blue",font=("Bold",20),command=self.window1)
        Registration.place(x=300,y=300)
        withdraw=Button(root,text="WITHDRAW",fg="White",bg="Blue",font=("Bold",20),command=self.window2)
        withdraw.place(x=300,y=380)

        my_menu = Menu(root)
        root.config(menu=my_menu)

        def our_command():
            lable = Label(root, text='Menu').pack()

        file_menu = Menu(my_menu)
        my_menu.add_cascade(label='about', menu=file_menu)
        file_menu.add_command(label='New', command=our_command)
        file_menu.add_separator()
        file_menu.add_command(label='exit', command=root.quit)
        root.mainloop()


    def window1(self):
        root=Tk()
        root.title("ATM Window")
        root.config(bg="Blue")
        root.geometry("500x500")
        name=Label(root,text="Name:",bg="Blue",fg="White",font=("Bold",20))
        name.place(x=300,y=300)
        self.name_entry=Entry(root,font=(20))
        self.name_entry.place(x=420,y=300)
        mobile_No=Label(root,text="Mobile:",bg="Blue",fg="White",font=("Bold",20))
        mobile_No.place(x=300,y=350)
        self.mobile_no_entry=Entry(root,font=(20))
        self.mobile_no_entry.place(x=420,y=350)
        Account_no=Label(root,text="Account:",bg="Blue",fg="White",font=("Bold",20))
        Account_no.place(x=300,y=400)
        self.account_no_entry=Entry(root,font=(20))
        self.account_no_entry.place(x=420,y=400)
        Amount=Label(root,text="Amount:",bg="Blue",fg="White",font=("Bold",20))
        Amount.place(x=300,y=450)
        self.amount_entry=Entry(root,font=(20))
        self.amount_entry.place(x=420,y=450)
        Submit=Button(root,text="Submit",fg="White",bg="Blue",font=("Bold",25),command=self.submit)
        Submit.place(x=400,y=500)
        root.mainloop()
    def submit(self):
        a=self.name_entry.get()
        b=self.mobile_no_entry.get()
        c=self.account_no_entry.get()
        d=self.amount_entry.get()
        mq=mysql.connector.connect(host="localhost",user="root",passwd="root",database="bank")
        cursor=mq.cursor()

        cursor.execute("insert into atm values(%s,%s,%s,%s)",(a,b,c,d))
        msg.showinfo("Details","Amount Added")
        mq.commit()

    def window2(self):
        root=Tk()
        root.title("ATM Window")
        root.config(bg="Blue")
        root.geometry("500x500")
        account_no=Label(root,text="AC:",bg="Blue",fg="White",font=("Bold",20))
        account_no.place(x=300,y=300)
        self.account_no_entry=Entry(root,font=(20))
        self.account_no_entry.place(x=400,y=305)
        amount=Label(root,text="Amount:",fg="White",bg="Blue",font=("Bold",20))
        amount.place(x=300,y=350)
        self.amount_entry=Entry(root,font=(20))
        self.amount_entry.place(x=400,y=355)
        wd=Button(root,text="WITHDRAW",fg="White",bg="Grey",font=("Bold",25),command=self.wd)
        wd.place(x=400,y=400)
        root.mainloop()
    def wd(self):
        x=self.account_no_entry.get()
        y=self.amount_entry.get()
        mq = mysql.connector.connect(host="localhost", user="root", passwd="root", database="bank")
        cursor = mq.cursor()
        if x=="" and str(y)=="":
            msg.showwarning("Warning","Fill all Entry")
        else:
            cursor.execute("select Balance from atm where Account=%s",(x,))
            q=0
            for i in cursor:
                q=int(i[0])
            cursor.execute("update atm set Balance=%s where Account=%s",(q-int(y),x))
            cursor.execute("insert into histry values(%s,%s)",(x,y))
            msg.showinfo("Result","Amount Debited")

        mq.commit()
a=ATM()

#Naren.git jsdbcjs

