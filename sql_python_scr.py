from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

def insert():

    id = e_id.get()
    name = e_name.get()
    phone = e_phone.get()
    if id=="" or name=="" or phone=="":
        MessageBox.showinfo("Insert Status", "All Fields are required")
    else:
        con = mysql.connect(host="localhost", user="root", password="Galaxy@M87", database="Mysql_Python")
        cursor = con.cursor()
        cursor.execute("insert into students values('{}', '{}', '{}')".format(id, name, phone))
        cursor.execute("commit")

        e_id.delete(0, 'end')
        e_name.delete(0, 'end')
        e_phone.delete(0, 'end')
        show()
        MessageBox.showinfo("Insert Status", "Inserted Successfully")
        con.close()

def delete():
    if e_id.get()=="":
        MessageBox.showinfo("Delete Status", "ID Needed")
    else:
        con = mysql.connect(host="localhost", user="root", password="Galaxy@M87", database="Mysql_Python")
        cursor = con.cursor()
        cursor.execute("delete from students where id = '{}'".format(e_id.get()))
        cursor.execute("commit")

        e_id.delete(0, 'end')
        e_name.delete(0, 'end')
        e_phone.delete(0, 'end')
        show()
        MessageBox.showinfo("Delete Status", "Deleted Successfully")
        con.close()

def update():
    id = e_id.get()
    name = e_name.get()
    phone = e_phone.get()

    if id=="" or name=="" or phone=="":
        MessageBox.showinfo("Update Status", "All Fields are required")
    else:
        con = mysql.connect(host="localhost", user="root", password="Galaxy@M87", database="Mysql_Python")
        cursor = con.cursor()
        cursor.execute("Update students SET name = '{}', phone = '{}' where id = '{}';".format(name, phone, id))
        cursor.execute("commit")

        e_id.delete(0, 'end')
        e_name.delete(0, 'end')
        e_phone.delete(0, 'end')
        show()
        MessageBox.showinfo("Update Status", "Updated Successfully")
        con.close()

def get():
    if e_id.get()=="":
        MessageBox.showinfo("Fetch Status", "ID Needed")
    else:
        con = mysql.connect(host="localhost", user="root", password="Galaxy@M87", database="Mysql_Python")
        cursor = con.cursor()
        cursor.execute("SELECT * from students where id = '{}'".format(e_id.get()))
        rows = cursor.fetchall()

        for row in rows:
            e_name.insert(0, row[1])
            e_phone.insert(0, row[2])

        con.close()

def show():
    con = mysql.connect(host="localhost", user="root", password="Galaxy@M87", database="Mysql_Python")
    cursor = con.cursor()
    cursor.execute("select * from students")
    rows = cursor.fetchall()
    list.delete(0, list.size())
    for row in rows:
        insertData = str(row[0])+ '       '+ str(row[1])
        list.insert(list.size()+1, insertData)

    con.close()


root = Tk()
root.geometry("600x300")
root.title("Python + Tkinter + MySql")

id = Label(root, text="Enter ID",font=("bold", 10))
id.place(x=20, y=30)

name = Label(root, text="Enter Name",font=("bold", 10))
name.place(x=20, y=60)

phone = Label(root, text="Enter Phone",font=("bold", 10))
phone.place(x=20, y=90)

e_id = Entry()
e_id.place(x=150, y=30)

e_name = Entry()
e_name.place(x=150, y=60)

e_phone = Entry()
e_phone.place(x=150, y=90)

insert = Button(root, text="Insert", font=("italic", 10), bg="white", command=insert)
insert.place(x=20, y=140)

delete = Button(root, text="Delete", font=("italic", 10), bg="white", command=delete)
delete.place(x=70, y=140)

update = Button(root, text="Update", font=("italic", 10), bg="white", command=update)
update.place(x=130, y=140)

get = Button(root, text="Get", font=("italic", 10), bg="white", command=get)
get.place(x=180, y=140)

list = Listbox(root)
list.place(x=400, y=30)
show()

root.mainloop()
