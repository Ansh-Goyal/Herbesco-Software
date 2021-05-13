from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

def create():

    id = e_evntid.get()

    name = e_evntnme.get()

    date = e_evntdat.get()

    entries = e_evntentrys.get()

    inchrg_id = e_evntinchrgid.get()


    if id=='' or name=="" or date=="" or entries == '' or inchrg_id == '':
        MessageBox.showinfo("CREATE Status", "All Fields are required")
    else:
        con = mysql.connect(host="localhost", user="root", password="Galaxy@M87", database="Herbesco")
        cursor = con.cursor()
        cursor.execute("insert into Events values('{}', {}, '{}', {}, {})".format(name, id, date, entries, inchrg_id))
        cursor.execute("commit")

        e_evntid.delete(0, 'end')

        e_evntnme.delete(0, 'end')

        e_evntdat.delete(0, 'end')

        e_evntentrys.delete(0, 'end')

        e_evntinchrgid.delete(0, 'end')

        show()
        MessageBox.showinfo("Insert Status", "Inserted Successfully")
        con.close()

def delete():
    id = e_evntid.get()
    inid = e_evntinchrgid.get()
    if id=="" and inid == "":
        MessageBox.showinfo("Delete Status", "ID AND Incharge ID Needed")
        return 0
    else:
        con = mysql.connect(host="localhost", user="root", password="Galaxy@M87", database="Herbesco")
        cursor = con.cursor()
        cursor.execute("SELECT Evnt_Id, Evnt_Incharg_Id FROM Events;")
        rows = cursor.fetchall()

        for row in rows:
            if row[0] == int(id) and row[1] == int(inid):
                cursor.execute("DELETE FROM Events where Evnt_Id = {} and Evnt_Incharg_Id = {};".format(int(id), int(inid)))
                cursor.execute("commit")
                e_evntid.delete(0, 'end')

                e_evntnme.delete(0, 'end')

                e_evntdat.delete(0, 'end')

                e_evntentrys.delete(0, 'end')

                e_evntinchrgid.delete(0, 'end')
                show()
                MessageBox.showinfo("Delete Status", "Deleted Successful")
                con.close()
                return 0
            else:
                continue

        MessageBox.showinfo("Delete Status", "Incorrect ID OR Incharge ID")

        return 0

def update():

    id = e_evntid.get()

    name = e_evntnme.get()

    date = e_evntdat.get()

    entries = e_evntentrys.get()

    inchrg_id = e_evntinchrgid.get()


    if id == "" or name == "" or date == "" or entries == "" or inchrg_id == "":
        MessageBox.showinfo("Update Status", "All Fields are required")
    else:
        con = mysql.connect(host="localhost", user="root", password="Galaxy@M87", database="Herbesco")
        cursor = con.cursor()
##        try:
        
        cursor.execute("Update Events SET Evnt_Nme = '{}', Evnt_Dat = '{}', Num_Entries = {} where Evnt_Incharg_Id = {} and  Evnt_Id= {};".format(name, date, entries, inchrg_id, id))
        cursor.execute("commit")

        e_evntid.delete(0, 'end')

        e_evntnme.delete(0, 'end')

        e_evntdat.delete(0, 'end')

        e_evntentrys.delete(0, 'end')

        e_evntinchrgid.delete(0, 'end')
        show()
        MessageBox.showinfo("Update Status", "Updated Successfully")
        con.close()
##        except:
##            MessageBox.showinfo("Update Status", "CHECK ENTRIES!")
def get():
    id = e_evntid.get()

    name = e_evntnme.get()

    date = e_evntdat.get()

    entries = e_evntentrys.get()

    if id == "" :
        MessageBox.showinfo("Fetch Status", "ID Needed")
    else:
        con = mysql.connect(host="localhost", user="root", password="Galaxy@M87", database="Herbesco")
        cursor = con.cursor()
        cursor.execute("SELECT Evnt_Nme, Evnt_Dat, Num_Entries from Events where Evnt_Id = '{}'".format(id))
        rows = cursor.fetchall()

        for row in rows:
            e_evntnme.insert(0, row[0])
            e_evntdat.insert(0, row[1])
            e_evntentrys.insert(0, row[2])
        con.close()

def show():
    con = mysql.connect(host="localhost", user="root", password="Galaxy@M87", database="Herbesco")
    cursor = con.cursor()
    cursor.execute("select * from Events")
    rows = cursor.fetchall()

    lst.delete(0, lst.size())

    lst.insert(END, "Name | Date | Entries\n")
    lst.insert(END,"------------------------")
    lst.insert(END,"\n")

    for row in rows:
        insertData ="{}  | {} | {}\n".format(row[0], row[2], row[3])
        lst.insert(lst.size()+1, insertData)

    con.close()

def evnts_scrn():

    global e_evntid, e_evntdat, e_evntnme, e_evntentrys, e_evntinchrgid, lst

    evnt_scrn = Tk()
    evnt_scrn.geometry("600x300+300+300")
    evnt_scrn.title("Events Control!")

    evntid = Label(evnt_scrn, text="ID",font=("bold", 10))
    evntid.place(x=20, y=30)

    evntnme = Label(evnt_scrn, text="Name",font=("bold", 10))
    evntnme.place(x=20, y=60)

    evntdat = Label(evnt_scrn, text="DATE",font=("bold", 10))
    evntdat.place(x=20, y=90)

    evntentrys = Label(evnt_scrn, text="Entries",font=("bold", 10))
    evntentrys.place(x=20, y=120)

    evntinchrgid = Label(evnt_scrn, text="Incharge ID",font=("bold", 10))
    evntinchrgid.place(x=20, y=150)


    e_evntid = Entry(evnt_scrn)
    e_evntid.place(x=150, y=30)

    e_evntnme = Entry(evnt_scrn)
    e_evntnme.place(x=150, y=60)

    e_evntdat = Entry(evnt_scrn)
    e_evntdat.place(x=150, y=90)

    e_evntentrys = Entry(evnt_scrn)
    e_evntentrys.place(x=150, y=120)

    e_evntinchrgid = Entry(evnt_scrn)
    e_evntinchrgid.place(x=150, y=150)


    crt_evnt_button = Button(evnt_scrn, text="CREATE", font=("italic", 10), bg="white", command=create)
    crt_evnt_button.place(x=20, y=180)

    dlt_evnt_button = Button(evnt_scrn, text="DELETE", font=("italic", 10), bg="white", command=delete)
    dlt_evnt_button.place(x=130, y=180)

    updt_evnt_button = Button(evnt_scrn, text="UPDATE", font=("italic", 10), bg="white", command=update)
    updt_evnt_button.place(x=250, y=180)

    get_evnt_button = Button(evnt_scrn, text="GET", font=("italic", 10), bg="white", command=get)
    get_evnt_button.place(x=320, y=180)

    lst = Listbox(evnt_scrn)
    lst.place(x=400, y=30)
    show()

    evnt_scrn.mainloop()
