from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import Global

class AdminDashboard:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1450x800")
        self.root.title("Admin Dashboard")

        # Header
        header_frame = Frame(self.root, bg="#3498db")
        header_frame.pack(side="top", fill="x")

        header_label = Label(header_frame, text="Admin Dashboard", font=('Helvetica', 18), bg="#3498db", fg="white")
        header_label.pack(pady=22)

        # Create a Treeview to display bookings
        self.treeview_frame = Frame(self.root)
        self.treeview_frame.place(x=20, y=80)

        # Style for Treeview
        style = ttk.Style()
        style.configure("Treeview.Heading", font=('Helvetica', 12))
        style.configure("Treeview", font=('Helvetica', 10), rowheight=25)

        # Treeview columns
        self.bookings_tree = ttk.Treeview(self.treeview_frame, columns=("Booking_id", "Pickup_Address", "Dropoff_Address", "Date", "Time", "Booking_Status", "Driver_id"), show="headings")
        self.bookings_tree.heading("Booking_id", text="Booking ID")
        self.bookings_tree.heading("Pickup_Address", text="Pickup Address")
        self.bookings_tree.heading("Dropoff_Address", text="Dropoff Address")
        self.bookings_tree.heading("Date", text="Date")
        self.bookings_tree.heading("Time", text="Time")
        self.bookings_tree.heading("Booking_Status", text="Booking Status")
        self.bookings_tree.heading("Driver_id", text="Driver ID")
        self.bookings_tree.pack()
        self.bookings_tree.bind("<<TreeviewSelect>>", self.selectedRow)

        # Load bookings into Treeview
        try:
            dbConnect = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="taxibookingsystem"
            )

            cursor = dbConnect.cursor()
            cursor.execute("SELECT * FROM booking")
            rows = cursor.fetchall()
            for row in rows:
                self.bookings_tree.insert("", "end", values=(row[0], row[1], row[2], row[3], row[4], row[6], row[7]))

        except Exception as err:
            print(f"{err}")

        # Entry fields and labels for pickup, destination, date, time, and driver id
        self.pickup_label = Label(self.root, text="Pickup Location:", font=("Helvetica", 12))
        self.pickup_label.place(x=20, y=400, height=30, width=150)
        self.pickup_entry = Entry(self.root, font=("Helvetica", 12))
        self.pickup_entry.place(x=200, y=400, height=30, width=200)

        self.destination_label = Label(self.root, text="Destination:", font=("Helvetica", 12))
        self.destination_label.place(x=600, y=400, height=30, width=150)
        self.destination_entry = Entry(self.root, font=("Helvetica", 12))
        self.destination_entry.place(x=750, y=400, height=30, width=200)

        self.date_label = Label(self.root, text="Date (YYYY-MM-DD):", font=("Helvetica", 12))
        self.date_label.place(x=20, y=500, height=30, width=150)
        self.date_entry = Entry(self.root, font=("Helvetica", 12))
        self.date_entry.place(x=200, y=500, height=30, width=200)

        self.time_label = Label(self.root, text="Time:", font=("Helvetica", 12))
        self.time_label.place(x=600, y=500, height=30, width=150)
        self.time_entry = Entry(self.root, font=("Helvetica", 12))
        self.time_entry.place(x=750, y=500, height=30, width=200)

        self.driver_id_label = Label(self.root, text="Driver id:", font=("Helvetica", 12))
        self.driver_id_label.place(x=1000, y=400, height=30, width=150)
        self.driver_id_entry = Entry(self.root, font=("Helvetica", 12))
        self.driver_id_entry.place(x=1150, y=400, height=30, width=200)

        self.booking_id_entry = Entry(self.root, font=("Helvetica", 12))
        self.booking_id_entry.place(x=2630, y=400, height=30, width=200)

        # Check Assign Driver Button
        self.check_button = Button(self.root, text="Check", command=self.check_driver, bg="green", fg="white", font=('Helvetica', 14))
        self.check_button.place(x=50, y=550, height=50, width=150)

        # Assign Driver Button
        self.assign_button = Button(self.root, text="Assign Driver", command=self.assign_driver, bg="green", fg="white", font=('Helvetica', 14))
        self.assign_button.place(x=250, y=550, height=50, width=150)

        # Logout Button
        self.logout_button = Button(self.root, text="Logout", command=self.logout, bg="green", fg="white", font=('Helvetica', 14))
        self.logout_button.place(x=1100, y=550, height=50, width=150)

    def check_driver(self):
        # Open a new window to check available drivers
        from CheckDriver import CheckDriver
        new_window = Tk()
        CheckDriver(new_window)
        new_window.mainloop()

    def assign_driver(self):
        driver_id = self.driver_id_entry.get()
        booking_id = self.booking_id_entry.get()

        try:
            dbConnect = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="taxibookingsystem"
            )

            myCursor = dbConnect.cursor()
            # SQL query to update booking with driver information
            sql = "UPDATE booking SET `Driver_id`=%s,`admin_id`=%s WHERE `Booking_id`=%s"
            sql2 = "UPDATE drivers SET `Availability`='No' WHERE driver_id=%s"
            values = (driver_id, Global.admin_id, booking_id)
            values2 = (driver_id,)
            myCursor.execute(sql, values)
            myCursor.execute(sql2, values2)
            dbConnect.commit()

            myCursor.close()
            dbConnect.close()

            messagebox.showinfo("Success", "Driver assigned successfully")

            # Close the current window and open a new AdminDashboard window
            self.root.destroy()
            new_window = Tk()
            AdminDashboard(new_window)
            new_window.mainloop()
            return True
        except Exception as error:
            print(error)

            messagebox.showerror("Error", "Failed to assign driver")
            return False

    def logout(self):
        # Close the current window and open a new Login window
        from Login import Login
        self.root.destroy()
        new_window = Tk()
        Login(new_window)
        new_window.mainloop()

    def selectedRow(self, event):
        # Handle selection in the Treeview
        selected_item = self.bookings_tree.focus()
        values = self.bookings_tree.item(selected_item, "values")

        if values:
            # Update entry fields with selected values
            self.pickup_entry.delete(0, "end")
            self.pickup_entry.insert(0, values[1])

            self.destination_entry.delete(0, "end")
            self.destination_entry.insert(0, values[2])

            self.date_entry.delete(0, "end")
            self.date_entry.insert(0, values[3])

            self.time_entry.delete(0, "end")
            self.time_entry.insert(0, values[4])

            self.booking_id_entry.delete(0, "end")
            self.booking_id_entry.insert(0, values[0])

            self.driver_id_entry.delete(0, "end")
            self.driver_id_entry.insert(0, values[6])

if __name__ == '__main__':
    root = Tk()
    AdminDashboard(root)
    root.mainloop()
