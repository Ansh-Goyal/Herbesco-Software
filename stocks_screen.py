from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
from plants_pie_plot import *

def increase():

    id = e_plnt_id.get()

    name = e_plnt_nme.get()

    qty_reqrd = e_qty_reqrd.get()

    qty_avlble = e_qty_avlble.get()


    if id=='' or name=="" or qty_reqrd == '' or qty_avlble == '':
        MessageBox.showinfo("INCREASE Status", "All Fields are required")
    else:
        con = mysql.connect(host="localhost", user="root", password="Galaxy@M87", database="Herbesco")
        cursor = con.cursor()
        cursor.execute("insert into Stocks values({}, '{}', {}, {})".format(id, name, qty_avlble, qty_reqrd))
        cursor.execute("commit")

        e_plnt_id.delete(0, 'end')

        e_plnt_nme.delete(0, 'end')

        e_qty_reqrd.delete(0, 'end')

        e_qty_avlble.delete(0, 'end')

        show()
        MessageBox.showinfo("INCREASE Status", "STOCK INCREASED Successfully")
        con.close()

def remove():
    id = e_plnt_id.get()
    if id=="":
        MessageBox.showinfo("REMOVE Status", "ID Needed")
        return 0
    else:
        con = mysql.connect(host="localhost", user="root", password="Galaxy@M87", database="Herbesco")
        cursor = con.cursor()
        cursor.execute("SELECT Plnt_Id FROM Stocks;")
        rows = cursor.fetchall()

        for row in rows:
            if int(row[0]) == int(id):
                cursor.execute("DELETE FROM Stocks where Plnt_Id = {}".format(int(id)))
                cursor.execute("commit")

                e_plnt_id.delete(0, 'end')

                e_plnt_nme.delete(0, 'end')

                e_qty_reqrd.delete(0, 'end')

                e_qty_avlble.delete(0, 'end')
                show()
                MessageBox.showinfo("REMOVE Status", "STOCK REMOVED Successfully")
                con.close()
                return 0
            else:
                continue

        MessageBox.showinfo("REMOVE Status", "ID Not Found!")

        return 0

def update():

    id = e_plnt_id.get()

    name = e_plnt_nme.get()

    qty_reqrd = e_qty_reqrd.get()

    qty_avlble = e_qty_avlble.get()


    if id == "" or name == "" or qty_reqrd == "" or qty_avlble == "":
        MessageBox.showinfo("Update Status", "All Fields are required")
    else:
        con = mysql.connect(host="localhost", user="root", password="Galaxy@M87", database="Herbesco")
        cursor = con.cursor()
        try:
            cursor.execute("Update Stocks SET plnt_nme = '{}', Qnty_Avlbl = '{}', Qnty_Reqrd = {} where Plnt_Id = '{}';".format(name, qty_avlble, qty_reqrd, id))
            cursor.execute("commit")

            e_plnt_id.delete(0, 'end')

            e_plnt_nme.delete(0, 'end')

            e_qty_reqrd.delete(0, 'end')

            e_qty_avlble.delete(0, 'end')
            show()
            MessageBox.showinfo("Update Status", "Updated Successfully")
            con.close()
        except:
            MessageBox.showinfo("Update Status", "CHECK ENTRIES!")
def get():

    id = e_plnt_id.get()

    if id == "" :
        MessageBox.showinfo("Fetch Status", "ID Needed")
    else:
        con = mysql.connect(host="localhost", user="root", password="Galaxy@M87", database="Herbesco")
        cursor = con.cursor()
        cursor.execute("SELECT plnt_nme, Qnty_Avlbl, Qnty_Reqrd from Stocks where Plnt_Id = '{}'".format(id))
        rows = cursor.fetchall()

        for row in rows:
            e_plnt_nme.insert(0, row[0])
            e_qty_avlble.insert(0, row[1])
            e_qty_reqrd.insert(0, row[2])
        con.close()

def show():
    con = mysql.connect(host="localhost", user="root", password="Galaxy@M87", database="Herbesco")
    cursor = con.cursor()
    cursor.execute("select * from Stocks")
    rows = cursor.fetchall()

    lst.delete(0, lst.size())

    lst.insert(END, "Name | Qnty_Avlbl | Qnty_Reqrd\n")
    lst.insert(END,"---------------------------------")
    lst.insert(END,"\n")

    for row in rows:
        insertData ="{}  | {} | {}\n".format(row[1], row[2], row[3])
        lst.insert(lst.size(), insertData)

    con.close()

def stocks_scrn():

    global e_plnt_id, e_plnt_nme, e_qty_reqrd, e_qty_avlble, lst

    plnt_scrn = Tk()
    plnt_scrn.geometry("600x300+300+300")
    plnt_scrn.title("Plants Stock Control!")

    plnt_id = Label(plnt_scrn, text="ID",font=("bold", 10))
    plnt_id.place(x=20, y=30)

    plnt_nme = Label(plnt_scrn, text="Name",font=("bold", 10))
    plnt_nme.place(x=20, y=60)

    qty_avlble = Label(plnt_scrn, text="Quantity Available",font=("bold", 10))
    qty_avlble.place(x=20, y=90)

    qty_reqrd = Label(plnt_scrn, text="Quantity Required",font=("bold", 10))
    qty_reqrd.place(x=20, y=120)


    e_plnt_id = Entry(plnt_scrn)
    e_plnt_id.place(x=150, y=30)

    e_plnt_nme = Entry(plnt_scrn)
    e_plnt_nme.place(x=150, y=60)

    e_qty_avlble = Entry(plnt_scrn)
    e_qty_avlble.place(x=150, y=90)

    e_qty_reqrd = Entry(plnt_scrn)
    e_qty_reqrd.place(x=150, y=120)


    ad_stock_button = Button(plnt_scrn, text="INCREASE STOCK", font=("italic", 10), bg="white", command=increase)
    ad_stock_button.place(x=20, y=180)

    rmv_stock_button = Button(plnt_scrn, text="REMOVE STOCK", font=("italic", 10), bg="white", command=remove)
    rmv_stock_button.place(x=130, y=180)

    updt_Stock_button = Button(plnt_scrn, text="UPDATE", font=("italic", 10), bg="white", command=update)
    updt_Stock_button.place(x=250, y=180)

    get_evnt_button = Button(plnt_scrn, text="GET", font=("italic", 10), bg="white", command=get)
    get_evnt_button.place(x=320, y=180)

    pie_show_button = Button(plnt_scrn, text="PLOT", font=("italic", 10), bg="BLUE", command=plot_pie)
    pie_show_button.place(x=450, y=220)
    lst = Listbox(plnt_scrn)
    lst.place(x=400, y=30)
    show()

    plnt_scrn.mainloop()
