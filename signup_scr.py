from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

def signup_info():
    name = e_name.get()
    id =  e_id.get()
    paswrd = e_paswrd.get()
    ph_no = e_ph_no.get()
    adrs = e_adrs.get()

    if name == "" or id == None or paswrd == "" or ph_no == None or adrs == "":
        MessageBox.showinfo("Insert Status", "All Fields are required")
    else:
        con = mysql.connect(host="localhost", user="root", password="Galaxy@M87", database="Herbesco")
        cursor = con.cursor()
        cursor.execute("INSERT INTO Users_Info VALUES('{}', {}, '{}', {}, '{}');".format(name, id, paswrd, ph_no, adrs))
        cursor.execute("commit")

        e_name.delete(0, 'end')
        e_id.delete(0, 'end')
        e_paswrd.delete(0, 'end')
        e_ph_no.delete(0, 'end')
        e_adrs.delete(0, 'end')
        #show()
        MessageBox.showinfo("Insert Status", "Inserted Successfully")
        con.close()


def signup_scr():

    global e_name, e_id, e_ph_no, e_adrs, e_paswrd

    sig_scr = Tk()
    sig_scr.title("SIGNUP")

    Label(sig_scr, text = "ENTER YOUR DETAILS").grid(row = 0, columnspan = 3)

    # first input-field
    Label(sig_scr, text = "FULL NAME").grid(row = 1)
    e_name = Entry(sig_scr)
    e_name.grid(row = 1, column = 1)
    Label(sig_scr, text = "(max 30 charachters)").grid(row = 1, column = 2)

    # second input-field
    Label(sig_scr, text = "USER ID").grid(row = 2)
    e_id = Entry(sig_scr)
    e_id.grid(row = 2, column = 1)
    Label(sig_scr, text = "(max 30 charachters)").grid(row = 2, column = 2)

    # third input-field
    Label(sig_scr, text = "PASSWORD").grid(row = 3)
    e_paswrd = Entry(sig_scr)
    e_paswrd.grid(row = 3, column = 1)
    Label(sig_scr, text = "(max 30 charachters)").grid(row = 3, column = 2)

    # fourth input-field
    Label(sig_scr, text = "PHONE NUMBER").grid(row = 4)
    e_ph_no = Entry(sig_scr)
    e_ph_no.grid(row = 4, column = 1)
    Label(sig_scr, text = "10 digits").grid(row = 4, column = 2)

    # fifth input-field
    Label(sig_scr, text = "ADDRESS").grid(row = 5)
    e_adrs = Entry(sig_scr)
    e_adrs.grid(row = 5, column = 1)
    Label(sig_scr, text = "(max 30 charachters)").grid(row = 5, column = 2)


    signing_button = Button(sig_scr, text = "SIGN UP", fg = "blue", command = signup_info)
    signing_button.grid(columnspan = 3)



    sig_scr.mainloop()
