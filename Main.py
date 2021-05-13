from tkinter import *
from signup_scr import *
from login_scr import *


def wlcm_scr():

    main_scr = Tk()
    main_scr.geometry("600x120+300+300")
    main_scr.configure(bg='white')
    main_scr.title("WELCOME")

    Label(main_scr, text = "GO - HERBESCO", bg='cyan').place(x=250, y=10)
    Label(main_scr, text = "WELCOME TO THE SOFTWARE!", bg='cyan').place(x=200, y=40)

    login_button = Button(main_scr, text = "LOGIN", fg = "blue",command = login_scr)
    login_button.place(x=100, y = 80)

    signup_button = Button(main_scr, text = "SIGN UP", fg = "red",command = signup_scr)
    signup_button.place(x=450, y = 80)


    main_scr.mainloop()


if __name__ == '__main__':
    wlcm_scr()
