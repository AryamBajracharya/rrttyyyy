from PIL import Image as PILImage, ImageTk
from tkinter import *
from Model.CustomerModel import Customer
from tkinter import messagebox
from Controller.RegistrationController import login_customer
import Global
from Model.AdminModel import Admin
from Controller.adminLogin import login_admin
from Model.DriverModel import Driver
from Controller.DriverLogin import login_driver

class Login():
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x700+190+40")
        self.root.title("Login")
        self.root.configure(bg="black")

        # Load background image
        self.image = PILImage.open("../photos/Aplicación de servicio de taxi _ Vector Gratis.jpeg")
        resized_image = self.image.resize((680, 700))
        self.image = ImageTk.PhotoImage(resized_image)

        self.image_label = Label(self.root, image=self.image, bg="black")
        self.image_label.image = self.image
        self.image_label.place(x=0, y=0)

        # Header frame
        header_frame = Frame(self.root, bg="yellow")
        header_frame.pack(side="top", fill="x")

        # Header label
        header_label = Label(header_frame, text="Taxi Login", font=('Helvetica', 18), bg="black", fg="white")
        header_label.pack(pady=22)

        # Username entry and label
        self.username_lbl = Label(self.root, text="Username:", font=(20))
        self.username_lbl.place(x=700, y=200, height=30, width=110)

        self.username_txt = Entry(self.root)
        self.username_txt.place(x=850, y=200, width=200, height=30)

        # Password entry and label
        self.password_lbl = Label(self.root, text="Password:", font=(20))
        self.password_lbl.place(x=700, y=300, height=30, width=110)

        self.password_txt = Entry(self.root, show='*')
        self.password_txt.place(x=850, y=300, width=200, height=30)

        # Login Button
        self.login_btn = Button(self.root, text="Login", bg="green", fg="white", font=(15), command=self.login)
        self.login_btn.place(x=850, y=400, height=40, width=100)

        # Register as Customer Button
        self.register_customer_btn = Button(self.root, text="Register as Customer", bg="green", fg="white", font=(15), command=self.open_customer_registration)
        self.register_customer_btn.place(x=700, y=500, height=40, width=200)

        # Register as Driver Button
        self.register_driver_btn = Button(self.root, text="Register as Driver", bg="green", fg="white", font=(15), command=self.open_driver_registration)
        self.register_driver_btn.place(x=900, y=500, height=40, width=200)

    def login(self):
        # Retrieve username and password from entry fields
        username = self.username_txt.get()
        password = self.password_txt.get()

        # Customer login attempt
        customer = Customer(Username=username, Password=password)
        customer_verification = login_customer(customer)

        # Admin login attempt
        admin = Admin(username=username, password=password)
        admin_verification = login_admin(admin)

        # Driver login attempt
        driver = Driver(Username=username, Password=password)
        driver_verification = login_driver(driver)

        # Check login results and open corresponding dashboard
        if customer_verification is not None:
            from MainDashboard import MainDashboard
            Global.customer_information = customer_verification
            messagebox.showinfo("Welcome", f"Welcome {Global.customer_information[1]}")
            self.root.destroy()
            new_window = Tk()
            MainDashboard(new_window)
            new_window.mainloop()

        elif admin_verification is not None:
            from AdminDashboard import AdminDashboard
            Global.admin_id = admin_verification[0]
            messagebox.showinfo("Welcome", f"Welcome {admin_verification[1]}")
            self.root.destroy()
            new_window = Tk()
            AdminDashboard(new_window)
            new_window.mainloop()

        elif driver_verification is not None:
            from DriverDashboard import DriverDashboard
            Global.driver_id = driver_verification[0]
            messagebox.showinfo("Welcome", f"Welcome {driver_verification[1]}")
            self.root.destroy()
            new_window = Tk()
            DriverDashboard(new_window)
            new_window.mainloop()

        else:
            messagebox.showerror("Error", "Invalid credentials")

    def open_customer_registration(self):
        # Open customer registration window
        from Registeration  import Registration
        self.root.destroy()
        registration_window = Tk()
        Registration(registration_window)
        registration_window.mainloop()

    def open_driver_registration(self):
        # Open driver registration window
        from DriverRegisteration  import DriverRegistration
        self.root.destroy()
        registration_window = Tk()
        DriverRegistration(registration_window)
        registration_window.mainloop()

if __name__ == '__main__':
    root = Tk()
    Login(root)
    root.mainloop()
