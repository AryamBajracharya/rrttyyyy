from tkinter import *

class MainDashboard:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x700+190+40")
        self.root.title("Main Dashboard")

        self.header = Frame(self.root,bg="light blue")
        self.header.place(x=0,y=0,height=150,width=1100)


        # Create and place widgets
        self.welcome_label = Label(self.root, text="Welcome to Taxi Booking", font=("Helvetica", 45))
        self.welcome_label.place(x=170, y=300, height=70, width=800)

        self.book_taxi_button = Button(self.header, text="Book a Taxi", command=self.book_taxi)
        self.book_taxi_button.place(x=100, y=50, height=50, width=120)

        self.update_booking_button = Button(self.header, text="Update Booking", command=self.update_booking)
        self.update_booking_button.place(x=280, y=50, height=50, width=120)

        self.view_bookings_button = Button(self.header, text="View Bookings", command=self.view_bookings)
        self.view_bookings_button.place(x=450, y=50, height=50, width=120)

        self.logout_button = Button(self.header, text="Logout", command=self.logout, bg="green", fg="white")
        self.logout_button.place(x=930, y=50, height=50, width=120)

    def book_taxi(self):
        from Booking import BookingApp
        self.root.destroy()
        Booking_window = Tk()
        BookingApp(Booking_window)
        Booking_window.mainloop()

    def update_booking(self):
        print("Opening update booking window")

    def view_bookings(self):
        from ViewBookings import ViewBookings

        self.root.destroy()
        view_window = Tk()
        login = ViewBookings(view_window)
        view_window.mainloop()

    def logout(self):
        from Login import Login

        self.root.destroy()
        login_window = Tk()
        login = Login(login_window)
        login_window.mainloop()

if __name__ == '__main__':
    root = Tk()
    MainDashboard(root)
    root.mainloop()