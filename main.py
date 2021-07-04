from tkinter import *
from tkinter import ttk
from tkcalendar import *
import mysql.connector
from tkinter import messagebox
import sqlite3
from datetime import *
from openpyxl import Workbook
import os
from fpdf import FPDF
# import smtplib, ssl
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database='library'
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS members (id INT AUTO_INCREMENT PRIMARY KEY, type VARCHAR(250),"
                 "reference VARCHAR(255), name VARCHAR(255), surname VARCHAR(255), phone_number VARCHAR(255),"
                 "email VARCHAR(255), address VARCHAR(255), status VARCHAR(255), debt VARCHAR(255))")

con = sqlite3.connect(r"C:\Users\erdem\Desktop\LibraryManagementSystem\sqlitedb.db")
cursor = con.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS books (barcode TEXT, title TEXT, writer TEXT, status TEXT,"
               "shelf TEXT, borrower TEXT, lendingDate TEXT, receiveDate TEXT)")
con.commit()

class Library(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.wm_geometry("600x400+400+100")
        self.wm_title("Kütüphane Yönetim Sistemi")
        self.wm_iconbitmap(default=r"C:\Users\erdem\Desktop\LibraryManagementSystem\Books.ico")
        self.wm_resizable(False, False)

        combostyle = ttk.Style()
        combostyle.theme_create("combostyle", parent="alt", settings={"TCombobox":
                                                                          {"configure":
                                                                               {'fieldbackground': "#fed39f",
                                                                                "background": "#f6eec9"}}})
        combostyle.theme_use("combostyle")

        self.frame1 = Frame(self, height=150, bg="#f6eec9")
        self.frame1.pack(fill=X)
        self.frame2 = Frame(self, height=450, bg="#fed39f")
        self.frame2.pack(fill=X)

        self.image = PhotoImage(file=r"C:\Users\erdem\Desktop\LibraryManagementSystem\books-icon.png")
        self.favicon = Label(self.frame1, image=self.image, bg="#f6eec9")
        self.favicon.place(x=65, y=5)
        self.heading = Label(self.frame1, text="KÜTÜPHANE", font=("Garamond", 35, "bold"), bg="#f6eec9")
        self.heading.place(x=210, y=40)
        self.heading = Label(self.frame1, text="YÖNETİM SİSTEMİ", font=("Garamond", 25, "bold"), bg="#f6eec9")
        self.heading.place(x=210, y=95)

        self.dugme1 = Button(self.frame2, text="ÜYELER", font=("Garamond", 15, "bold"), bg="#f6eec9",
                             activebackground="#fed39f", command=Members)
        self.dugme1.place(x=200, y=40, width=200)
        self.dugme2 = Button(self.frame2, text="KİTAPLAR", font=("Garamond", 15, "bold"), bg="#f6eec9",
                             activebackground="#fed39f", command=Books)
        self.dugme2.place(x=200, y=100, width=200)
        self.dugme3 = Button(self.frame2, text="KİTAPLIK", font=("Garamond", 15, "bold"), bg="#f6eec9",
                             activebackground="#fed39f", command=BookCase)
        self.dugme3.place(x=200, y=160, width=200)

class Members(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.wm_geometry("600x400+400+100")
        self.wm_title("Üyeler")
        self.wm_iconbitmap(default=r"C:\Users\erdem\Desktop\LibraryManagementSystem\Books.ico")

        style = ttk.Style()
        style.theme_use("combostyle")

        self.frame1 = Frame(self, bg="#f6eec9", width=600, height=400)
        self.frame1.pack()

        Label(self.frame1, text="ÜYE BİLGİLERİ", bg="#f6eec9", font=("Garamond", 25, "bold")).place(x=175)


        Label(self.frame1, text="Üyelik Türü", bg="#f6eec9", font=("Garamond", 15, "bold")).place(x=45, y=50)
        Label(self.frame1, text="Referans No", bg="#f6eec9", font=("Garamond", 15, "bold")).place(x=45, y=80)
        Label(self.frame1, text="İsim", bg="#f6eec9", font=("Garamond", 15, "bold")).place(x=45, y=110)
        Label(self.frame1, text="Soyisim", bg="#f6eec9", font=("Garamond", 15, "bold")).place(x=45, y=140)
        Label(self.frame1, text="Telefon", bg="#f6eec9", font=("Garamond", 15, "bold")).place(x=45, y=170)
        Label(self.frame1, text="Email", bg="#f6eec9", font=("Garamond", 15, "bold")).place(x=45, y=200)
        Label(self.frame1, text="Adres", bg="#f6eec9", font=("Garamond", 15, "bold")).place(x=45, y=230)
        Label(self.frame1, text="Üyelik Durumu", bg="#f6eec9", font=("Garamond", 15, "bold")).place(x=45, y=280)
        Label(self.frame1, text="Borç", bg="#f6eec9", font=("Garamond", 15, "bold")).place(x=45, y=310)

        self.type = ttk.Combobox(self.frame1, font=("Garamond", 15, "bold"), state="readonly",
                                 values=['Öğrenci', "Normal", "Kütüphane Görevlisi"])
        self.type.place(x=350, y=50, width=200)

        self.reference = Entry(self.frame1, font=("Garamond", 15, "bold"), bg="#fed39f")
        self.reference.place(x=350, y=80, width=200)

        self.name = Entry(self.frame1, font=("Garamond", 15, "bold"), bg="#fed39f")
        self.name.place(x=350, y=110, width=200)

        self.surname = Entry(self.frame1, font=("Garamond", 15, "bold"), bg="#fed39f")
        self.surname.place(x=350, y=140, width=200)

        self.phone_number = Entry(self.frame1, font=("Garamond", 15, "bold"), bg="#fed39f")
        self.phone_number.place(x=350, y=170, width=200)

        self.email = Entry(self.frame1, font=("Garamond", 15, "bold"), bg="#fed39f")
        self.email.place(x=350, y=200, width=200)

        self.address = Text(self.frame1, font=("Garamond", 15, "bold"), bg="#fed39f", height=2)
        self.address.place(x=350, y=230, width=200)

        self.status = IntVar(self.frame1)
        self.status0 = Radiobutton(self.frame1, text="Pasif", variable=self.status, value=0, bg="#fed39f")
        self.status0.place(x=350, y=280)
        self.status1 = Radiobutton(self.frame1, text="Aktif", variable=self.status, value=1, bg="#fed39f")
        self.status1.place(x=406, y=280)
        self.status2 = Radiobutton(self.frame1, text="Beklemede", variable=self.status, value=2, bg="#fed39f")
        self.status2.place(x=463, y=280)

        self.debt = Entry(self.frame1, font=("Garamond", 15, "bold"), bg="#fed39f")
        self.debt.place(x=350, y=310, width=200)

        Button(self.frame1, text="KAYDET", command=self.save, bg="#fed39f",
               activebackground="#f6eec9", font=("Garamond", 15, "bold")).place(x=45, y=350, width=125, height=30)

        Button(self.frame1, text="GETİR", command=self.fetch, bg="#fed39f",
               activebackground="#f6eec9", font=("Garamond", 15, "bold")).place(x=171, y=350, width=125, height=30)

        Button(self.frame1, text="GÜNCELLE", command=self.update_, bg="#fed39f",
               activebackground="#f6eec9", font=("Garamond", 15, "bold")).place(x=298, y=350, width=125, height=30)

        Button(self.frame1, text="MAİL", command=self.mail, bg="#fed39f",
               activebackground="#f6eec9", font=("Garamond", 15, "bold")).place(x=425, y=350, width=125, height=30)

    def update_(self):
        sql = "UPDATE members SET type=%s, name=%s, surname=%s, phone_number=%s, email=%s, address=%s, status=%s, " \
              "debt=%s WHERE reference=%s"
        val = (self.type.get(), self.name.get(), self.surname.get(), self.phone_number.get(), self.email.get(),
               self.address.get('1.0', END), self.status.get(), self.debt.get(), self.reference.get())
        mycursor.execute(sql, val)
        mydb.commit()
        self.clear()

    def mail(self):
        pass

    def save(self):
        sql = "INSERT INTO members (type, reference, name, surname, phone_number, email, address, status) " \
              "VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
        val = (self.type.get(), self.reference.get(), self.name.get(), self.surname.get(), self.phone_number.get(),
               self.email.get(), self.address.get('1.0', END), self.status.get())
        mycursor.execute(sql, val)
        mydb.commit()
        self.clear()

    def fetch(self):
        sql = "SELECT * FROM members WHERE reference=%s"
        val = (self.reference.get(),)
        mycursor.execute(sql, val)
        result = mycursor.fetchall()

        for i in result:
            self.type.set("")
            self.name.delete(0, END)
            self.surname.delete(0, END)
            self.phone_number.delete(0, END)
            self.email.delete(0, END)
            self.address.delete('1.0', END)
            self.status.set(3)
            self.debt.delete(0, END)

            self.type.set(i[1])
            self.name.insert(0, i[3])
            self.surname.insert(0, i[4])
            self.phone_number.insert(0, i[5])
            self.email.insert(0, i[6])
            self.address.insert("end", i[7])
            self.status.set(i[8])
            self.debt.insert(0, i[9])


    def clear(self):
        messagebox.showinfo("Başarılı", "İşlem başarılı!")
        self.type.set("")
        self.reference.delete(0, END)
        self.name.delete(0, END)
        self.surname.delete(0, END)
        self.phone_number.delete(0, END)
        self.email.delete(0, END)
        self.address.delete('1.0', END)
        self.status.set(3)
        self.debt.delete(0, END)
        self.focus()


class Books(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.wm_geometry("600x400+400+100")
        self.wm_title("Kitaplar")
        self.wm_iconbitmap(default=r"C:\Users\erdem\Desktop\LibraryManagementSystem\Books.ico")

        style = ttk.Style()
        style.theme_use("combostyle")

        self.frame1 = Frame(self, bg="#f6eec9", width=600, height=400)
        self.frame1.pack()

        Label(self.frame1, text="KİTAP BİLGİLERİ", bg="#f6eec9", font=("Garamond", 25, "bold")).place(x=150)

        Label(self.frame1, text="Barkod", bg="#f6eec9", font=("Garamond", 15, "bold")).place(x=45, y=50)
        Label(self.frame1, text="Başlık", bg="#f6eec9", font=("Garamond", 15, "bold")).place(x=45, y=80)
        Label(self.frame1, text="Yazar", bg="#f6eec9", font=("Garamond", 15, "bold")).place(x=45, y=110)
        Label(self.frame1, text="Durum", bg="#f6eec9", font=("Garamond", 15, "bold")).place(x=45, y=140)
        Label(self.frame1, text="Raf", bg="#f6eec9", font=("Garamond", 15, "bold")).place(x=45, y=170)
        Label(self.frame1, text="Kime", bg="#f6eec9", font=("Garamond", 15, "bold")).place(x=45, y=200)
        Label(self.frame1, text="Ödünç Tarihi", bg="#f6eec9", font=("Garamond", 15, "bold")).place(x=45, y=230)
        Label(self.frame1, text="Teslim Tarihi", bg="#f6eec9", font=("Garamond", 15, "bold")).place(x=45, y=260)

        self.barcode = Entry(self.frame1, font=("Garamond", 15, "bold"), bg="#fed39f")
        self.barcode.place(x=350, y=50, width=200)

        self.title = Entry(self.frame1, font=("Garamond", 15, "bold"), bg="#fed39f")
        self.title.place(x=350, y=80, width=200)

        self.writer = Entry(self.frame1, font=("Garamond", 15, "bold"), bg="#fed39f")
        self.writer.place(x=350, y=110, width=200)

        self.status = IntVar(self.frame1)
        self.status0 = Radiobutton(self.frame1, text="Rafta", variable=self.status, value=0, bg="#fed39f")
        self.status0.place(x=350, y=140, width=80)
        self.status1 = Radiobutton(self.frame1, text="Ödünç Verilmiş", variable=self.status, value=1, bg="#fed39f")
        self.status1.place(x=440, y=140)

        self.shelf = Entry(self.frame1, font=("Garamond", 15, "bold"), bg="#fed39f")
        self.shelf.place(x=350, y=170, width=200)

        self.borrower = ttk.Combobox(self.frame1, font=("Garamond", 15, "bold"), values=["Teslim Al"])
        self.borrower.place(x=350, y=200, width=200)

        self.borrower.bind("<KeyRelease>", self.process)
        self.borrower.bind("<Button-3>", self.process)
        self.borrower.bind("<Return>", self.process)
        self.borrower.bind("<<ComboboxSelected>>", self.process)

        self.lendingDate = DateEntry(self.frame1, font=("Garamond", 15, "bold"), bg="#fed39f", locale="tr_TR",
                                     selectbackground="#fed39f", weekendbackground="#f6eec9", state="disabled")
        self.lendingDate.place(x=350, y=230, width=200)

        self.receiveDate = DateEntry(self.frame1, font=("Garamond", 15, "bold"), bg="#fed39f", locale="tr_TR",
                                     selectbackground="#fed39f", weekendbackground="#f6eec9", state="disabled")
        self.receiveDate.place(x=350, y=260, width=200)

        self.debt = Label(self.frame1, bg="#f6eec9", font=("Garamond", 15, "bold"))
        self.debt.place(x=350, y=290)

        Button(self.frame1, text="KAYDET", command=self.save, bg="#fed39f",
               activebackground="#f6eec9", font=("Garamond", 15, "bold")).place(x=45, y=350, width=125, height=30)

        Button(self.frame1, text="GETİR", command=self.fetch, bg="#fed39f",
               activebackground="#f6eec9", font=("Garamond", 15, "bold")).place(x=171, y=350, width=125, height=30)

        Button(self.frame1, text="GÜNCELLE", command=self.update, bg="#fed39f",
               activebackground="#f6eec9", font=("Garamond", 15, "bold")).place(x=298, y=350, width=125, height=30)

        Button(self.frame1, text="SİL", command=self.delete, bg="#fed39f",
               activebackground="#f6eec9", font=("Garamond", 15, "bold")).place(x=425, y=350, width=125, height=30)

        self.exDebt = 0

    def process(self, event):
        if len(self.borrower.get()) != 0:
            if self.borrower.get() != "Teslim Al":
                self.status.set(1)
                self.lendingDate.config(state='normal')
                self.receiveDate.config(state='normal')
                self.receiveDate2(event=None)
            else:
                if len(self.lendingDate.get()) != 0:
                    self.receiveDate.config(state="normal")
                    t1 = self.receiveDate.get_date()
                    t2 = date.today()
                    self.receiveDate.delete(0, END)
                    t3 = str(t2).split("-")
                    t4 = str(t3[2] + "." + str(t3[1]) + "." + str(t3[0]))
                    self.receiveDate.insert(0, t4)
                    day = (t2-t1).days
                    if day > 0:
                        self.debt['text'] = day * 1
                    else:
                        self.debt['text'] = 0

                else:
                    messagebox.showerror("Hata", "Kitap ödünç verilmemiş.")
                    self.borrower.delete(0, END)
                    self.focus()
        else:
            self.status.set(0)
            self.lendingDate.delete(0, END)
            self.receiveDate.delete(0, END)
            self.lendingDate.config(state="disabled")
            self.receiveDate.config(state="disabled")


    def receiveDate2(self, event):
        a = self.lendingDate.get_date()
        y = a + timedelta(days=14)
        b = str(y).split("-")
        c = b[2] + "." + b[1] + "." + b[0]
        self.receiveDate.delete(0, END)
        self.receiveDate.insert(0, c)
        self.lendingDate.config(state="disabled")
        self.receiveDate.config(state="disabled")

    def save(self):
        sql = "INSERT INTO books (barcode, title, writer, status, shelf, borrower, lendingDate, receiveDate)" \
              " VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
        val = (self.barcode.get(), self.title.get(), self.writer.get(), self.status.get(),
               self.shelf.get(), self.borrower.get(), self.lendingDate.get(), self.receiveDate.get())
        con.execute(sql, val)
        con.commit()

        self.clear()

    def fetch(self):
        sql = "SELECT * FROM books WHERE barcode=?"
        val = (self.barcode.get(),)
        cursor.execute(sql, val)
        result = cursor.fetchall()

        for i in result:
            self.title.delete(0, END)
            self.title.insert(0, i[1])
            self.writer.delete(0, END)
            self.writer.insert(0, i[2])
            self.status.set(i[3])
            self.shelf.delete(0, END)
            self.shelf.insert(0, i[4])
            self.lendingDate.config(state="normal")
            self.lendingDate.delete(0, END)
            self.lendingDate.insert(0, i[6])
            self.lendingDate.config(state="disabled")
            self.receiveDate.config(state="normal")
            self.receiveDate.delete(0, END)
            self.receiveDate.insert(0, i[7])
            self.receiveDate.config(state="disabled")
            try:
                self.borrower.delete(0, END)
                self.borrower.insert(0, i[5])
            except TclError:
                pass
        self.reference = self.borrower.get()

    def update(self):
        if self.borrower.get() == "Teslim Al":
            self.status.set(0)
            self.lendingDate.config(state='normal')
            self.receiveDate.config(state='normal')
            self.lendingDate.delete(0, END)
            self.receiveDate.delete(0, END)
            self.borrower.delete(0, END)

            sql = "UPDATE books SET" \
                  " title=?, writer=?, status=?, shelf=?, borrower=?, lendingDate=?, receiveDate=? WHERE barcode=? "
            val = (self.title.get(), self.writer.get(), self.status.get(), self.shelf.get(), self.borrower.get(),
                   self.lendingDate.get(), self.receiveDate.get(), self.barcode.get())
            cursor.execute(sql, val)
            con.commit()

            sql = "SELECT * from members WHERE reference=%s"
            val = (self.reference,)
            mycursor.execute(sql, val)
            result = mycursor.fetchall()

            for i in result:
                self.exDebt = i[9]
            try:
                sql = "UPDATE members SET debt=%s WHERE reference=%s"
                val = (int(self.exDebt) + int(self.debt['text']), self.reference)
                mycursor.execute(sql, val)
                mydb.commit()
            except TypeError:
                sql = "UPDATE members SET debt=%s WHERE reference=%s"
                val = (0 + int(self.debt['text']), self.reference)
                mycursor.execute(sql, val)
                mydb.commit()

        else:
            sql = "UPDATE books SET" \
                  " title=?, writer=?, status=?, shelf=?, borrower=?, lendingDate=?, receiveDate=? WHERE barcode=? "
            val = (self.title.get(), self.writer.get(), self.status.get(), self.shelf.get(), self.borrower.get(),
                   self.lendingDate.get(), self.receiveDate.get(), self.barcode.get())
            cursor.execute(sql, val)
            con.commit()

        self.clear()

    def delete(self):
        sql = "DELETE FROM books WHERE barcode=?"
        val = (self.barcode.get(),)
        cursor.execute(sql, val)
        con.commit()
        self.clear()

    def clear(self):
        messagebox.showinfo("Başarılı", "İşlem Başarılı")
        self.barcode.delete(0, END)
        self.title.delete(0, END)
        self.writer.delete(0, END)
        self.status.set(0)
        self.borrower.delete(0, END)
        self.shelf.delete(0, END)
        self.lendingDate.config(state="normal")
        self.receiveDate.config(state="normal")
        self.lendingDate.delete(0, END)
        self.receiveDate.delete(0, END)
        self.lendingDate.config(state="disabled")
        self.receiveDate.config(state="disabled")
        self.debt['text'] = 0
        self.focus()


class BookCase(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.wm_geometry("600x400+400+100")
        self.wm_title("Kitaplık")
        self.wm_iconbitmap(default=r"C:\Users\erdem\Desktop\LibraryManagementSystem\Books.ico")

        style = ttk.Style()
        style.theme_use("clam")

        self.frame1 = Frame(self, bg="#f6eec9", width=600, height=400)
        self.frame1.pack()

        Label(self.frame1, text="KİTAPLIK", bg="#f6eec9", font=("Garamond", 15, "bold")).place(x=220)

        self.scroll = ttk.Scrollbar(self.frame1)
        self.scroll.place(x=529, y=50, height=300)

        self.tree = ttk.Treeview(self.frame1, yscrollcommand=self.scroll.set,
                                 columns=("column1", "column2", "column3", "column4"), show="headings")

        self.tree.heading("column1", text="Barkod")
        self.tree.heading("column2", text="Kitap")
        self.tree.heading("column3", text="Yazar")
        self.tree.heading("column4", text="Raf")

        self.tree.column("column1", width=120)
        self.tree.column("column2", width=120)
        self.tree.column("column3", width=120)
        self.tree.column("column4", width=120)

        self.tree.place(x=45, y=50, height=300)
        self.scroll.config(command=self.tree.yview)

        self.barcode_list = []
        self.book_list = []
        self.writer_list = []
        self.shelf_list = []

        cursor.execute("SELECT * FROM books")
        result = cursor.fetchall()
        for i in result:
            self.barcode_list.append(i[0])
            self.book_list.append(i[1])
            self.writer_list.append(i[2])
            self.shelf_list.append(i[4])

        self.bookcase_list = list(zip(self.barcode_list, self.book_list, self.writer_list, self.shelf_list))

        for i in self.bookcase_list:
            self.tree.insert("", END, values=(i[0], i[1], i[2], i[3]))

        Button(self.frame1, text="EXCEL", command=self.excel, bg="#fed39f",
               activebackground="#f6eec9", font=("Garamond", 15, "bold")).place(x=45, y=355, width=125)

        Button(self.frame1, text="PDF", command=self.pdf, bg="#fed39f",
               activebackground="#f6eec9", font=("Garamond", 15, "bold")).place(x=420, y=355, width=125)

    def excel(self):
        work_book = Workbook()
        page = work_book.active

        page.append(["Barkod", "Kitap", "Yazar", "Raf"])

        for i in self.bookcase_list:
            page.append(i)

        work_book.save("kitaplık.xlsx")
        os.startfile("kitaplık.xlsx")

    def pdf(self):
        data = [["Barkod", "Kitap", "Yazar", "Raf"]]
        for i in self.bookcase_list:
            data.append(list(i))

        pdf = FPDF()
        pdf.set_font("Arial", size=12)
        pdf.add_page()

        column_width = pdf.w / 4
        row_width = pdf.font_size

        for i in data:
            for j in i:
                pdf.cell(column_width, row_width*2, txt=j, border=1)
            pdf.ln(row_width*2)

        pdf.output("kitaplık.pdf")
        os.startfile("kitaplık.pdf")


if __name__ == "__main__":
    app = Library()
    app.mainloop()
