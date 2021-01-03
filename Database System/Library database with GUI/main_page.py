#Lakshmaiah Dinesh Hitesh- 1001679243
#Amartejas manjunath- 1001742606

from tkinter import *
import tkinter as tk
import mysql.connector
from notify import triger

from datetime import date,timedelta

Mem_id=0
membership_id=0
requested_book=0
book_wanted=0
book_returned=0
current_mem_id=""
current_emp=""


reff=triger()

def update_mem_id():
    global Mem_id
    file1 = open("/Users/hitesh/PycharmProjects/DB_project2/venv/buffer1.txt", "r")
    Mem_id=file1.readline()
    file1.close()
    file1 = open("/Users/hitesh/PycharmProjects/DB_project2/venv/buffer1.txt", "w")
    Mem_id=int(Mem_id)+1
    file1.write(str(Mem_id))
    file1.close()

def mem_login_validate(a,b):
    global current_mem_id
    conn = mysql.connector.connect(user='root', password='Godream2021!',
                              host='127.0.0.1',
                              database='LIBRARY',auth_plugin='mysql_native_password')
    cursor = conn.cursor()
    cursor.execute("SELECT USERNAME,PASSWORD,mem_id FROM LIBRARY.MEMBERS where USERNAME='"+ str(a) +"' and PASSWORD='"+str(b)+"';")
    row = cursor.fetchone()
    current_mem_id=row[2]
    if row :
        correct_mem()
    else:
        reff.error_notification()
    cursor.close()
    conn.close()

def emp_login_validate(a,b):
    global current_emp
    conn = mysql.connector.connect(user='root', password='Godream2021!',
                              host='127.0.0.1',
                              database='LIBRARY',auth_plugin='mysql_native_password')
    cursor = conn.cursor()
    cursor.execute("SELECT USERNAME,PASSWORD,POSITION FROM LIBRARY.EMPLOYEE where username='"+ str(a) +"' and PASSWORD='"+str(b)+"';")
    row = cursor.fetchone()
    if row :
        current_emp=a
        correct_emp()
    else:
        reff.error_notification()

    cursor.close()
    conn.close()


def view_books():
    view_b = Tk()
    view_b.title("List of Books")
    view_b.minsize(100,100)
    T = tk.Text(view_b, height=100, width=150)
    T.pack()
    disp=""
    conn = mysql.connector.connect(user='root', password='Godream2021!',
                                   host='127.0.0.1',
                                   database='LIBRARY', auth_plugin='mysql_native_password')

    cursor = conn.cursor()
    cursor.execute("SELECT ISBN,TITLE,EDITION FROM LIBRARY.BOOKS ;")

    row = cursor.fetchone()

    while row is not None:
        ISBN="ISBN:"+row[0] +"\t\t\t"
        title="TITLE:" + row[1] +"\t\t\t\t\t\t\t\t\t\t\t"
        edition="EDITION"+row[2]
        disp=str(disp)+str(ISBN)+title+str(edition)+"\n"
        row = cursor.fetchone()

    cursor.close()
    conn.close()

    T.insert(tk.END, disp)

    cancel = Button(view_b, text="CANCEL",font=( 32), command=view_b.destroy,height="3",width="15")
    cancel.place(relx=0.5, rely=0.8, anchor=S)



def mem_login():

    def callback():
        a=username_field.get()
        b=password_field.get()
        mem_login_validate(a,b)
        username_field.delete(0, 'end')
        password_field.delete(0, 'end')
        member_login.destroy()
    def focus1(event):
        username_field.focus_set()
    def focus2(event):
        password_field.focus_set()

    # create a GUI window
    member_login = Tk()
    member_login.title("MEMBER LOGIN")
    member_login.geometry("400x100")
    username = Label(member_login, text="Username")
    password = Label(member_login, text="Password")
    username.grid(row=1, column=0)
    password.grid(row=2, column=0)

    username_field = Entry(member_login)
    password_field = Entry(member_login)
    username_field.bind("<Return>", focus1)
    password_field.bind("<Return>", focus2)
    username_field.grid(row=1, column=1, ipadx="60")
    password_field.grid(row=2, column=1, ipadx="60")
    submit = Button(member_login, text="Submit", command=callback)
    submit.grid(row=4, column=1)

