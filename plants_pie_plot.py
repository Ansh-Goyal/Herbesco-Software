import matplotlib.pyplot as plt
import mysql.connector as mysql


def plot_pie():
    plants = []
    qty_avlbl = []
    colours = ['red', 'green', 'blue', 'yellow', 'cyan', 'violet', 'pink', 'lightcoral', 'gold', 'yellowgreen', 'black' , 'brown']

    con = mysql.connect(host="localhost", user="root", password="Galaxy@M87", database="Herbesco")
    cursor = con.cursor()
    cursor.execute("SELECT Plnt_Nme, Qnty_Avlbl FROM STOCKS")
    rows = cursor.fetchall()

    try:
        for row in rows:
            plants.append(str(row[0]))
            qty_avlbl.append(int(row[1]))
        plt.pie(qty_avlbl, labels=plants, colors=colours[0:len(qty_avlbl)])
        plt.title("PLANTS ON THE BASIS OF QUANTITY AVAILABLE")
        plt.show()
    except:
        print("Empty")
