import sqlite3

class Backend():

    def datas(self):
        conn = sqlite3.connect('movie.db')
        conn.execute("PRAGMA foreign_keys = 1")
        c = conn.cursor()

        c.execute("""CREATE TABLE IF NOT EXISTS customer (
                    cid INTEGER PRIMARY KEY,
                    c_name text,
                    email_id text,
                    phone_no text
                )""")

        c.execute(""" CREATE TABLE IF NOT EXISTS movie_data(
                    m_id INTEGER PRIMARY KEY,
                    m_name text,
                    release_date text,
                    director text,
                    actors text,
                    budget integer,
                    duration int,
                    rating int
                )""")
        
        c.execute(""" CREATE TABLE IF NOT EXISTS tickets(
                    ticket_no INTEGER PRIMARY KEY,
                    m_name text,
                    price int,
                    seat_no int,
                    show_date text
                )""")

        c.execute(""" CREATE TABLE IF NOT EXISTS booking(

                    cid INTEGER,
                    ticket_no INTEGER,
                    show_date text,
                    FOREIGN KEY(cid) REFERENCES customer(cid),
                    FOREIGN KEY(ticket_no) REFERENCES tickets(ticket_no),
                    FOREIGN KEY(show_date) REFERENCES tickets(show_date)
                    PRIMARY KEY(cid,ticket_no)

                )""")

        conn.commit()
        conn.close()


    def addMovie(self,m_id,m_name,release_date,director,actors,budget,duration,rating):
        conn = sqlite3.connect('movie.db')
        c = conn.cursor()
        c.execute('INSERT INTO movie_data VALUES(?,?,?,?,?,?,?,?)',(m_id,m_name,release_date,director,actors,budget,duration,rating))
        conn.commit()
        conn.close()

    def ViewMovieData(self):
        conn=sqlite3.connect("movie.db")    
        c=conn.cursor()
        c.execute("SELECT * FROM movie_data")
        rows=c.fetchall()
        conn.commit()
        conn.close()    
        return rows

    def DeleteMovieRec(self,m_id):    
        conn=sqlite3.connect("movie.db")    
        c=conn.cursor()
        c.execute("DELETE FROM movie_data WHERE m_id=?", (m_id,))
        conn.commit()
        conn.close()

    def addCustomerData(self,cid,c_name,email_id,phone_no):
        conn=sqlite3.connect("movie.db")    
        c=conn.cursor()
        c.execute('INSERT INTO customer VALUES(?,?,?,?)',(cid,c_name,email_id,phone_no))
        conn.commit()
        conn.close()

    def ViewCustomerData(self):
        conn=sqlite3.connect("movie.db")    
        c=conn.cursor()
        c.execute("SELECT * FROM customer")
        rows=c.fetchall()
        conn.commit()
        conn.close()    
        return rows

    def DeleteCustomRec(self,cid):    
        conn=sqlite3.connect("movie.db")    
        c=conn.cursor()
        c.execute("DELETE FROM customer WHERE cid=?", (cid,))
        conn.commit()
        conn.close()

    def addTickets(self,ticket_no,m_name,price,seat_no,show_date):
        conn=sqlite3.connect("movie.db")    
        c=conn.cursor()
        c.execute('INSERT INTO tickets VALUES(?,?,?,?,?)',(ticket_no,m_name,price,seat_no,show_date))
        conn.commit()
        conn.close()

    def ViewTicketsData(self):
        conn=sqlite3.connect("movie.db")    
        c=conn.cursor()
        c.execute("SELECT * FROM tickets")
        rows=c.fetchall()
        conn.commit()
        conn.close()    
        return rows


    def addBooking(self,cid,ticket_no,show_date):
        conn=sqlite3.connect("movie.db")    
        c=conn.cursor()
        c.execute('INSERT INTO booking VALUES(?,?,?)',(cid,ticket_no,show_date))
        conn.commit()
        conn.close()

    def deleteBooking(self,cid):
        conn=sqlite3.connect("movie.db")    
        c=conn.cursor()  
        c.execute('DELETE from booking WHERE cid=?',(cid,))
        conn.commit()
        conn.close()

    def ViewBookingRec(self):
        conn=sqlite3.connect("movie.db")    
        c=conn.cursor()
        c.execute("""SELECT c.cid,t.ticket_no,t.show_date
                    FROM customer c,tickets t

                """)
        rows = c.fetchall()
        conn.commit()
        conn.close()
        return rows