def insert_book():


    def insert():
        global Mem_id, membership_id
        update_mem_id()
        member_id = "LIB" + str(Mem_id)
        reff.inbox_msg(member_id)
        a = isbn_field.get()
        b = title_field.get()
        c=1
        d = edition_field.get()
        e = "YES"
        f = "NULL"
        g = book_typee_no_field.get()
        STATS = "YES"
        dss=desc_field.get()
        athr=author_field.get()
        sub=sub_area_field.get()


        conn = mysql.connector.connect(user='root', password='Godream2021!',
                                       host='127.0.0.1',
                                       database='LIBRARY', auth_plugin='mysql_native_password')
        cursor = conn.cursor()

        cursor.execute("select no_of_copies from library.books where isbn=\""+str(a)+"\";")
        know=cursor.fetchone()
        if know is not None:
            data = "insert into LIBRARY.books values" + "(\"" + str(a) + "\",\"" + str(b) + "\",\"" + str(int(know(0))+1) + "\",\"" + d + "\",\"" + e + "\",\"" + f + "\",\"" + g  + "\");"
            cursor.execute(data)
        else:
            data = "insert into LIBRARY.books values" + "(\"" + str(a) + "\",\"" + str(b) + "\",\"" + str(c) + "\",\"" + d + "\",\"" + e + "\",\"" + f + "\",\"" + g + "\");"
            cursor.execute(data)

        cursor.execute("insert into LIBRARY.catalog values(\"" + str(a) + "\",\"" + str(
            b) +"\",\""+str(dss)+ "\",\""+str(athr) +"\",\""+str(sub) +"\",\""+str(STATS)+"\",\"" + "NULL" + "\");")

        conn.commit()
        cursor.close
        conn.close()
        clear()
        root.destroy()
    def focus1(event):
        isbn_field.focus_set()

    def focus2(event):
        title_field.focus_set()

    def focus3(event):
        edition_field.focus_set()

    def focus5(event):
        book_typee_no_field.focus_set()

    def focus6(event):
        desc_field.focus_set()

    def focus7(event):
        author_field.focus_set()

    def focus8(event):
        sub_area_field.focus_set()


    def clear():
        # clear the content of text entry box
        isbn_field.delete(0, END)
        title_field.delete(0, END)
        book_typee_no_field.delete(0, END)
        edition_field.delete(0, END)
        desc_field.delete(0, END)
        author_field.delete(0, END)
        sub_area_field.delete(0, END)



    # create a GUI window

    conn = mysql.connector.connect(user='root', password='Godream2021!',
                                   host='127.0.0.1',
                                   database='LIBRARY', auth_plugin='mysql_native_password')

    cursor = conn.cursor()

    cursor.execute("select position from LIBRARY.employee where username=\"" + current_emp + "\";")
    col = cursor.fetchone()

    if (str(col[0]) == "REFERENCE_LIB"):
        root = Tk()
        root.title("BOOK INSERTION")
        root.geometry("600x300")
        isbn = Label(root, text="ISBN")
        title = Label(root, text="TITLE")
        edition = Label(root, text="EDITION")
        book_typee = Label(root, text="BOOK TYPE")
        desc = Label(root, text="DESCRIPTION")
        authur = Label(root, text="AUTHOR")
        SUB_AREA = Label(root, text="SUBJECT AREA")


        isbn.grid(row=1, column=0)
        title.grid(row=2, column=0)
        edition.grid(row=3, column=0)
        book_typee.grid(row=4, column=0)
        desc.grid(row=5, column=0)
        authur.grid(row=6, column=0)
        SUB_AREA.grid(row=7, column=0)

        isbn_field = Entry(root)
        title_field = Entry(root)
        edition_field = Entry(root)
        book_typee_no_field = Entry(root)
        desc_field = Entry(root)
        author_field = Entry(root)
        sub_area_field = Entry(root)


        isbn_field.bind("<Return>", focus1)
        title_field.bind("<Return>", focus2)
        edition_field.bind("<Return>", focus3)
        book_typee_no_field.bind("<Return>", focus5)
        desc_field.bind("<Return>", focus6)
        author_field.bind("<Return>", focus7)
        sub_area_field.bind("<Return>", focus8)


        isbn_field.grid(row=1, column=1, ipadx="100")
        title_field.grid(row=2, column=1, ipadx="100")
        edition_field.grid(row=3, column=1, ipadx="100")
        book_typee_no_field.grid(row=4, column=1, ipadx="100")
        desc_field.grid(row=5, column=1, ipadx="100")
        author_field.grid(row=6, column=1, ipadx="100")
        sub_area_field.grid(row=7, column=1, ipadx="100")



        submit = Button(root, text="Submit", command=insert)
        submit.grid(row=9, column=1)

    else:
        reff.error_notification1()


