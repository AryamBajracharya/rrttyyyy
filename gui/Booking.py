from tkinter import *
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from Model.BookingModel import Booking
from Controller.BookingController import book
import Global
from PIL import Image as PILImage, ImageTk


class BookingApp():
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x700+190+40")
        self.root.title("Taxi Booking")
        self.root.configure(bg="black")

        self.image = PILImage.open("../photos/Bannerimg-min.png")
        resized_image = self.image.resize((680, 700))
        self.image = ImageTk.PhotoImage(resized_image)

        self.image_label = Label(self.root, image=self.image, bg="#404040")
        self.image_label.image = self.image
        self.image_label.place(x=500, y=0)

        # Back Button
        self.back_button = Button(self.root, text="Back", bg="green", fg="white", font=(15), command=self.go_back)
        self.back_button.place(x=950, y=650, height=40, width=100)

        # Pickup Location
        self.pickup_lbl = Label(self.root, text="Pickup Location:", font=(20))
        self.pickup_lbl.place(x=50, y=150, height=30, width=150)

        self.pickup_txt = Entry(self.root)
        self.pickup_txt.place(x=220, y=150, width=200, height=30)

        # Destination
        self.destination_lbl = Label(self.root, text="Destination:", font=(20))
        self.destination_lbl.place(x=50, y=200, height=30, width=110)

        self.destination_txt = Entry(self.root)
        self.destination_txt.place(x=220, y=200, width=200, height=30)

        # Date of Booking
        self.date_lbl = Label(self.root, text="Date of Booking:", font=(20))
        self.date_lbl.place(x=50, y=250, height=30, width=150)

        self.date_txt = DateEntry(self.root)
        self.date_txt.place(x=220, y=250, width=200, height=30)

        # Time of Booking
        self.time_lbl = Label(self.root, text="Time of Booking:", font=(20))
        self.time_lbl.place(x=50, y=300, height=30, width=150)

        self.time_txt = Entry(self.root)
        self.time_txt.place(x=220, y=300, width=200, height=30)

        # Book Taxi Button
        self.book_button = Button(self.root, text="Book Taxi", bg="green", fg="white", font=(15), command=self.book_taxi)
        self.book_button.place(x=200, y=450, height=40, width=200)

    def go_back(self):
        pass

    def go_back(self):
        from MainDashboard import MainDashboard  # Import MainDashboard class
        self.root.destroy()  # Destroy the current window
        main_dashboard_window = Tk()  # Create a new Tkinter window
        MainDashboard(main_dashboard_window)  # Create an instance of MainDashboard
        main_dashboard_window.mainloop()  # Start the Tkinter event loop

    def book_taxi(self):
        pickup_location = self.pickup_txt.get()
        destination = self.destination_txt.get()
        date = self.date_txt.get_date()
        time = self.time_txt.get()

        booking = Booking(pickup_address=pickup_location, Destination=destination, Pickup_date=date, Time=time,
                          booking_status="Pending", Customer_id=Global.customer_information[0])
        booking_done = book(booking)
        if booking_done:
            messagebox.showinfo("booked", "booked")
        else:
            messagebox.showinfo("error", "error")


if __name__ == '__main__':
    root = Tk()
    BookingApp(root)
    root.mainloop()
