from tkinter import *
from tkinter import ttk
import mysql.connector

class CheckDriver:
    def __init__(self,window):
        self.window = window
        self.window.title("Drivers")
        self.window.geometry("300x300")
        self.window.resizable(False,False)

        self.driver_table = ttk.Treeview(self.window, columns=(
            'Driver Id', 'Name', 'Availability'), show='headings')

        self.driver_table.heading('Driver Id', text='Driver Id')
        self.driver_table.heading('Name', text='Name')
        self.driver_table.heading('Availability', text='Availability')

        self.driver_table.column('Driver Id', width=100)
        self.driver_table.column('Name', width=100)
        self.driver_table.column('Availability', width=90)

        self.driver_table.place(x=0, y=0, height=300, width=300)

        try:
            database = mysql.connector.connect(host="localhost",user="root",password="",database="taxibookingsystem")
            cursor = database.cursor()
            cursor.execute("SELECT * FROM drivers")
            rows = cursor.fetchall()
            for row in rows:
                self.driver_table.insert("", "end", values=(row[0], row[1], row[10]))

        except Exception as err:
            print(f"{err}")


if __name__ == '__main__':
    window = Tk()
    CheckDriver(window)
    window.mainloop()