def correct_emp():

    def check():
        a=e1.get()
        conn = mysql.connector.connect(user='root', password='Godream2021!',
                                      host='127.0.0.1',
                                      database='LIBRARY', auth_plugin='mysql_native_password')

        cursor = conn.cursor()
        cursor.execute("select isbn,title,no_of_copies,availability from LIBRARY.books where isbn=\"" + a + "\";")
        row = cursor.fetchone()
        if row is not None:
            cursor.execute("select author from LIBRARY.catalog where isbn=\"" + a + "\";")
            col=cursor.fetchone()
            book_details = "ISBN:" + row[0] + "\nTITLE:" + row[1] + "\nAUTHOR:" + col[0] + "\nNO_OF_COPIES:" + row[2]+ "\nAVAILABILITY:"+row[3]
            cursor.close()
            conn.close()
            reff.details(book_details)
        else:
            reff.enter_book()
        e1.delete(0, 'end')

    def description():
        a=e2.get()
        conn = mysql.connector.connect(user='root', password='Godream2021!',
                                      host='127.0.0.1',
                                      database='LIBRARY', auth_plugin='mysql_native_password')

        cursor = conn.cursor()

        cursor.execute("select position from LIBRARY.employee where username=\"" + current_emp+ "\";")
        col=cursor.fetchone()

        if(str(col[0])=="REFERENCE_LIB"):

            cursor.execute("select * from LIBRARY.catalog where isbn=\"" + a + "\";")
            row = cursor.fetchone()
            if row is not None:
                mystr=row[2]
                book_details = "ISBN:" + row[0] + "\nTITLE:" + row[1] + "\nDESCRIPTION:" + mystr[0:60]+"\n\t     "+ mystr[61:120]+"\n\t     "+ mystr[121:180]+"\n\t     "+ mystr[181:240]+"\n\t     "+ mystr[241:299]+"\n"+"SUBJECT AREA:"+row[4]
                conn.commit()
                cursor.close()
                conn.close()
                reff.details(book_details)
            else:
                reff.enter_book()

        else:
            reff.error_notification1()
        e2.delete(0, 'end')

    def due_check():
        id=e3.get()
        if (id!=""):
            conn = mysql.connector.connect(user='root', password='Godream2021!',
                                           host='127.0.0.1',
                                           database='LIBRARY', auth_plugin='mysql_native_password')

            cursor = conn.cursor()

            cursor.execute("select position from LIBRARY.employee where username=\"" + current_emp + "\";")
            col = cursor.fetchone()

            if (str(col[0]) == "REFERENCE_LIB"):

                cursor.execute("SELECT mem_type FROM library.members where mem_id=\"" + str(id) + "\";")
                col1 = cursor.fetchone()

                if (str(col1[0]) != "professor"):
                    cursor.execute("SELECT borrow_date,isbn FROM library.issue where mem_id=\""+str(id) +"\";")
                    row = cursor.fetchone()

                    if row is not None:
                        while row is not None:

                            datte=row[0]
                            datte2 = date.today()
                            datte = str(datte)
                            bal = datte.split('-')
                            month = int(bal[1])
                            day = int(bal[2])
                            year = int(bal[0])

                            datte2 = str(datte2)
                            bal = datte2.split('-')
                            month2 = int(bal[1])
                            day2 = int(bal[2])
                            year2 = int(bal[0])

                            d0 = date(year, month, day)
                            d1 = date(year2, month2, day2)
                            delta = d1 - d0
                            days = delta.days

                            if ((days >= 22) and (days < 28)):
                                reff.mail1("ISBN: "+str(row[1])+"\nRemaining Grace period is " + str(int(days)-21))
                            elif(days >= 28):
                                reff.mail1("ISBN: "+str(row[1])+"\nPlease return your book, grace period is over")
                            elif ((days >= 0) and (days < 22)):
                                reff.remainder("ISBN: "+str(row[1])+"\nDAYS SINCE BORROWED: "+str(days))
                            row = cursor.fetchone()

                    else:
                        reff.no_book_to_chck_due()
                else:
                    cursor.execute(
                        "SELECT borrow_date,isbn FROM library.issue where mem_id=\"" + str(id)  + "\";")
                    row = cursor.fetchone()
                    if row is not None:
                        while row is not None:

                            datte = row[0]
                            datte2 = date.today()
                            datte = str(datte)
                            bal = datte.split('-')
                            month = int(bal[1])
                            day = int(bal[2])
                            year = int(bal[0])

                            datte2 = str(datte2)
                            bal = datte2.split('-')
                            month2 = int(bal[1])
                            day2 = int(bal[2])
                            year2 = int(bal[0])

                            d0 = date(year, month, day)
                            d1 = date(year2, month2, day2)
                            delta = d1 - d0
                            days = delta.days
                            grac_days = days - 90

                            if ((grac_days >= 0) and (grac_days <= 15)):
                                reff.mail1(
                                    "ISBN:" + str(row[1]) + "\nGrace period end with in " + str(grac_days) + " days")
                            elif ((grac_days > 15)):
                                reff.mail1(
                                    "ISBN:" + str(row[1]) + "\nGrace date exceeded.\n you will me fined")
                            elif ((days >= 0) and (days < 91)):
                                reff.remainder_for_member(
                                    "ISBN:" + str(row[1]) + "\nRemaining days to return is " + str(91 - days))
                            row = cursor.fetchone()
                    else:
                        reff.no_book_to_chck_due()



            else:
                reff.error_notification1()
            e3.delete(0, 'end')
            cursor.close()
            conn.close()
        else:
            reff.enter_mem_id()

    def weekly_report():
        today = date.today()
        week_ago = today - timedelta(days=7)

        conn = mysql.connector.connect(user='root', password='Godream2021!',
                                       host='127.0.0.1',
                                       database='LIBRARY', auth_plugin='mysql_native_password')

        cursor = conn.cursor()

        cursor.execute("select position from LIBRARY.employee where username=\"" + current_emp + "\";")
        col = cursor.fetchone()

        if (str(col[0]) == "REFERENCE_LIB"):
            cursor.execute("select isbn,mem_id,borrow_date,book_borrowed from LIBRARY.issue where Borrow_Date between\'" + str(week_ago) +"\' and \'"+str(today)+ "\';")
            row = cursor.fetchone()
            if row is not None:
                view_b = Tk()
                view_b.title("WEEKLY REPORT")
                view_b.minsize(100, 100)
                T = tk.Text(view_b, height=100, width=150)
                T.pack()
                disp = ""

                while row is not None:
                    ISBN = "ISBN: " + row[0] + "\t\t\t"
                    MEM_ID = "MEM_ID: " + row[1] + "\t\t\t"
                    BORROW_DT = "BORROW_DATE: " + row[2]
                    TITLE="TITLE: " +row[3]+ "\t\t\t\t"
                    disp = disp + str(ISBN) + str(TITLE)+ str(MEM_ID) + str(BORROW_DT)  + "\n"
                    row = cursor.fetchone()

                T.insert(tk.END, disp)
                cancel = Button(view_b, text="CANCEL", font=(32), command=view_b.destroy, height="3", width="15")
                cancel.place(relx=0.5, rely=0.8, anchor=S)
            else:
                reff.no_weekly_report()
        else:
            reff.error_notification1()
            e3.delete(0, 'end')
        cursor.close()
        conn.close()



    def focus1(event):
        e1.focus_set()
    def focus2(event):
        e2.focus_set()

    def focus3(event):
        e3.focus_set()

    newwin = Tk()
    newwin.minsize(400, 400)
    newwin.title("EMPLOYEE")
    Label(newwin, text='Book to check:', justify='center').grid(row=1)
    Label(newwin, text='Description of:', justify='center').grid(row=2)
    Label(newwin, text='MEMBER_ID').grid(row=3)



    e1 = Entry(newwin)
    e2 = Entry(newwin)
    e3=Entry(newwin)
    e1.bind("<Return>", focus1)
    e2.bind("<Return>", focus2)
    e3.bind("<Return>", focus3)


    e1.grid(row=1, column=2)
    e2.grid(row=2, column=2)
    e3.grid(row=3, column=2)


    button = tk.Button(newwin, text='Check', width=5, height=1, command=check)
    button.grid(row=1, column=3)

    button3 = tk.Button(newwin, text='Submit', width=5, height=1, command=description)
    button3.grid(row=2, column=3)

    button2 = tk.Button(newwin, text='Check Due Date', width=13, height=1, command=due_check)
    button2.grid(row=3, column=3)

    button3 = tk.Button(newwin, text=' GET WEEKLY REPORT', width=20, height=2, command=weekly_report)
    button3.grid(row=4, column=1)

    button3 = tk.Button(newwin, text='INSERT BOOK', width=20, height=2, command=insert_book)
    button3.grid(row=5, column=1)

