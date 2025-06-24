from tkinter import *
from tkinter import ttk
import cx_Oracle
import datetime

from tkinter import messagebox

class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("LIBRARY MANAGEMENT SYSTEM")
        self.root.geometry("1500x800")

        self.mem=StringVar()
        self.libno=StringVar()
        self.sname=StringVar()
        self.branch=StringVar()
        self.rollno=StringVar()

        self.bname=StringVar()
        self.author=StringVar()
        self.noofbooks=StringVar()

        self.bookid=StringVar()
        self.issuedate=StringVar()
        self.returndate=StringVar()

        self.search=StringVar()

        #-----titleframe-----
        lbltitle=Label(self.root,bg="grey",fg="black",text="LIBRARY MANAGEMENT SYSTEM",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)

        #-----buttonframe----
        framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="grey")
        framebutton.place(x=0,y=130,width=250,height=650)

        #in button frame we should add headings like addmember,etc...
        addmember=Button(framebutton,bg="white",fg="black",text="ADD MEMBER",command=self.addmember,font=('aril',12,"bold"),width=18)
        addmember.grid(row=0,column=0,pady=8)

        addbook=Button(framebutton,bg="white",fg="black",text="ADD BOOK",command=self.addbook,font=('aril',12,"bold"),width=18)
        addbook.grid(row=1,column=0,pady=8)

        issuebook=Button(framebutton,bg="white",fg="black",text="ISSUE BOOK",command=self.issuebook,font=('aril',12,"bold"),width=18)
        issuebook.grid(row=2,column=0,pady=8)

        returnbook=Button(framebutton,bg="white",fg="black",text="RETURN BOOK",command=self.returnbook,font=('aril',12,"bold"),width=18)
        returnbook.grid(row=3,column=0,pady=8)

        showbooks=Button(framebutton,bg="white",fg="black",text="SHOW BOOKS",command=self.showbooks,font=('aril',12,"bold"),width=18)
        showbooks.grid(row=4,column=0,pady=8)

        #----informationframe---
        self.frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="grey")
        self.frame.place(x=250,y=130,width=1275,height=650)

        #in information frame we should add memberdetails
    def addmember(self):
        for item in self.frame.winfo_children():
            item.destroy()
        
        lblmember=Label(self.frame,bg="grey",fg="black",text="MEMBER DETAILS",font=("times new roman",20,"bold"),padx=10,pady=10)
        lblmember.grid(row=0,column=1,sticky="nsew")

        membertype=Label(self.frame,bg="grey",fg="black",text="MEMBER TYPE",font=("aril",12,"bold"),padx=10,pady=10)
        membertype.grid(row=2,column=0,sticky="nsew")

        commember=ttk.Combobox(self.frame,textvariable=self.mem,font=("aril",12,"bold"),state="readonly",width=25)
        commember["values"]=("Admin","Student","Teaching Staff")
        commember.grid(row=2,column=1,sticky="nsew")

        libraryno=Label(self.frame,bg="grey",fg="black",text="LIBRARY NO:",font=("aril",12,"bold"),padx=10,pady=10)
        libraryno.grid(row=3,column=0,sticky="nsew")
        txtlibraryno=Entry(self.frame,fg="black",textvariable=self.libno,font=("aril",12,"bold"),width=27)
        txtlibraryno.grid(row=3,column=1,sticky="nsew")

        sname=Label(self.frame,bg="grey",fg="black",text="SNAME:",font=("aril",12,"bold"),padx=10,pady=10)
        sname.grid(row=4,column=0,sticky="nsew")
        txtsname=Entry(self.frame,fg="black",textvariable=self.sname,font=("aril",12,"bold"),width=27)
        txtsname.grid(row=4,column=1,sticky="nsew")

        branch=Label(self.frame,bg="grey",fg="black",text="BRANCH:",font=("aril",12,"bold"),padx=10,pady=10)
        branch.grid(row=5,column=0,sticky="nsew")

        commember=ttk.Combobox(self.frame,textvariable=self.branch,font=("aril",12,"bold"),state="readonly",width=25)
        commember["values"]=("CSE","ECE","MECH","CIVIL","AIML");
        commember.grid(row=5,column=1,sticky="nsew")

        rollno=Label(self.frame,bg="grey",fg="black",text="ROLL NO:",font=("aril",12,"bold"),padx=10,pady=10)
        rollno.grid(row=6,column=0,sticky="nsew")
        txtrollno=Entry(self.frame,fg="black",textvariable=self.rollno,font=("aril",12,"bold"),width=27)
        txtrollno.grid(row=6,column=1,sticky="nsew")

        btnadd=Button(self.frame,bg="pink",fg="black",command=self.addmemberdb,text="ADD",font=("aril",12,"bold"),width=18)
        btnadd.grid(row=9,column=1,pady=2)

    def addmemberdb(self):
        con=cx_Oracle.connect('scott/tiger@localhost/orcl')
        cursor=con.cursor()
        cursor.execute("insert into addmember values('%s','%s','%s','%s','%s')"%(self.mem.get(),
                                                                                 self.libno.get(),
                                                                                 self.sname.get(),
                                                                                 self.branch.get(),
                                                                                 self.rollno.get()));
        con.commit()
        messagebox.showinfo("SUCCESS","MEMBER HAS BEEN INSERTED SUCCESSFULLY")
        self.mem.set("")
        self.libno.set("")
        self.sname.set("")
        self.branch.set("")
        self.rollno.set("")

     
    def addbook(self):
        for item  in self.frame.winfo_children():
            item.destroy()

        lblbook=Label(self.frame,bg="grey",fg="black",text="BOOK DETAILS",font=("times new roman",20,"bold"),padx=10,pady=10)
        lblbook.grid(row=0,column=1,sticky="nsew")

        bookname=Label(self.frame,bg="grey",fg="black",text="BOOK NAME:",font=("aril",12,"bold"),padx=2,pady=8)
        bookname.grid(row=2,column=0,sticky="nsew")
        txtbookname=Entry(self.frame,fg="black",textvariable=self.bname,font=("aril",12,"bold"),width=27)
        txtbookname.grid(row=2,column=1,sticky="nsew")

        author=Label(self.frame,bg="grey",fg="black",text="AUTHOR NAME:",font=("aril",12,"bold"),padx=2,pady=8)
        author.grid(row=3,column=0,sticky="nsew")
        txtauthor=Entry(self.frame,fg="black",textvariable=self.author,font=("aril",12,"bold"),width=27)
        txtauthor.grid(row=3,column=1,sticky="nsew")

        noofbooks=Label(self.frame,bg="grey",fg="black",text="NO OF BOOKS:",font=("aril",12,"bold"),padx=2,pady=8)
        noofbooks.grid(row=4,column=0,sticky="nsew")
        txtnoofbooks=Entry(self.frame,fg="black",textvariable=self.noofbooks,font=("aril",12,"bold"),width=27)
        txtnoofbooks.grid(row=4,column=1,sticky="nsew")

        btnaddbook=Button(self.frame,bg="pink",fg="black",command=self.addbookdb,text="ADD BOOK",font=("aril",12,"bold"),width=18)
        btnaddbook.grid(row=6,column=1,pady=2)

    def addbookdb(self):
        con=cx_Oracle.connect('scott/tiger@localhost/orcl')
        cursor=con.cursor()
        cursor.execute("insert into addbook values('%s','%s','%s')"%(self.bname.get(),
                                                                     self.author.get(),
                                                                     self.noofbooks.get()));
        con.commit()
        messagebox.showinfo("SUCCESS","BOOK HAS BEEN INSERTED SUCCESSFULLY")
        self.bname.set("")
        self.author.set("")
        self.noofbooks.set("")                                                                       

    def issuebook(self):
        for item  in self.frame.winfo_children():
            item.destroy()

        con=cx_Oracle.connect("scott/tiger@localhost/orcl")
        cursor=con.cursor()
        cursor.execute("select *from addbook")
        data=cursor.fetchall()
        books=[]
        for ele in data:
            if ele[0] not in books:
                books.append(ele[0])

            def author(even=""):
                con=cx_Oracle.connect('scott/tiger@localhost/orcl')
                cursor=con.cursor()
                cursor.execute("select *from addbook where bname='%s'"%(self.bname.get()))
                data=cursor.fetchall()
                author=[]
                for ele in data:
                    author.append(ele[1])

                commember1["values"]=author

        lblissuebook=Label(self.frame,bg="grey",fg="black",text="ISSUE BOOK DETAILS",font=("times new roman",20,"bold"),padx=10,pady=10)
        lblissuebook.grid(row=0,column=1,sticky="nsew")

        bookid=Label(self.frame,bg="grey",fg="black",text="BOOK ID:",font=("aril",12,"bold"),padx=2,pady=8)
        bookid.grid(row=2,column=0,sticky="nsew")
        txtbookid=Entry(self.frame,fg="black",textvariable=self.bookid,font=("aril",12,"bold"),width=27)
        txtbookid.grid(row=2,column=1,sticky="nsew")

        booktitle=Label(self.frame,bg="grey",fg="black",text="BOOK TITLE:",font=("aril",12,"bold"),padx=10,pady=10)
        booktitle.grid(row=3,column=0,sticky="nsew")

        commember=ttk.Combobox(self.frame,textvariable=self.bname,font=("aril",12,"bold"),width=25)
        
        commember.bind("<<ComboboxSelected>>",author)
        commember["values"]=books
        commember.grid(row=3,column=1,sticky="nsew")


        author=Label(self.frame,bg="grey",fg="black",text="AUTHOR:",font=("aril",12,"bold"),padx=10,pady=10)
        author.grid(row=4,column=0,sticky="nsew")

        commember1=ttk.Combobox(self.frame,textvariable=self.author,font=("aril",12,"bold"),width=25)
        

        commember1.grid(row=4,column=1,sticky="nsew")

        name=Label(self.frame,bg="grey",fg="black",text="NAME:",font=("aril",12,"bold"),padx=2,pady=8)
        name.grid(row=5,column=0,sticky="nsew")
        txtname=Entry(self.frame,fg="black",textvariable=self.sname,font=("aril",12,"bold"),width=27)
        txtname.grid(row=5,column=1,sticky="nsew")

        number=Label(self.frame,bg="grey",fg="black",text="NUMBER:",font=("aril",12,"bold"),padx=2,pady=8)
        number.grid(row=6,column=0,sticky="nsew")
        txtnumber=Entry(self.frame,fg="black",textvariable=self.rollno,font=("aril",12,"bold"),width=27)
        txtnumber.grid(row=6,column=1,sticky="nsew")

        d1=datetime.datetime.today()
        self.issuedate.set(d1.strftime("%d-%m-%y"))
        d2=datetime.timedelta(days=15)
        d3=d2+d1
        self.returndate.set(d3.strftime("%d-%m-%y"))

        issuedate=Label(self.frame,bg="grey",fg="black",text="ISSUE DATE:",font=("aril",12,"bold"),padx=2,pady=8)
        issuedate.grid(row=7,column=0,sticky="nsew")
        txtissuedate=Entry(self.frame,fg="black",textvariable=self.issuedate,font=("aril",12,"bold"),width=27)
        txtissuedate.grid(row=7,column=1,sticky="nsew")

        returndate=Label(self.frame,bg="grey",fg="black",text="RETURN DATE:",font=("aril",12,"bold"),padx=2,pady=8)
        returndate.grid(row=8,column=0,sticky="nsew")
        txtreturndate=Entry(self.frame,fg="black",textvariable=self.returndate,font=("aril",12,"bold"),width=27)
        txtreturndate.grid(row=8,column=1,sticky="nsew")

        btnissuebook=Button(self.frame,bg="pink",fg="black",command=self.issuebookdb,text="ISSUE BOOK",font=("aril",12,"bold"),width=18)
        btnissuebook.grid(row=9,column=1,pady=2)

    def issuebookdb(self):
        con=cx_Oracle.connect('scott/tiger@localhost/orcl')
        cursor=con.cursor()
        cursor.execute("insert into issuebook values('%s','%s','%s','%s','%s','%s','%s')"%(self.bookid.get(),
                                                                                           self.bname.get(),
                                                                                           self.author.get(),
                                                                                           self.sname.get(),
                                                                                           self.rollno.get(),
                                                                                           self.issuedate.get(),
                                                                                           self.returndate.get()));

        cursor.execute("update addbook set noofbooks=noofbooks-1 where bname='%s' and author='%s'"%(self.bname.get(),
                                                                                                    self.author.get()));
        con.commit()
        messagebox.showinfo("SUCCESS","BOOK HAS BEEN ISSUED SUCCESSFULLY")
        self.bookid.set("")
        self.bname.set("")
        self.author.set("")
        self.sname.set("")
        self.rollno.set("")
        self.issuedate.set("")
        self.returndate.set("")

    def returnbook(self):
        for item  in self.frame.winfo_children():
            item.destroy()


        lblreturnbook=Label(self.frame,bg="grey",fg="black",text="RETURN BOOK",font=("times new roman",20,"bold"),padx=10,pady=10)
        lblreturnbook.grid(row=0,column=1,sticky="nsew")

    
        def search(even=""):
            con=cx_Oracle.connect('scott/tiger@localhost/orcl')
            cursor=con.cursor()
            cursor.execute("select *from issuebook where bookid='%s'"%(self.bookid.get()))
            data=cursor.fetchone()
            s1=""
            if data==None:
                messagebox.showerror("ERROR","There is no book on this {}".format(self.bookid.get()))
            else:
                self.bname.set(data[1])
                self.author.set(data[2])
                self.sname.set(data[3])
                self.rollno.set(data[4])
                self.issuedate.set(data[5])
                self.returndate.set(data[6])


        bookid=Label(self.frame,bg="grey",fg="black",text="BOOK ID:",font=("aril",12,"bold"),padx=2,pady=8)
        bookid.grid(row=2,column=0,sticky="nsew")
        txtbookid=Entry(self.frame,fg="black",textvariable=self.bookid,font=("aril",12,"bold"),width=27)
        txtbookid.grid(row=2,column=1,sticky="nsew")

        btnsearch=Button(self.frame,bg="pink",fg="black",command=search,text="SEARCH",font=("aril",12,"bold"),width=10)
        btnsearch.grid(row=2,column=3,pady=2)

        booktitle=Label(self.frame,bg="grey",fg="black",text="BOOK TITLE:",font=("aril",12,"bold"),padx=10,pady=10)
        booktitle.grid(row=3,column=0,sticky="nsew")
        txtbooktitle=Entry(self.frame,fg="black",textvariable=self.bname,font=("aril",12,"bold"),width=27)
        txtbooktitle.grid(row=3,column=1,sticky="nsew")

        
        author=Label(self.frame,bg="grey",fg="black",text="AUTHOR:",font=("aril",12,"bold"),padx=10,pady=10)
        author.grid(row=4,column=0,sticky="nsew")
        txtauthor=Entry(self.frame,fg="black",textvariable=self.author,font=("aril",12,"bold"),width=27)
        txtauthor.grid(row=4,column=1,sticky="nsew")

        name=Label(self.frame,bg="grey",fg="black",text="NAME:",font=("aril",12,"bold"),padx=2,pady=8)
        name.grid(row=5,column=0,sticky="nsew")
        txtname=Entry(self.frame,fg="black",textvariable=self.sname,font=("aril",12,"bold"),width=27)
        txtname.grid(row=5,column=1,sticky="nsew")
        
        number=Label(self.frame,bg="grey",fg="black",text="NUMBER:",font=("aril",12,"bold"),padx=2,pady=8)
        number.grid(row=6,column=0,sticky="nsew")
        txtnumber=Entry(self.frame,fg="black",textvariable=self.rollno,font=("aril",12,"bold"),width=27)
        txtnumber.grid(row=6,column=1,sticky="nsew")

        issuedate=Label(self.frame,bg="grey",fg="black",text="ISSUE DATE:",font=("aril",12,"bold"),padx=2,pady=8)
        issuedate.grid(row=7,column=0,sticky="nsew")
        txtissuedate=Entry(self.frame,fg="black",textvariable=self.issuedate,font=("aril",12,"bold"),width=27)
        txtissuedate.grid(row=7,column=1,sticky="nsew")

        returndate=Label(self.frame,bg="grey",fg="black",text="RETURN DATE:",font=("aril",12,"bold"),padx=2,pady=8)
        returndate.grid(row=8,column=0,sticky="nsew")
        txtreturndate=Entry(self.frame,fg="black",textvariable=self.returndate,font=("aril",12,"bold"),width=27)
        txtreturndate.grid(row=8,column=1,sticky="nsew")

        btnreturnbook=Button(self.frame,bg="pink",fg="black",command=self.returnbookdb,text="RETURN BOOK",font=("aril",12,"bold"),width=18)
        btnreturnbook.grid(row=9,column=1,pady=2)

    def returnbookdb(self):
        con=cx_Oracle.connect('scott/tiger@localhost/orcl')
        cursor=con.cursor()
        cursor.execute("update addbook set noofbooks=noofbooks+1 where bname='%s' and author='%s'"%(self.bname.get(),
                                                                                                    self.author.get()));
        cursor.execute("delete from issuebook where bookid='%s'"%(self.bookid.get()));
        messagebox.showinfo("SUCCESS","RETURNED THE BOOK SUCCESSFULLY")
        self.bookid.set("")
        self.bname.set("")
        self.author.set("")
        self.sname.set("")
        self.rollno.set("")
        self.issuedate.set("")
        self.returndate.set("")
        con.commit()




    def showbooks(self):
        for item in self.frame.winfo_children():
            item.destroy()


        def search(even=""):
            con=cx_Oracle.connect('scott/tiger@localhost/orcl')
            cursor=con.cursor()
            cursor.execute("select *from issuebook where bookid='%s'"%(self.search.get()))
            rows=cursor.fetchall()
            update(rows)
            con.commit()
            con.close()
            
        frame1=LabelFrame(self.frame,bg="grey",fg="black",text="search",bd=15,relief=RIDGE,font=("aril",12,"bold"),padx=2,pady=6)
        frame1.place(x=0,y=5,width=1220,height=95)

        booknum=Label(frame1,bg="grey",fg="black",text="BOOK NUM:",font=("aril",12,"bold"),padx=2,pady=6)
        booknum.grid(row=0,column=0,sticky=W)
        txtbooknum=Entry(frame1,fg="black",text=self.search,font=("aril",12,"bold"),width=27)
        txtbooknum.grid(row=0,column=1,sticky="nsew")
     
        btnsearch=Button(frame1,bg="pink",fg="black",command=search,text="SEARCH",font=("aril",12,"bold"),width=10)
        btnsearch.grid(row=0,column=2,pady=8)

        frame2=LabelFrame(self.frame,bg="grey",fg="black",text="Table Data",bd=12,relief=RIDGE,font=("aril",12,"bold"),padx=2,pady=6)
        frame2.place(x=0,y=100,width=1220,height=520)

        table=ttk.Treeview(frame2,column=("bid","bname","author","num","name","issuedate","returndate"),show="headings")
        table.column("bid",anchor="center",width=100)
        table.heading("bid",text="BOOK ID")
        table.column("bname",anchor="center",width=100)
        table.heading("bname",text="BOOK NAME")
        table.column("author",anchor="center",width=100)
        table.heading("author",text="AUTHOR")
        table.column("num",anchor="center",width=100)
        table.heading("num",text="NUMBER")
        table.column("name",anchor="center",width=100)
        table.heading("name",text="NAME")
        table.column("issuedate",anchor="center",width=100)
        table.heading("issuedate",text="ISSUE DATE")
        table.column("returndate",anchor="center",width=100)
        table.heading("returndate",text="RETURN DATE")
        table.pack()


        def update(rows):
            table.delete(*table.get_children())
            for i in rows:
                table.insert("",END,values=i)


        con=cx_Oracle.connect('scott/tiger@localhost/orcl')
        cursor=con.cursor()
        cursor.execute("select *from issuebook")
        rows=cursor.fetchall()
        update(rows)
        con.commit()
        con.close()


root=Tk()
l=LibraryManagementSystem(root)
root.mainloop()