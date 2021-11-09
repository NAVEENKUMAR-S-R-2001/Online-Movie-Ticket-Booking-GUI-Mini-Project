from tkinter import *
import tkinter.messagebox
import database

class Bookings():
    
    def __init__(self, root):
        d = database.Backend()
        #d.conn
        

        self.root=root
        self.root.title('Movie Ticket Booking System')
        self.root.geometry('1350x750')
        self.root.config(bg="black")


        def disData():
            bookList.delete(0,END)
            for row in d.ViewBookingRec():
                bookList.insert(END,row,str(''))


        #Fraames
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

        LeftBody=LabelFrame(BodyFrame, bd=2, width=700, height=480, padx=20, bg="black", relief=RIDGE, font=('Arial', 15, 'bold'),text='Bookings:\n',fg='white')
        LeftBody.pack(side=LEFT)




        self.btndisp=Button(BottomFrame, text="Display", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="orange",command=disData)
        self.btndisp.grid(row=0, column=0)


        #Scroll bar
        scroll=Scrollbar(LeftBody)
        scroll.grid(row=0, column=1, sticky='ns')

        bookList=Listbox(LeftBody, width=41, height=16, font=('Arial', 12, 'bold'), bg="black", fg="white", yscrollcommand=scroll.set)
        #MovieList.bind('<<ListboxSelect>>', movierec)
        bookList.grid(row=0, column=0, padx=8)
        scroll.config(command=bookList.yview)



if __name__=='__main__':
	root=Tk()
	application = Bookings(root)
	root.mainloop()