def check_due_date_mem():
    conn = mysql.connector.connect(user='root', password='Godream2021!',
                                   host='127.0.0.1',
                                   database='LIBRARY', auth_plugin='mysql_native_password')

    cursor = conn.cursor()
    cursor.execute("SELECT mem_type FROM library.members where mem_id=\"" + current_mem_id + "\";")
    col = cursor.fetchone()

    if(str(col[0])!="professor"):
        cursor.execute("SELECT borrow_date,isbn FROM library.issue where mem_id=\"" + current_mem_id + "\";")
        row = cursor.fetchone()
        if row is not None:
            while row is not None:

                datte = row[0]
                datte2 = date.today()
                datte = str(datte)
                bal = datte.split('-')
                month = int(bal[1])
                day = int(bal[2])
                year = int(bal[0])

                datte2 = str(datte2)
                bal = datte2.split('-')
                month2 = int(bal[1])
                day2 = int(bal[2])
                year2 = int(bal[0])

                d0 = date(year, month, day)
                d1 = date(year2, month2, day2)
                delta = d1 - d0
                days = delta.days
                grac_days=days-21


                if ((grac_days >=0) and (grac_days <=7)):
                    reff.remainder_for_member("ISBN:"+str(row[1])+"\nGrace period end with in "+ str(grac_days) +" days" )
                elif ((grac_days >7)):
                    reff.remainder_for_member("ISBN:"+str(row[1])+"\nGrace date exceeded.\n you will me fined" )
                elif ((days >= 0) and (days < 22)):
                    reff.remainder_for_member("ISBN:"+str(row[1])+"\nRemaining days to return is "+str(21-days))
                row = cursor.fetchone()
        else:
            reff.no_book_to_chck_due()

    else:
        cursor.execute("SELECT borrow_date,isbn FROM library.issue where mem_id=\"" + current_mem_id + "\";")
        row = cursor.fetchone()
        if row is not None:
            while row is not None:

                datte = row[0]
                datte2 = date.today()
                datte = str(datte)
                bal = datte.split('-')
                month = int(bal[1])
                day = int(bal[2])
                year = int(bal[0])

                datte2 = str(datte2)
                bal = datte2.split('-')
                month2 = int(bal[1])
                day2 = int(bal[2])
                year2 = int(bal[0])

                d0 = date(year, month, day)
                d1 = date(year2, month2, day2)
                delta = d1 - d0
                days = delta.days
                grac_days = days - 90

                if ((grac_days >= 0) and (grac_days <= 15)):
                    reff.remainder_for_member(
                        "ISBN:" + str(row[1]) + "\nGrace period end with in " + str(grac_days) + " days")
                elif ((grac_days > 15)):
                    reff.remainder_for_member("ISBN:" + str(row[1]) + "\nGrace date exceeded.\n you will me fined")
                elif ((days >= 0) and (days < 91)):
                    reff.remainder_for_member("ISBN:" + str(row[1]) + "\nRemaining days to return is " + str(91 - days))
                row = cursor.fetchone()
        else:
            reff.no_book_to_chck_due()


    cursor.close()
    conn.close()

