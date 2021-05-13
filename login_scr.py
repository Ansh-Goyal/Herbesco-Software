from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
from events_screen import *
from stocks_screen import *
def login_scr():

    global e_id, e_paswrd

    log_scr = Tk()
    log_scr.title("LOGIN")
    log_scr.geometry("300x100+450+400")
    # first input-field

    Label(log_scr, text = "UserID").grid(row = 0)


    e_id = Entry(log_scr)
    e_id.grid(row = 0, column = 1)

    # second input-field

    Label(log_scr, text = "Password").grid(row = 1)

    e_paswrd = Entry(log_scr)
    e_paswrd.grid(row = 1, column = 1)

    Checkbutton(log_scr, text = "Keep Me Logged In").grid(columnspan = 2)

    logging_button = Button(log_scr, text = "LOGIN", fg = "Blue", command = check_user)
    logging_button.grid(columnspan = 2)

    log_scr.mainloop()

def check_user():
    id =  e_id.get()
    paswrd = e_paswrd.get()


    if id == None or paswrd == "":
        MessageBox.showinfo("Login Status", "All Fields are required")
        return 0

    else:
##        try:
        con = mysql.connect(host="localhost", user="root", password="Galaxy@M87", database="Herbesco")
        cursor = con.cursor()
        cursor.execute("SELECT User_Id, Usr_Pas FROM Users_Info;")
        rows = cursor.fetchall()

        for row in rows:
            if row[0] == int(id) and row[1] == str(paswrd):
                MessageBox.showinfo("Login Status", "Login Successful")
                con.close()
                return user_scr()
                print(1)

            else:
                continue
        else:
            e_id.delete(0, 'end')
            e_paswrd.delete(0, 'end')
            print(2)
            MessageBox.showinfo("Login Status", "INVALID USERID OR PASSWORD")
            con.close()
            return 0
##        except:
##            print(3)
##            MessageBox.showinfo("Login Status", "INVALID USERID OR PASSWORD")



def user_scr():

    #LOCAL VARIABLES :- usr_scr,
    con = mysql.connect(host="localhost", user="root", password="Galaxy@M87", database="Herbesco")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM Users_Info where User_Id = {};".format(e_id.get()))
    user_details = cursor.fetchone()


    usr_scr = Tk()
    usr_scr.geometry("200x100+450+450")
    usr_scr.title("USER SCREEN")

    Label(usr_scr, text = "HELLO {}!".format(user_details[0]).upper()).grid(row = 0, columnspan = 3)

    evnts_button = Button(usr_scr, text = "EVENTS", command = evnts_scrn)
    evnts_button.grid(row = 1, columnspan = 3)

    stc_button = Button(usr_scr, text = "STOCK", command = stocks_scrn)
    stc_button.grid(row = 2, columnspan = 3)

    mmbrs_button = Button(usr_scr, text = "MEMBERS", command = usr_scr.destroy)
    mmbrs_button.grid(row = 3, columnspan = 3)

    usr_scr.mainloop()


# def events_scr():
#     evnt_scr = Tk()
#     evnt_scr.title("EVENTS HELP")
#
#     Label(evnt_scr, text = "ENTER YOUR DETAILS").grid(row = 0, columnspan = 3)
#
#     crt_evnt_button = Button(evnt_scr, text = "CREATE EVENT", bg = "blue", command = create_event_scr)
#     crt_evnt_button.grid(row = 2, columnspan = 3)
#
#     cur_evnts_button = Button(evnt_scr, text = "CURRENT EVENTS", bg = "green", command = evnt_scr.destroy)
#     cur_evnts_button.grid(row = 3, columnspan = 3)
#
#     evnt_scr.mainloop()

# def create_event_scr():
#
#     crt_evnt_scr = Tk()
#     crt_evnt_scr.title("CREATE EVENTS")
#
#     Label(crt_evnt_scr, text = "ENTER YOUR DETAILS").grid(row = 0, columnspan = 3)
#
#     # first input-field
#     Label(crt_evnt_scr, text = "EVENT NAME").grid(row = 1)
#     evnt_nme = Entry(crt_evnt_scr).grid(row = 1, column = 1)
#     Label(crt_evnt_scr, text = "(max 30 charachters)").grid(row = 1, column = 2)
#
#     # second input-field
#     Label(crt_evnt_scr, text = "EVENT ID").grid(row = 2)
#     evnt_id = Entry(crt_evnt_scr).grid(row = 2, column = 1)
#     Label(crt_evnt_scr, text = "(max 30 charachters)").grid(row = 2, column = 2)
#
#     # third input-field
#     Label(crt_evnt_scr, text = "EVENT DATE").grid(row = 3)
#     evnt_dt = Entry(crt_evnt_scr).grid(row = 3, column = 1)
#     Label(crt_evnt_scr, text = "(YYYY-MM-DD)").grid(row = 3, column = 2)
#
#
#
#
#     create_button = Button(crt_evnt_scr, text = "SIGN UP", fg = "blue", bg = "cyan", command = crt_evnt_scr.destroy)
#     create_button.grid(columnspan = 3)
#
#     crt_evnt_scr.mainloop()

# def current_events_scr():
#
#     cur_evnt_scr = Tk()
#     cur_evnt_scr.title("EVENTS DETAILS")
