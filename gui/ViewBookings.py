from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import Global
from Model.BookingModel import Booking
from Controller.BookingController import update_booking, cancel_booking


class ViewBookings:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1000x700")
        self.root.title("View Bookings")

        # Frame for displaying bookings in a Treeview
        self.treeview_frame = Frame(self.root)
        self.treeview_frame.place(x=20, y=20)

        # Styling for Treeview
        style = ttk.Style()
        style.configure("Treeview.Heading", font=('Helvetica', 12))
        style.configure("Treeview", font=('Helvetica', 10), rowheight=25)

        # Treeview to display bookings
        self.bookings_tree = ttk.Treeview(self.treeview_frame,
                                          columns=("Booking_id", "Pickup Location", "Destination", "Date", "Time"),
                                          show="headings")
        self.bookings_tree.heading("Booking_id", text="Booking_id")
        self.bookings_tree.heading("Pickup Location", text="Pickup Location")
        self.bookings_tree.heading("Destination", text="Destination")
        self.bookings_tree.heading("Date", text="Date")
        self.bookings_tree.heading("Time", text="Time")
        self.bookings_tree.bind("<<TreeviewSelect>>", self.selectedRow)
        self.bookings_tree.pack()

        try:
            # Connect to the database and fetch bookings for the current customer
            dbConnect = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="taxibookingsystem"
            )

            cursor = dbConnect.cursor()
            cursor.execute(f"SELECT * FROM booking WHERE `customer_id`={Global.customer_information[0]}")
            rows = cursor.fetchall()

            # Insert fetched bookings into the Treeview
            for row in rows:
                self.bookings_tree.insert("", "end", values=(row[0], row[1], row[2], row[3], row[4]))

        except Exception as err:
            print(f"{err}")

        # Entry fields and labels for updating/canceling bookings
        self.pickup_label = Label(self.root, text="Pickup Location:", font=("Helvetica", 12))
        self.pickup_label.place(x=20, y=350, height=30, width=150)
        self.pickup_entry = Entry(self.root, font=("Helvetica", 12))
        self.pickup_entry.place(x=200, y=350, height=30, width=200)

        self.destination_label = Label(self.root, text="Destination:", font=("Helvetica", 12))
        self.destination_label.place(x=450, y=350, height=30, width=150)
        self.destination_entry = Entry(self.root, font=("Helvetica", 12))
        self.destination_entry.place(x=630, y=350, height=30, width=200)

        self.date_label = Label(self.root, text="Date (YYYY-MM-DD):", font=("Helvetica", 12))
        self.date_label.place(x=20, y=400, height=30, width=150)
        self.date_entry = Entry(self.root, font=("Helvetica", 12))
        self.date_entry.place(x=200, y=400, height=30, width=200)

        self.time_label = Label(self.root, text="Time:", font=("Helvetica", 12))
        self.time_label.place(x=450, y=400, height=30, width=150)
        self.time_entry = Entry(self.root, font=("Helvetica", 12))
        self.time_entry.place(x=630, y=400, height=30, width=200)

        self.booking_id_entry = Entry(self.root, font=("Helvetica", 12))
        self.booking_id_entry.place(x=2630, y=400, height=30, width=200)

        # Buttons for update, cancel, and go back
        self.update_button = Button(self.root, text="Update", command=self.update, bg="green", fg="white",
                                    font=("Helvetica", 12))
        self.update_button.place(x=20, y=450, height=40, width=120)

        self.cancel_button = Button(self.root, text="Cancel", command=self.cancel, bg="green", fg="white",
                                    font=("Helvetica", 12))
        self.cancel_button.place(x=20, y=550, height=40, width=120)

        self.back_button = Button(self.root, text="Back", command=self.close_window, bg="green", fg="white",
                                  font=("Helvetica", 12))
        self.back_button.place(x=160, y=450, height=40, width=120)

    def insert_data(self, booking_id, pickup_location, destination, date, time):
        # Insert new data into the Treeview
        self.bookings_tree.insert("", "end", values=(booking_id, pickup_location, destination, date, time))

    def close_window(self):
        # Close the current window and go back to the main dashboard
        from MainDashboard import MainDashboard
        self.root.destroy()
        new_root = Tk()
        MainDashboard(new_root)
        new_root.mainloop()

    def cancel(self):
        # Get booking ID from the entry field
        booking_id = self.booking_id_entry.get()

        # Check if booking_id is provided
        if not booking_id:
            messagebox.showerror("Error", "Please provide a Booking ID.")
            return

        # Display a confirmation messagebox
        confirm_cancel = messagebox.askyesno("Confirm Cancellation", "Are you sure you want to cancel this booking?")

        # If user confirms cancellation
        if confirm_cancel:
            booking = Booking(booking_id=booking_id)
            booking_cancelled = cancel_booking(booking)

            if booking_cancelled:
                messagebox.showinfo("Cancelled", "Booking cancelled successfully.")
                self.root.destroy()
                new_root = Tk()
                ViewBookings(new_root)
                new_root.mainloop()
            else:
                messagebox.showinfo("Error", "Failed to cancel booking.")

    def selectedRow(self, event):
        # Get selected item from the Treeview
        selected_item = self.bookings_tree.focus()
        values = self.bookings_tree.item(selected_item, "values")

        if values:
            # Fill entry fields with selected data
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

    def update(self):
        # Get data from entry fields
        pickup_location = self.pickup_entry.get()
        destination = self.destination_entry.get()
        date = self.date_entry.get()
        time = self.time_entry.get()
        booking_id = self.booking_id_entry.get()

        # Create Booking object
        booking = Booking(pickup_address=pickup_location, Destination=destination, Pickup_date=date, Time=time,
                          booking_id=booking_id)

        # Call update_booking function
        booking_updated = update_booking(booking)

        # Show success or error message
        if booking_updated:
            messagebox.showinfo("Updated", "Updated")
            self.root.destroy()
            new_root = Tk()
            ViewBookings(new_root)
            new_root.mainloop()
        else:
            messagebox.showinfo("error", "error")


if __name__ == '__main__':
    root = Tk()
    ViewBookings(root)
    root.mainloop()