def process_requested_book(book_requested):
    tdy = date.today()

    conn = mysql.connector.connect(user='root', password='Godream2021!',
                                   host='127.0.0.1',
                                   database='LIBRARY', auth_plugin='mysql_native_password')

    cursor = conn.cursor()
    cursor.execute("SELECT book_type,no_of_copies,availability,title FROM LIBRARY.books where ISBN=\""+book_requested+"\";")

    row = cursor.fetchone()
    if row is not None:

        if(row[0]=="OTHER"):
            if(row[2]=="YES"):
                if(int(row[1])>0 and int(row[1])<=2):
                    cursor.execute("SELECT count(*) FROM LIBRARY.issue where mem_id=\"" + current_mem_id + "\" group by mem_id;")
                    coll=cursor.fetchone()
                    if (coll is not None):
                        if( int(coll[0])<5):
                            reff.Book_alloted()
                            reff.update_copies(book_requested,tdy,str(row[3]),current_mem_id)
                        else:
                            reff.limit_exceed_mem()
                    else:
                        reff.Book_alloted()
                        reff.update_copies(book_requested, tdy, str(row[3]), current_mem_id)
                else:
                    reff.Book_out_of_stock()
            else:
                reff.Book_not_avai()
        else:
            reff.Book_no_rent()
    else:
        reff.enter_book()

    cursor.close()
    conn.close()

def process_return_book(book_returned):

    conn = mysql.connector.connect(user='root', password='Godream2021!',
                                   host='127.0.0.1',
                                   database='LIBRARY', auth_plugin='mysql_native_password')

    cursor = conn.cursor()
    cursor.execute("SELECT no_of_copies,title FROM LIBRARY.books where ISBN=\""+book_returned+"\";")

    row=cursor.fetchone()
    if row is not None:
        row=int(row[0])+1
        if(row<=2 and row>=0):
            cursor.execute("UPDATE LIBRARY.BOOKS SET NO_OF_COPIES = \'" + str(row) + "\' WHERE ISBN=\'" + book_returned + "\' ;")
            reff.book_returned()

    cursor.execute("select borrow_date,book_borrowed from library.issue where isbn=\"" + book_returned + "\";")
    info = cursor.fetchone()
    if info is None:
        reff.no_return()
    else:
        cursor.execute("delete from library.issue WHERE isbn=\"" + str(book_returned) + "\" and mem_id=\""+current_mem_id+"\" ;")

    conn.commit()
    cursor.close()
    conn.close()



