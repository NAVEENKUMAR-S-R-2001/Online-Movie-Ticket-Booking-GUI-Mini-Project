from tkinter import *
import tkinter.messagebox  as MessageBox
import mysql.connector as mysql

def submit():
    name=entry_name.get()
    dob=entry_seat.get()
    usn=entry_no.get()
    phone=entry_g.get()
    branch=entry_b.get()
    section=entry_movie.get()
    address=entry_amt.get()

    if(name=='' or dob==''or usn==''or phone=='' or branch=='' or section=='' or address==''):
        MessageBox.showinfo('submit Status','All Feilds are requird')
 
    else:
        con=mysql.connect(host='localhost',user='root',password='',database='student_info')
        cursor=con.cursor()
        cursor.execute("insert into student values('"+name+"','"+dob+"','"+usn+"','"+phone+"','"+branch+"','"+section+"','"+address+"')")
        cursor.execute("commit")

        entry_name.delete(0,'end')
        entry_seat.delete(0,'end')
        entry_no.delete(0,'end')
        entry_g.delete(0,'end')
        entry_b.delete(0,'end')
        entry_movie.delete(0,'end')
        entry_amt.delete(0,'end')
        MessageBox.showinfo("Submit Status","Submitted successfully")
        con.close()

def delete():
    if entry_no.get()=='':
        MessageBox.showinfo('Cancel Status','Mobile No is compalsory for Cancel')
    else:
        con=mysql.connect(host='127.0.0.1 ',user='root',password='',database='student_info')
        cursor=con.cursor()
        cursor.execute("delete from student where  usn='"+entry_usn.get()+"'")
        cursor.execute("commit");

        entry_name.delete(0,'end')
        entry_seat.delete(0,'end')
        entry_no.delete(0,'end')
        entry_g.delete(0,'end')
        entry_b.delete(0,'end')
        entry_movie.delete(0,'end')
        entry_amt.delete(0,'end')
        MessageBox.showinfo("Delete Status","Deleted successfully")
        con.close()



def update():
    name=entry_name.get()
    dob=entry_seat.get()
    usn=entry_no.get()
    phone=entry_g.get()
    branch=entry_b.get()
    section=entry_movie.get()
    address=entry_amt.get()

    if(name=='' or dob==''or usn==''or phone=='' or branch=='' or section=='' or address==''):
        MessageBox.showinfo('Update Status','All Feilds are requird')
 
    else:
        con=mysql.connect(host='localhost',user='root',password='',database='student_info')
        cursor=con.cursor()
        cursor.execute("update student set name='"+name+"',dob='"+dob+"',usn='"+usn+"',phone='"+phone+"',branch='"+branch+"',section='"+section+"',address='"+address+"'")
        cursor.execute("commit")

        entry_name.delete(0,'end')
        entry_seat.delete(0,'end')
        entry_no.delete(0,'end')
        entry_g.delete(0,'end')
        entry_b.delete(0,'end')
        entry_movie.delete(0,'end')
        entry_amt.delete(0,'end')
        MessageBox.showinfo("update Status","Updated successfully")
        con.close()


def get():
    if entry_no.get()=='':
        MessageBox.showinfo('fetch Status','Mobile No is compalsory for  Fetch data')
    else:
        con=mysql.connect(host='127.0.0.1 ',user='root',password='',database='student_info')
        cursor=con.cursor()
        cursor.execute("select * from student where usn='"+entry_usn.get()+"'")
        rows=cursor.fetchall()

        for row in rows:
            entry_name.insert(0,row[0])
            entry_seat.insert(0,row[1])
            entry_g.insert(0,row[3])
            entry_b.insert(0,row[4])
            entry_movie.insert(0,row[5])
            entry_amt.insert(0,row[6])
            
        con.close()

def show():
        con=mysql.connect(host='127.0.0.1 ',user='root',password='',database='student_info')
        cursor=con.cursor()
        cursor.execute("select * from student ")
        rows=cursor.fetchall()

        for row in rows:
            insertData=row[0]+'   '+row[1]+'   '+row[2]+'   '+str(row[3])+'   '+row[4]+'   '+row[5]+'   '+row[6]
            list_s.insert(list_s.size()+1,insertData)

        con.close()


    
    
win =Tk()
win.title("STUDENT DETAILES")
win.geometry("1800x800")
win.configure(bg='black')

name= StringVar()
dob=StringVar()
usn=StringVar()
phone=IntVar()
branch=StringVar()
section=StringVar()
address=StringVar()

Label(win,text='\u2680Online Movie Ticket Booking System(Book Your Show Now)\u2680',font=('Arial',30,'bold'),bg="orange",fg="black").place(x=200,y=20)



Label(win,text="Customer Name :",font=('Arial',15,'bold'),bg="white",fg="black").place(x=10,y=120)
entry_name = Entry(win,textvariable=name,relief = "solid")
entry_name.place(x=290,y=120,height=30,width=200)
 

Label(win,text="Total No of Seat: ",font=('Arial',15,'bold'),bg="white",fg="black").place(x=10,y=190)
entry_seat = Entry(win,textvariable=dob,relief = "solid")
entry_seat.place(x=290,y=190,height=30,width=200)

Label(win,text="Customer Mobile No : ",font=('Arial',15,'bold'),bg="white",fg="black").place(x=10,y=260)
entry_no= Entry(win,textvariable=usn,relief = "solid")
entry_no.place(x=290,y=260,height=30,width=200)

Label(win,text="Gold class Seat(120): ",font=('Arial',15,'bold'),bg="white",fg="black").place(x=10,y=330)
entry_g= Entry(win,textvariable=phone,relief = "solid")
entry_g.place(x=290,y=330,height=30,width=200)

Label(win,text="Balcony Seat(60): ",font=('Arial',15,'bold'),bg="white",fg="black").place(x=10,y=400)
entry_b= Entry(win,textvariable=branch,relief = "solid")
entry_b.place(x=290,y=400,height=30,width=200)

Label(win,text="Movie Name : ",font=('Arial',15,'bold'),bg="white",fg="black").place(x=10,y=470)
entry_movie= Entry(win,textvariable=section,relief = "solid")
entry_movie.place(x=290,y=470,height=30,width=200)


Label(win,text="Total Amount : ",font=('Arial',15,'bold'),bg="white",fg="black").place(x=10,y=540)
entry_amt= Entry(win,textvariable=address,relief = "solid")
entry_amt.place(x=290,y=540,height=30,width=200)


submit=Button(win,text='Submit',font=('italic',15,'bold'),width=10,height=1,bd=4,bg='orange',command=submit,relief = "solid")
submit.place(x=100,y=700)

delete=Button(win,text='Cancel',font=('italic',15,'bold'),width=10,height=1,bd=4,bg='orange',command=delete,relief = "solid")
delete.place(x=400,y=700)

update=Button(win,text='Update',font=('italic',15,'bold'),width=10,height=1,bd=4,bg='orange',command=update,relief = "solid")
update.place(x=700,y=700)

get=Button(win,text='Get',font=('italic',15,'bold'),width=10,height=1,bd=4,bg='orange',command=get,relief = "solid")
get.place(x=1000,y=700)

view=Button(win,text='See Which Movie Realse In Theatures',font=('italic',15,'bold'),width=80,height=1,bd=4,bg='Yellow',command=get,relief = "solid")
view.place(x=230,y=630)

list_s=Listbox(win)
list_s.place(x=650,y=100,width=850, height=500)
show()
win.mainloop()

