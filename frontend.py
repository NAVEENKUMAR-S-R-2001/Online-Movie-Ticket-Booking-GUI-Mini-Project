from tkinter import *
import tkinter.messagebox
import database
import first
import booking


class Movie:
    
    

    def __init__(self, root):
        d = database.Backend()
        #d.conn
        

        self.root=root
        self.root.title('Movie Ticket Booking System')
        self.root.geometry('1350x750')
        self.root.config(bg="black")

        Movie_Name=StringVar()
        Movie_ID=StringVar()
        Release_Date=StringVar()
        Director=StringVar()
        Cast=StringVar()
        Budget=StringVar()
        Duration=StringVar()
        Rating=StringVar()


        def clcdata():
            self.txtMovie_ID.delete(0,END)
            self.txtMovie_Name.delete(0,END)
            self.txtRelease_Date.delete(0,END)
            self.txtDirector.delete(0,END)
            self.txtCast.delete(0,END)
            self.txtBudget.delete(0,END)
            self.txtRating.delete(0,END)
            self.txtDuration.delete(0,END)

        def addData():
            if (len(Movie_ID.get())!=0):
                d.addMovie(Movie_ID.get(),Movie_Name.get(),Release_Date.get(),Director.get(),Cast.get(),Budget.get(),Duration.get(),Rating.get())
                MovieList.delete(0,END)
                MovieList.insert(Movie_ID.get(),Movie_Name.get(),Release_Date.get(),Director.get(),Cast.get(),Budget.get(),Duration.get(),Rating.get())
                disData()
            else:
                tkinter.messagebox.askyesno('Enter a Movie ID')
        
        def disData():
            MovieList.delete(0,END)
            for row in d.ViewMovieData():
                MovieList.insert(END,row,str(''))

        def delData():
            if (len(Movie_ID.get())!=0):
                d.DeleteMovieRec(sd[0])
                clcdata()
                disData()

        def movieRec(event):
            global sd
            searchmovie=MovieList.curselection()[0]
            sd=MovieList.get(searchmovie)
            self.txtMovie_ID.delete(0,END)
            self.txtMovie_ID.insert(END,sd[0])
            self.txtMovie_Name.delete(0,END)
            self.txtMovie_Name.insert(END,sd[1])
            self.txtRelease_Date.delete(0,END)
            self.txtRelease_Date.insert(END,sd[2])
            self.txtDirector.delete(0,END)
            self.txtDirector.insert(END,sd[3])
            self.txtCast.delete(0,END)
            self.txtCast.insert(END,sd[4])
            self.txtBudget.delete(0,END)
            self.txtBudget.insert(END,sd[5])
            self.txtDuration.delete(0,END)
            self.txtDuration.insert(END,sd[6])
            self.txtRating.delete(0,END)
            self.txtRating.insert(END,sd[7])
            

            

        #Fraames
        MainFrame = Frame(self.root,bg='black')
        MainFrame.grid()
        

        HeadFrame = Frame(MainFrame,bd=1,bg='black',relief=RIDGE,padx=50,pady=10)
        HeadFrame.pack(side=TOP)

        self.TFrame=Label(HeadFrame, font=('Arial', 50, 'bold'), text="\u2680MOVIE TICKET BOOKING SYSTEM\u2680", bg="black", fg="red")
        self.TFrame.grid() 

        BottomFrame=Frame(MainFrame, bd=2, width=1350, height=70, padx=18, pady=10, bg="black", relief=RIDGE)
        BottomFrame.pack(side=BOTTOM)

        BodyFrame=Frame(MainFrame, bd=2, width=1300, height=500, padx=20, pady=20, bg="black", relief=RIDGE)
        BodyFrame.pack(side=BOTTOM)

        LeftBody=LabelFrame(BodyFrame, bd=2, width=700, height=480, padx=20, bg="black", relief=RIDGE, font=('Arial', 15, 'bold'),text='Movie info:\n',fg='white')
        LeftBody.pack(side=LEFT)

        RightBody=LabelFrame(BodyFrame, bd=2, width=350, height=480, padx=31, pady=3, bg="black", relief=RIDGE, font=('Arial', 15, 'bold'),text='Movie Details:\n',fg='white')
        RightBody.pack(side=RIGHT)

        #labels
        self.lblMovie_ID=Label(LeftBody, font=('Arial', 18, 'bold'), text="Movie ID:", padx=2, pady=2, bg="black", fg="orange")
        self.lblMovie_ID.grid(row=0, column=0, sticky=W)
        self.txtMovie_ID=Entry(LeftBody, font=('Arial', 18, 'bold'), textvariable=Movie_ID, width=39, bg="black", fg="white")
        self.txtMovie_ID.grid(row=0, column=1)

        self.lblMovie_Name=Label(LeftBody, font=('Arial', 18, 'bold'), text="Movie Name:", padx=2, pady=2, bg="black", fg="orange")
        self.lblMovie_Name.grid(row=1, column=0, sticky=W) 
        self.txtMovie_Name=Entry(LeftBody, font=('Arial', 18, 'bold'), textvariable=Movie_Name, width=39, bg="black", fg="white")
        self.txtMovie_Name.grid(row=1, column=1)

        self.lblRelease_Date=Label(LeftBody, font=('Arial', 18, 'bold'), text="Release Date:", padx=2, pady=2, bg="black", fg="orange")
        self.lblRelease_Date.grid(row=2, column=0, sticky=W) 
        self.txtRelease_Date=Entry(LeftBody, font=('Arial', 18, 'bold'), textvariable=Release_Date, width=39, bg="black", fg="white")
        self.txtRelease_Date.grid(row=2, column=1)

        self.lblDirector=Label(LeftBody, font=('Arial', 18, 'bold'), text="Director:", padx=2, pady=2, bg="black", fg="orange")
        self.lblDirector.grid(row=3, column=0, sticky=W) 
        self.txtDirector=Entry(LeftBody, font=('Arial', 18, 'bold'), textvariable=Director, width=39, bg="black", fg="white")
        self.txtDirector.grid(row=3, column=1)

        self.lblCast=Label(LeftBody, font=('Arial', 18, 'bold'), text="Cast:", padx=2, pady=2, bg="black", fg="orange")
        self.lblCast.grid(row=4, column=0, sticky=W) 
        self.txtCast=Entry(LeftBody, font=('Arial', 18, 'bold'), textvariable=Cast, width=39, bg="black", fg="white")
        self.txtCast.grid(row=4, column=1)

        self.lblBudget=Label(LeftBody, font=('Arial', 18, 'bold'), text="Budget (Crores INR):", padx=2, pady=2, bg="black", fg="orange")
        self.lblBudget.grid(row=5, column=0, sticky=W) 
        self.txtBudget=Entry(LeftBody, font=('Arial', 18, 'bold'), textvariable=Budget, width=39, bg="black", fg="white")
        self.txtBudget.grid(row=5, column=1)

        self.lblDuration=Label(LeftBody, font=('Arial', 18, 'bold'), text="Duration (Hrs):", padx=2, pady=2, bg="black", fg="orange")
        self.lblDuration.grid(row=6, column=0, sticky=W) 
        self.txtDuration=Entry(LeftBody, font=('Arial', 18, 'bold'), textvariable=Duration, width=39, bg="black", fg="white")
        self.txtDuration.grid(row=6, column=1)

        self.lblRating=Label(LeftBody, font=('Arial', 18, 'bold'), text="Rating (Out of 5):", padx=2, pady=2, bg="black", fg="orange")
        self.lblRating.grid(row=7, column=0, sticky=W) 
        self.txtRating=Entry(LeftBody, font=('Arial', 18, 'bold'), textvariable=Rating, width=39, bg="black", fg="white")
        self.txtRating.grid(row=7, column=1)

        
        #Scroll bar
        scroll=Scrollbar(RightBody)
        scroll.grid(row=0, column=1, sticky='ns')

        MovieList=Listbox(RightBody, width=41, height=16, font=('Arial', 12, 'bold'), bg="black", fg="white", yscrollcommand=scroll.set)
        MovieList.bind('<<ListboxSelect>>', movieRec)
        MovieList.grid(row=0, column=0, padx=8)
        scroll.config(command=MovieList.yview)

        #self.btnback=Button(BottomFrame, text="Back", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="orange",command=lambda:self.goBack(MainFrame))
        #self.btnback.grid(row=0, column=0)

        self.btnadd=Button(BottomFrame, text="Add New", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="orange",command=addData)
        self.btnadd.grid(row=0, column=1)

        self.btnclear=Button(BottomFrame, text="Clear", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="orange",command=clcdata)
        self.btnclear.grid(row=0, column=2)

        self.btndisp=Button(BottomFrame, text="Display", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="orange",command=disData)
        self.btndisp.grid(row=0, column=3)

        self.btndel=Button(BottomFrame, text="Delete", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="orange",command=delData)
        self.btndel.grid(row=0, column=4)

        self.btnbook=Button(BottomFrame, text="Bookings", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="orange",command=lambda:self.gotoBook())
        self.btnbook.grid(row=0, column=5)

    '''
    def goBack(self,frame):
        
        frame.grid_forget()
        first.Firstpage(root)
    '''

    def gotoBook(self):
        
        #frame.grid_forget()
        top = Toplevel()
        booking.Bookings(top)



if __name__=='__main__':
	root=Tk()
	application = Movie(root)
	root.mainloop()