def correct_mem():
    def focus1(event):
        req_books_field.focus_set()

    def focus2(event):
        req_books_field.focus_set()

    def mem_submit_book():
        global book_wanted
        book_wanted=req_books_field.get()
        process_requested_book(book_wanted)

    def book_return():
        global book_returned
        book_returned=retu_books_field.get()
        process_return_book(book_returned)

    def extension():
        conn = mysql.connector.connect(user='root', password='Godream2021!',
                                       host='127.0.0.1',
                                       database='LIBRARY', auth_plugin='mysql_native_password')

        cursor = conn.cursor()
        cursor.execute("SELECT mem_dt FROM LIBRARY.members where mem_id=\"" + str(current_mem_id) + "\";")
        row=cursor.fetchone()

        if row is not None:
            datte = row[0]
            datte2 = date.today()
            datte = str(datte)
            bal = datte.split('-')
            month = int(bal[1])
            day = int(bal[2])
            year = int(bal[0])

            datte2 = str(datte2)
            bal = datte2.split('-')
            month2 = int(bal[1])
            day2 = int(bal[2])
            year2 = int(bal[0])

            d0 = date(year, month, day)
            d1 = date(year2, month2, day2)
            delta = d1 - d0
            days = delta.days

            if(days>1461):
                cursor.execute("UPDATE LIBRARY.members SET mem_dt = \"" + str(datte2) + "\"WHERE mem_id=\"" + str(current_mem_id) + "\" ;")
                reff.extend_mail()
            else:
                reff.extend()
        conn.commit()
        cursor.close()
        conn.close()



    newwin = Tk()
    newwin.minsize(400, 400)
    newwin.title("Member Window")
    button = tk.Button(newwin, text='View books', width=15, height=5, command=view_books)
    button.grid(row=1, column=2)

    request=Label(newwin, text='Request books', justify='center')
    return_bo = Label(newwin, text='Return books', justify='center')
    request.grid(row=4)
    return_bo.grid(row=5)

    req_books_field = Entry(newwin)
    retu_books_field = Entry(newwin)
    req_books_field.grid(row=4, column=2)
    retu_books_field.grid(row=5, column=2)
    req_books_field.bind("<Return>", focus1)
    retu_books_field.bind("<Return>", focus2)


    button3 = tk.Button(newwin, text='submit', width=5, height=1, command=mem_submit_book)
    button3.grid(row=4, column=4)

    button2 = tk.Button(newwin, text='Check Due Date', width=15, height=5, command=check_due_date_mem)
    button2.grid(row=2, column=2)

    button4 = tk.Button(newwin, text='return book', width=9, height=1, command=book_return)
    button4.grid(row=5, column=4)

    button5 = tk.Button(newwin, text='Extend Membership', width=15, height=2, command=extension)
    button5.grid(row=7, column=2)

def emp_login():
    def callback():
        a=username_field.get()
        b=password_field.get()
        emp_login_validate(a,b)
        username_field.delete(0, 'end')
        password_field.delete(0, 'end')
        employee_login.destroy()
    def focus1(event):
        username_field.focus_set()
    def focus2(event):
        password_field.focus_set()

    # create a GUI window
    employee_login = Tk()
    employee_login.title("EMPLOYEE LOGIN")
    employee_login.geometry("400x100")
    username = Label(employee_login, text="Username")
    password = Label(employee_login, text="Password")
    username.grid(row=1, column=0)
    password.grid(row=2, column=0)

    username_field = Entry(employee_login)
    password_field = Entry(employee_login)
    username_field.bind("<Return>", focus1)
    password_field.bind("<Return>", focus2)
    username_field.grid(row=1, column=1, ipadx="60")
    password_field.grid(row=2, column=1, ipadx="60")
    submit = Button(employee_login, text="Submit", command=callback)
    submit.grid(row=4, column=1)


