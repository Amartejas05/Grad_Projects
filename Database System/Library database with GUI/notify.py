#Lakshmaiah Dinesh Hitesh- 1001679243
#Amartejas manjunath- 1001742606

import tkinter as tk
from tkinter import ttk
import mysql.connector
import smtplib,ssl
from email.mime.text import MIMEText


class triger:
    def extend_mail(self):
        popup = tk.Tk()
        popup.minsize(200, 100)
        popup.wm_title("Notification")
        label = ttk.Label(popup, text="          Membership has been extended")
        label.pack(side="top", fill="x", pady=10)
        B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
        B1.pack()

    def error_notification(self):
        popup = tk.Tk()
        popup.minsize(200, 100)
        popup.wm_title("warning")
        label = ttk.Label(popup, text="          wrong Credentials")
        label.pack(side="top", fill="x", pady=10)
        B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
        B1.pack()

    def extend(self):
        popup = tk.Tk()
        popup.minsize(200, 100)
        popup.wm_title("Notification")
        label = ttk.Label(popup, text="      Membership date not expired")
        label.pack(side="top", fill="x", pady=10)
        B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
        B1.pack()

    def no_weekly_report(self):
        popup = tk.Tk()
        popup.minsize(200, 100)
        popup.wm_title("Notification")
        label = ttk.Label(popup, text="   NO BOOKS BORROWED SINCE LAST WEEK ")
        label.pack(side="top", fill="x", pady=10)
        B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
        B1.pack()

    def no_book_to_chck_due(self):
        popup = tk.Tk()
        popup.minsize(200, 100)
        popup.wm_title("Notification")
        label = ttk.Label(popup, text="  No book borrowed to check due date")
        label.pack(side="top", fill="x", pady=10)
        B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
        B1.pack()

    def enter_book(self):
        popup = tk.Tk()
        popup.minsize(200, 100)
        popup.wm_title("warning")
        label = ttk.Label(popup, text=" enter the book name correctly")
        label.pack(side="top", fill="x", pady=10)
        B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
        B1.pack()

    def enter_mem_id(self):
        popup = tk.Tk()
        popup.minsize(200, 100)
        popup.wm_title("warning")
        label = ttk.Label(popup, text=" enter the member_id correctly")
        label.pack(side="top", fill="x", pady=10)
        B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
        B1.pack()

    def limit_exceed_mem(self):
        popup = tk.Tk()
        popup.minsize(200, 100)
        popup.wm_title("warning")
        label = ttk.Label(popup, text="     You can only borrow 5 books maximum")
        label.pack(side="top", fill="x", pady=10)
        B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
        B1.pack()

    def no_return(self):
        popup = tk.Tk()
        popup.minsize(200, 100)
        popup.wm_title("Notification")
        label = ttk.Label(popup, text="          you have not borrowed book ")
        label.pack(side="top", fill="x", pady=10)
        B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
        B1.pack()

    def remainder(self,msg):
        popup = tk.Tk()
        popup.minsize(200, 100)
        popup.wm_title("Notification")
        label = ttk.Label(popup, text=str(msg))
        label.pack(side="top", fill="x", pady=10)
        B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
        B1.pack()

    def remainder_for_member(self, msg):
        popup = tk.Tk()
        popup.minsize(200, 100)
        popup.wm_title("remainder")
        label = ttk.Label(popup, text=str(msg))
        label.pack(side="top", fill="x", pady=10)
        B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
        B1.pack()

    def error_notification1(self):
        popup = tk.Tk()
        popup.minsize(200, 100)
        popup.wm_title("warning")
        label = ttk.Label(popup, text="          Accesss denied")
        label.pack(side="top", fill="x", pady=10)
        B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
        B1.pack()

    def mail(self,message):
        conn = mysql.connector.connect(user='root', password='Godream2021!',
                                       host='127.0.0.1',
                                       database='LIBRARY', auth_plugin='mysql_native_password')

        cursor = conn.cursor()
        cursor.execute("SELECT camp_addr FROM LIBRARY.members where mem_id=\""+message+"\";")

        row = cursor.fetchone()
        message="The membership card with member ID:" +message +" has been mailed.\nSHIPPING ADDRESS: " + str(row[0])
        smtp_ssl_host = 'smtp.gmail.com'  # smtp.mail.yahoo.com
        smtp_ssl_port = 465
        username = 'hiteshdbprojec2@gmail.com'
        password = 'Hitesh2019'
        sender = 'hiteshdbprojec2@gmail.com'
        targets = ['hiteshdbprojec2@gmail.com']

        msg = MIMEText(str(message))
        msg['Subject'] = 'MEMBERSHIP CARD'
        msg['From'] = sender
        msg['To'] = ', '.join(targets)

        server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
        server.login(username, password)
        server.sendmail(sender, targets, msg.as_string())
        server.quit()

    def mail1(self, message):
        message = str(message)
        smtp_ssl_host = 'smtp.gmail.com'  # smtp.mail.yahoo.com
        smtp_ssl_port = 465
        username = 'hiteshdbprojec2@gmail.com'
        password = 'Hitesh2019'
        sender = 'hiteshdbprojec2@gmail.com'
        targets = ['hiteshdbprojec2@gmail.com', 'hiteshdbprojec2@gmail.com']

        msg = MIMEText(str(message))
        msg['Subject'] = 'REMAINDER'
        msg['From'] = sender
        msg['To'] = ', '.join(targets)

        server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
        server.login(username, password)
        server.sendmail(sender, targets, msg.as_string())
        server.quit()


    def Mem_ship_id(self,a):
        popup = tk.Tk()
        popup.minsize(200, 100)
        popup.title("New message")
        label = ttk.Label(popup, text="          Your member_id is "+a)
        label.pack(side="top", fill="x", pady=10)
        B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
        B1.pack()

    def inbox_msg(self,id):
        file1 = open("/Users/hitesh/PycharmProjects/DB_project2/venv/member_messages.txt", "w")
        file1.write(str(id))
        file1.close()

    def Book_alloted(self):
        popup = tk.Tk()
        popup.minsize(200, 100)
        popup.wm_title("LIBRARY")
        label = ttk.Label(popup, text="          Requested book\nis available\ncontact Librarian")
        label.pack(side="top", fill="x", pady=10)
        B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
        B1.pack()

    def book_returned(self):
        popup = tk.Tk()
        popup.minsize(200, 100)
        popup.wm_title("LIBRARY")
        label = ttk.Label(popup, text="      Book borrowed\n returned successfully.")
        label.pack(side="top", fill="x", pady=10)
        B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
        B1.pack()

    def Book_not_avai(self):
        popup = tk.Tk()
        popup.minsize(200, 100)
        popup.wm_title("LIBRARY")
        label = ttk.Label(popup, text="          Requested book\nnot available")
        label.pack(side="top", fill="x", pady=10)
        B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
        B1.pack()

    def Book_no_rent(self):
        popup = tk.Tk()
        popup.minsize(200, 100)
        popup.wm_title("LIBRARY")
        label = ttk.Label(popup, text="          Requested book\ncannot be rented")
        label.pack(side="top", fill="x", pady=10)
        B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
        B1.pack()

    def Book_out_of_stock(self):
        popup = tk.Tk()
        popup.minsize(200, 100)
        popup.wm_title("LIBRARY")
        label = ttk.Label(popup, text="          Requested book\nis out of stock")
        label.pack(side="top", fill="x", pady=10)
        B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
        B1.pack()

    def details(self,a):
        popup = tk.Tk()
        popup.minsize(400, 400)
        popup.wm_title("LIBRARY")
        label = ttk.Label(popup, text=a)
        label.pack(side="top", fill="x", pady=10)
        B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
        B1.pack()

    def update_copies(self,book_req,date_brw,book_brwd,cur_mem_id):
        conn = mysql.connector.connect(user='root', password='Godream2021!',
                                       host='127.0.0.1',
                                       database='LIBRARY', auth_plugin='mysql_native_password')

        cursor = conn.cursor()
        cursor.execute("select no_of_copies from LIBRARY.books where ISBN=\""+book_req +"\";")
        row = cursor.fetchone()
        cursor.execute("UPDATE LIBRARY.BOOKS SET NO_OF_COPIES = \""+str(int(row[0])-1)+"\"WHERE ISBN=\""+str(book_req) +"\" ;")


        cursor.execute("insert into LIBRARY.ISSUE values(\""+str(book_req)+"\",\""+cur_mem_id+"\",\""+"null"+"\",\""+"null"+"\",\""+ str(date_brw)+"\" ,\""+str(book_brwd)+"\");")

        conn.commit()
        cursor.close()
        conn.close()


