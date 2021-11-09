from tkinter import *
import tkinter.messagebox
import database


class Ticket:

    def __init__(self, root):

        d = database.Backend()
        self.root=root
        self.root.title('Movie Ticket Booking System')
        self.root.geometry('1350x750')
        self.root.config(bg="black")


        Ticket_no = StringVar()
        Movie_name = StringVar()
        Price = StringVar()
        Seat_no = StringVar()
        Show_date = StringVar()

        def clcdata():
            self.txtTicket_no.delete(0,END)
            self.txtMovie_name.delete(0,END)
            self.txtPrice.delete(0,END)
            self.txtSeat_no.delete(0,END)
            self.txtShow_date.delete(0,END)

        def disData():
            MovieList.delete(0,END)
            for row in d.ViewMovieData():
                MovieList.insert(END,row,str(''))

        def addData():
            if (len(Ticket_no.get())!=0):
                d.addTickets(Ticket_no.get(),Movie_name.get(),Price.get(),Seat_no.get(),Show_date.get())
                #MovieList.delete(0,END)
                #MovieList.insert(Custom_id.get(),Movie_Name.get(),Release_Date.get(),Director.get(),Cast.get(),Budget.get(),Duration.get(),Rating.get())
                #disData()
            else:
                tkinter.messagebox.askyesno('Enter a Ticket Number')

        #Frames
        MainFrame = Frame(self.root,bg='black')
        MainFrame.grid()

        HeadFrame = Frame(MainFrame,bd=1,bg='black',relief=RIDGE,padx=50,pady=10)
        HeadFrame.pack(side=TOP)

        self.TFrame=Label(HeadFrame, font=('Arial', 50, 'bold'), text="MOVIE TICKET BOOKING SYSTEM", bg="black", fg="red")
        self.TFrame.grid() 

        BottomFrame=Frame(MainFrame, bd=2, width=1350, height=70, padx=18, pady=10, bg="black", relief=RIDGE)
        BottomFrame.pack(side=BOTTOM)

        BodyFrame=Frame(MainFrame, bd=2, width=1300, height=500, padx=20, pady=20, bg="black", relief=RIDGE)
        BodyFrame.pack(side=BOTTOM)

        LeftBody=LabelFrame(BodyFrame, bd=2, width=700, height=480, padx=20, bg="black", relief=RIDGE, font=('Arial', 15, 'bold'),text='Ticket info:\n',fg='white')
        LeftBody.pack(side=LEFT)

        RightBody=LabelFrame(BodyFrame, bd=2, width=350, height=480, padx=31, pady=3, bg="black", relief=RIDGE, font=('Arial', 15, 'bold'),text='Movie Details:\n',fg='white')
        RightBody.pack(side=RIGHT)

        #Labels

        self.lblTicket_no=Label(LeftBody, font=('Arial', 18, 'bold'), text="Ticket No.:", padx=2, pady=2, bg="black", fg="orange")
        self.lblTicket_no.grid(row=0, column=0, sticky=W)
        self.txtTicket_no=Entry(LeftBody, font=('Arial', 18, 'bold'), textvariable=Ticket_no, width=39, bg="black", fg="white")
        self.txtTicket_no.grid(row=0, column=1)

        self.lblMovie_name=Label(LeftBody, font=('Arial', 18, 'bold'), text="Movie Name:", padx=2, pady=2, bg="black", fg="orange")
        self.lblMovie_name.grid(row=1, column=0, sticky=W)
        self.txtMovie_name=Entry(LeftBody, font=('Arial', 18, 'bold'), textvariable=Movie_name, width=39, bg="black", fg="white")
        self.txtMovie_name.grid(row=1, column=1)

        self.lblPrice=Label(LeftBody, font=('Arial', 18, 'bold'), text="Price:", padx=2, pady=2, bg="black", fg="orange")
        self.lblPrice.grid(row=2, column=0, sticky=W)
        self.txtPrice=Entry(LeftBody, font=('Arial', 18, 'bold'), textvariable=Price, width=39, bg="black", fg="white")
        self.txtPrice.grid(row=2, column=1)

        self.lblSeat_no=Label(LeftBody, font=('Arial', 18, 'bold'), text="Seat No.:", padx=2, pady=2, bg="black", fg="orange")
        self.lblSeat_no.grid(row=3, column=0, sticky=W)
        self.txtSeat_no=Entry(LeftBody, font=('Arial', 18, 'bold'), textvariable=Seat_no, width=39, bg="black", fg="white")
        self.txtSeat_no.grid(row=3, column=1)

        self.lblShow_date=Label(LeftBody, font=('Arial', 18, 'bold'), text="Show Date.:", padx=2, pady=2, bg="black", fg="orange")
        self.lblShow_date.grid(row=4, column=0, sticky=W)
        self.txtShow_date=Entry(LeftBody, font=('Arial', 18, 'bold'), textvariable=Show_date, width=39, bg="black", fg="white")
        self.txtShow_date.grid(row=4, column=1)

        #Scroll bar
        scroll=Scrollbar(RightBody)
        scroll.grid(row=0, column=1, sticky='ns')

        MovieList=Listbox(RightBody, width=41, height=16, font=('Arial', 12, 'bold'), bg="black", fg="white", yscrollcommand=scroll.set)
        #MovieList.bind('<<ListboxSelect>>', movierec)
        MovieList.grid(row=0, column=0, padx=8)
        scroll.config(command=MovieList.yview)
        
        #Buttons      
          
        self.btnadd=Button(BottomFrame, text="Add", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="orange",command=addData)
        self.btnadd.grid(row=0, column=0)

        self.btnclear=Button(BottomFrame, text="Clear", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="orange",command=clcdata)
        self.btnclear.grid(row=0, column=1)   #column 2

        self.btndisp=Button(BottomFrame, text="Display", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="orange",command=disData)
        self.btndisp.grid(row=0, column=2)

if __name__=='__main__':
	root=Tk()
	database = Ticket(root)
	root.mainloop()