def mem_reg():

        def insert():
            global Mem_id,membership_id
            update_mem_id()
            member_id="LIB"+str(Mem_id)
            reff.inbox_msg(member_id)
            dte=date.today()
            a=name_field.get()
            b=ssn_field.get()
            c=haddr_field.get()
            d=caddr_field.get()
            e=contact_no_field.get()
            f=posi_field.get()
            g=usr_field.get()
            h=psd_field.get()
            conn = mysql.connector.connect(user='root', password='Godream2021!',
                                           host='127.0.0.1',
                                           database='LIBRARY', auth_plugin='mysql_native_password')
            cursor = conn.cursor()
            data="insert into LIBRARY.MEMBERS values" +"(\""+"null"+"\",\""+member_id+"\",\""+str(dte)+"\",\""+f+"\",\""+d+"\",\""+c+"\",\""+e+"\",\""+"null"+"\","+ "\"null\""+",\""+g+"\",\""+h+"\",\""+b+"\");"
            cursor.execute(data)
            cursor.execute("insert into LIBRARY.membership_issue values(\""+str(member_id)+"\",\"" + str(
                dte) + "\",\"" + "4 years from date of issue" + "\");")

            conn.commit()
            cursor.close
            conn.close()
            clear()
            root.destroy()
            reff.Mem_ship_id(member_id)
            reff.mail(member_id)


        def focus1(event):
            ssn_field.focus_set()
        def focus2(event):
            haddr_field.focus_set()
        def focus3(event):
            caddr_field.focus_set()
        def focus4(event):
            contact_no_field.focus_set()
        def focus5(event):
            posi_field.focus_set()
        def focus6(event):
            name_field.focus_set()
        def focus7(event):
            usr_field.focus_set()
        def focus8(event):
            psd_field.focus_set()

        def clear():
            # clear the content of text entry box
            name_field.delete(0, END)
            ssn_field.delete(0, END)
            haddr_field.delete(0, END)
            caddr_field.delete(0, END)
            contact_no_field.delete(0, END)
            posi_field.delete(0, END)
            usr_field.delete(0, END)
            psd_field.delete(0, END)

        # create a GUI window
        root = Tk()
        root.title("Membership registration")
        root.geometry("600x300")
        name = Label(root, text="Name")
        ssn = Label(root, text="SSN")
        haddr = Label(root, text="Home address")
        caddr = Label(root, text="campus adddress")
        contact_no = Label(root, text="phone No")
        posi = Label(root, text="position\n(Professor,Staff,other)")
        usr = Label(root, text="username")
        psd = Label(root, text="password")


        name.grid(row=1, column=0)
        ssn.grid(row=2, column=0)
        haddr.grid(row=3, column=0)
        caddr.grid(row=4, column=0)
        contact_no.grid(row=5, column=0)
        posi.grid(row=6, column=0)
        usr.grid(row=7, column=0)
        psd.grid(row=8, column=0)


        name_field = Entry(root)
        ssn_field = Entry(root)
        haddr_field = Entry(root)
        caddr_field = Entry(root)
        contact_no_field = Entry(root)
        posi_field = Entry(root)
        usr_field = Entry(root)
        psd_field = Entry(root)


        name_field.bind("<Return>", focus1)
        ssn_field.bind("<Return>", focus2)
        haddr_field.bind("<Return>", focus3)
        caddr_field.bind("<Return>", focus4)
        contact_no_field.bind("<Return>", focus5)
        posi_field.bind("<Return>", focus6)
        usr_field.bind("<Return>", focus7)
        psd_field.bind("<Return>", focus8)


        name_field.grid(row=1, column=1, ipadx="100")
        ssn_field.grid(row=2, column=1, ipadx="100")
        haddr_field.grid(row=3, column=1, ipadx="100")
        caddr_field.grid(row=4, column=1, ipadx="100")
        contact_no_field.grid(row=5, column=1, ipadx="100")
        posi_field.grid(row=6, column=1, ipadx="100")
        usr_field.grid(row=7, column=1, ipadx="100")
        psd_field.grid(row=8, column=1, ipadx="100")

        submit = Button(root, text="Submit", command=insert)
        submit.grid(row=11, column=1)


