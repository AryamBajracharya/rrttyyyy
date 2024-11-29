from tkinter import *
from tkinter import ttk, messagebox
from Model.CustomerModel import Customer
from Controller.RegistrationController import registerCustomer
from tkcalendar import DateEntry

class Registration():
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x600+250+100")
        self.root.title("Registration")

        # Header
        header_frame = Frame(self.root, bg="#3498db")
        header_frame.pack(side="top", fill="x")

        header_label = Label(header_frame, text="Customer Registration", font=('Helvetica', 10), bg="#3498db", fg="white")
        header_label.pack(pady=12)

        # Name
        self.name_lbl = Label(self.root, text="Name:", font=(20))
        self.name_lbl.place(x=100, y=50, height=30, width=110)

        self.name_txt = Entry(self.root)
        self.name_txt.place(x=250, y=50, width=200, height=30)

        # Address
        self.address_lbl = Label(self.root, text="Address:", font=(20))
        self.address_lbl.place(x=100, y=100, height=30, width=110)

        self.address_txt = Entry(self.root)
        self.address_txt.place(x=250, y=100, width=200, height=30)

        # Username
        self.username_lbl = Label(self.root, text="Username:", font=(20))
        self.username_lbl.place(x=100, y=150, height=30, width=110)

        self.username_txt = Entry(self.root)
        self.username_txt.place(x=250, y=150, width=200, height=30)

        # Password
        self.password_lbl = Label(self.root, text="Password:", font=(20))
        self.password_lbl.place(x=100, y=200, height=30, width=110)

        self.password_txt = Entry(self.root, show='*')
        self.password_txt.place(x=250, y=200, width=200, height=30)

        # Confirm Password
        self.confirm_password_lbl = Label(self.root, text="Confirm:", font=(20))
        self.confirm_password_lbl.place(x=100, y=250, height=30, width=110)

        self.confirm_password_txt = Entry(self.root, show='*')
        self.confirm_password_txt.place(x=250, y=250, width=200, height=30)

        # Email
        self.email_lbl = Label(self.root, text="Email:", font=(20))
        self.email_lbl.place(x=100, y=300, height=30, width=110)

        self.email_txt = Entry(self.root)
        self.email_txt.place(x=250, y=300, width=200, height=30)

        # Gender
        self.gender_lbl = Label(self.root, text="Gender:", font=(20))
        self.gender_lbl.place(x=100, y=350, height=30, width=110)

        self.gender_var = StringVar()
        self.gender_var.set("Male")  # Default value
        gender_options = ["Male", "Female", "Other"]

        self.gender_combobox = ttk.Combobox(self.root, textvariable=self.gender_var, values=gender_options, state="readonly")
        self.gender_combobox.place(x=250, y=350, width=200, height=30)

        # Date of Birth
        self.dob_lbl = Label(self.root, text="Date of Birth:", font=(20))
        self.dob_lbl.place(x=100, y=400, height=30, width=150)

        self.dob_txt = DateEntry(self.root)
        self.dob_txt.place(x=250, y=400, width=200, height=30)

        # Phone Number
        self.phone_lbl = Label(self.root, text="Phone Number:", font=(20))
        self.phone_lbl.place(x=100, y=450, height=30, width=150)

        self.phone_txt = Entry(self.root)
        self.phone_txt.place(x=250, y=450, width=200, height=30)

        # Register Button
        self.register_btn = Button(self.root, text="Register", bg="green", fg="white", font=(15), command=self.register)
        self.register_btn.place(x=250, y=500, height=40, width=100)

    def register(self):
        # Get values from the input fields
        name = self.name_txt.get()
        address = self.address_txt.get()
        username = self.username_txt.get()
        password = self.password_txt.get()
        confirm_password = self.confirm_password_txt.get()
        email = self.email_txt.get()
        gender = self.gender_var.get()
        dob = self.dob_txt.get_date()
        phone = self.phone_txt.get()

        # Check if passwords match
        if password == confirm_password:
            # Create a Customer object
            customer = Customer(Name=name, Address=address, Username=username, Password=password,
                                Confirm_Password=confirm_password, Email=email, Gender=gender, Date_Of_Birth=dob,
                                Phone_Number=phone, Card_Number="0000")

            # Register the customer
            registered = registerCustomer(customer)

            if registered:
                # Show success message and return to login screen
                messagebox.showinfo("Successful", "Registered Successfully")
                self.root.destroy()
                from Login import Login
                new_window = Tk()
                Login(new_window)
                new_window.mainloop()
            else:
                messagebox.showinfo("Error", "Error")
        else:
            messagebox.showerror("Registration Failed", "Passwords do not match.")

# Main program
if __name__ == '__main__':
    root = Tk()
    Registration(root)
    root.mainloop()
