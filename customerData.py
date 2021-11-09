from tkinter import *
import tkinter.messagebox
import database
import tickets

class Custm:

    def __init__(self, root):
        d = database.Backend()
        self.root=root
        self.root.title('Movie Ticket Booking System')
        self.root.geometry('1350x750')
        self.root.config(bg="black")


        def clcdata():
            self.txtCustom_id.delete(0,END)
            self.txtCustom_name.delete(0,END)
            self.txtCustom_email.delete(0,END)
            self.txtCustom_phno.delete(0,END)

        def addData():
            if (len(Custom_id.get())!=0):
                d.addCustomerData(Custom_id.get(),Custom_name.get(),Custom_email.get(),Custom_phno.get())
                custList.delete(0,END)
                custList.insert(Custom_id.get(),Custom_name.get(),Custom_email.get(),Custom_phno.get())
                disData()
            else:
                tkinter.messagebox.askyesno('Enter a Customer ID')
                  

        def disData():
            custList.delete(0,END)
            for row in d.ViewCustomerData():
                custList.insert(END,row,str(''))

        def delData():
            if (len(Custom_id.get())!=0):
                d.DeleteCustomRec(Custom_id.get())
                clcdata()
                disData()
           

        

        Custom_id = StringVar()
        Custom_name = StringVar()
        Custom_email = StringVar()
        Custom_phno = StringVar()

        MainFrame = Frame(self.root,bg='black')
        MainFrame.grid()


        HeadFrame = Frame(MainFrame,bd=1,bg='black',relief=RIDGE,padx=50,pady=10)
        HeadFrame.pack(side=TOP)

        self.TFrame=Label(HeadFrame, font=('Arial', 50, 'bold'), text="\u2680 MOVIE TICKET BOOKING SYSTEM\u2680", bg="black", fg="red")
        self.TFrame.grid()

        BottomFrame=Frame(MainFrame, bd=2, width=1350, height=70, padx=18, pady=10, bg="black", relief=RIDGE)
        BottomFrame.pack(side=BOTTOM)

        BodyFrame=Frame(MainFrame, bd=2, width=1300, height=500, padx=20, pady=20, bg="black", relief=RIDGE)
        BodyFrame.pack(side=BOTTOM)

        LeftBody=LabelFrame(BodyFrame, bd=2, width=1000, height=480, padx=20, bg="black", relief=RIDGE, font=('Arial', 15, 'bold'),text='Customer info:\n',fg='white')
        LeftBody.pack()

        RightBody=LabelFrame(BodyFrame, bd=2, width=350, height=480, padx=31, pady=3, bg="black", relief=RIDGE, font=('Arial', 15, 'bold'),text='Customer Details:\n',fg='white')
        RightBody.pack(side=RIGHT)


        self.lblCustom_id=Label(LeftBody, font=('Arial', 18, 'bold'), text="Customer ID:", padx=2, pady=2, bg="black", fg="orange")
        self.lblCustom_id.grid(row=0, column=0, sticky=W)
        self.txtCustom_id=Entry(LeftBody, font=('Arial', 18, 'bold'), textvariable=Custom_id, width=39, bg="black", fg="white")
        self.txtCustom_id.grid(row=0, column=1)

        self.lblCustom_name=Label(LeftBody, font=('Arial', 18, 'bold'), text="Customer Name:", padx=2, pady=2, bg="black", fg="orange")
        self.lblCustom_name.grid(row=1, column=0, sticky=W) 
        self.txtCustom_name=Entry(LeftBody, font=('Arial', 18, 'bold'), textvariable=Custom_name, width=39, bg="black", fg="white")
        self.txtCustom_name.grid(row=1, column=1)

        self.lblCustom_email=Label(LeftBody, font=('Arial', 18, 'bold'), text="Customer Email:", padx=2, pady=2, bg="black", fg="orange")
        self.lblCustom_email.grid(row=2, column=0, sticky=W) 
        self.txtCustom_email=Entry(LeftBody, font=('Arial', 18, 'bold'), textvariable=Custom_email, width=39, bg="black", fg="white")
        self.txtCustom_email.grid(row=2, column=1)

        self.lblCustom_phno=Label(LeftBody, font=('Arial', 18, 'bold'), text="Customer Ph no:", padx=2, pady=2, bg="black", fg="orange")
        self.lblCustom_phno.grid(row=3, column=0, sticky=W) 
        self.txtCustom_phno=Entry(LeftBody, font=('Arial', 18, 'bold'), textvariable=Custom_phno, width=39, bg="black", fg="white")
        self.txtCustom_phno.grid(row=3, column=1)


        #Scroll bar
        scroll=Scrollbar(RightBody)
        scroll.grid(row=0, column=1, sticky='ns')

        custList=Listbox(RightBody, width=41, height=16, font=('Arial', 12, 'bold'), bg="black", fg="white", yscrollcommand=scroll.set)
        #MovieList.bind('<<ListboxSelect>>', movierec)
        custList.grid(row=0, column=0, padx=8)
        scroll.config(command=custList.yview)



        self.btnadd=Button(BottomFrame, text="Add", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="orange",command=addData)
        self.btnadd.grid(row=0, column=0)

        self.btnclear=Button(BottomFrame, text="Clear", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="orange",command=clcdata)
        self.btnclear.grid(row=0, column=1)

        self.btndel=Button(BottomFrame, text="Delete", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="orange",command=delData)
        self.btndel.grid(row=0, column=2)

        self.btndisp=Button(BottomFrame, text="Display", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="orange",command=disData)
        self.btndisp.grid(row=0, column=3)

        self.btnnext=Button(BottomFrame, text="Next", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="orange",command=lambda:self.openTicketsInfo()) # if wanted (Mainframe) as args
        self.btnnext.grid(row=0, column=4)

    def openTicketsInfo(self):
        
        #frame.grid_forget()
        top = Toplevel()
        tickets.Ticket(top)



if __name__=='__main__':
	root=Tk()
	database = Custm(root)
	root.mainloop()