def emp_reg():
    def insert():
        global Mem_id, membership_id
        update_mem_id()
        member_id = "LIB" + str(Mem_id)
        reff.inbox_msg(member_id)
        dte = date.today()
        a = name_field.get()
        b = ssn_field.get()
        c = haddr_field.get()
        d = caddr_field.get()
        e = contact_no_field.get()
        f = posi_field.get()
        g = usr_field.get()
        h = psd_field.get()
        conn = mysql.connector.connect(user='root', password='Godream2021!',
                                       host='127.0.0.1',
                                       database='LIBRARY', auth_plugin='mysql_native_password')
        cursor = conn.cursor()
        data = "insert into LIBRARY.employee values" + "(\"" + str(b) + "\",\"" + str(a) + "\",\"" + str(
            f) + "\",\"" + str(d) + "\",\"" + str(c) + "\",\"" + str(e) +  "\",\"" + g + "\",\"" + h  + "\");"
        cursor.execute(data)
        if(f=="professor"):
            data1 = "insert into LIBRARY.MEMBERS values" + "(\"" + "null" + "\",\"" + member_id + "\",\"" + str(
                dte) + "\",\"" + f + "\",\"" + d + "\",\"" + c + "\",\"" + e + "\",\"" + "null" + "\"," + "\"null\"" + ",\"" + g + "\",\"" + h + "\",\"" + b + "\");"
            cursor.execute(data1)

        conn.commit()
        cursor.close
        conn.close()
        clear()
        root.destroy()
        reff.Mem_ship_id(member_id)
        reff.mail(member_id)

    def focus1(event):
        ssn_field.focus_set()

    def focus2(event):
        haddr_field.focus_set()

    def focus3(event):
        caddr_field.focus_set()

    def focus4(event):
        contact_no_field.focus_set()

    def focus5(event):
        posi_field.focus_set()

    def focus6(event):
        name_field.focus_set()

    def focus7(event):
        usr_field.focus_set()

    def focus8(event):
        psd_field.focus_set()

    def clear():
        # clear the content of text entry box
        name_field.delete(0, END)
        ssn_field.delete(0, END)
        haddr_field.delete(0, END)
        caddr_field.delete(0, END)
        contact_no_field.delete(0, END)
        posi_field.delete(0, END)
        usr_field.delete(0, END)
        psd_field.delete(0, END)

    # create a GUI window
    root = Tk()
    root.title("Employment registration form")
    root.geometry("600x300")
    name = Label(root, text="Name")
    ssn = Label(root, text="SSN")
    haddr = Label(root, text="Home address")
    caddr = Label(root, text="campus adddress")
    contact_no = Label(root, text="phone No")
    posi = Label(root, text="position\n(Professor,library_Staff)")
    usr = Label(root, text="username")
    psd = Label(root, text="password")

    name.grid(row=1, column=0)
    ssn.grid(row=2, column=0)
    haddr.grid(row=3, column=0)
    caddr.grid(row=4, column=0)
    contact_no.grid(row=5, column=0)
    posi.grid(row=6, column=0)
    usr.grid(row=7, column=0)
    psd.grid(row=8, column=0)

    name_field = Entry(root)
    ssn_field = Entry(root)
    haddr_field = Entry(root)
    caddr_field = Entry(root)
    contact_no_field = Entry(root)
    posi_field = Entry(root)
    usr_field = Entry(root)
    psd_field = Entry(root)

    name_field.bind("<Return>", focus1)
    ssn_field.bind("<Return>", focus2)
    haddr_field.bind("<Return>", focus3)
    caddr_field.bind("<Return>", focus4)
    contact_no_field.bind("<Return>", focus5)
    posi_field.bind("<Return>", focus6)
    usr_field.bind("<Return>", focus7)
    psd_field.bind("<Return>", focus8)

    name_field.grid(row=1, column=1, ipadx="100")
    ssn_field.grid(row=2, column=1, ipadx="100")
    haddr_field.grid(row=3, column=1, ipadx="100")
    caddr_field.grid(row=4, column=1, ipadx="100")
    contact_no_field.grid(row=5, column=1, ipadx="100")
    posi_field.grid(row=6, column=1, ipadx="100")
    usr_field.grid(row=7, column=1, ipadx="100")
    psd_field.grid(row=8, column=1, ipadx="100")

    submit = Button(root, text="Submit", command=insert)
    submit.grid(row=11, column=1)


if __name__== "__main__":
    master=Tk()
    master.minsize(600, 400)

    master.title('LIBRARY')
    button = tk.Button(master, text='MEMBERSHIP LOGIN', width=20, height=5,command=mem_login)
    button1 = tk.Button(master, text='EMPLOYEE LOGIN', width=20, height=5,command=emp_login)
    button2 = tk.Button(master, text='NEW EMPLOYEE REGISTER', width=25, height=1,command=emp_reg)
    button3 = tk.Button(master, text='NEW MEMBER REGISTER', width=25, height=1,command=mem_reg)


    button.place(relx=0.5, rely=0.1, anchor=N)
    button1.place(relx=0.5, rely=0.5, anchor=CENTER)
    button2.place(relx=0.3, rely=0.7, anchor=CENTER)
    button3.place(relx=0.7, rely=0.7, anchor=CENTER)

    master.mainloop()
