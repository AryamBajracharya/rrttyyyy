class Driver:
    def __init__(self, Driver_Id=0, Name=None, Address=None, Username=None, Password=None, Confirm_Password=None, Email=None, Gender=None,  Phone_Number=None, License_No=None):
        self._Driver_Id = Driver_Id
        self._Name = Name
        self._Address = Address
        self._Username = Username
        self._Password = Password
        self._Confirm_Password = Confirm_Password
        self._Email = Email
        self._Gender = Gender
        self._Phone_Number = Phone_Number
        self._License_No = License_No

    # Getter methods
    def get_driver_id(self):
        return self._Driver_Id

    def get_name(self):
        return self._Name

    def get_address(self):
        return self._Address

    def get_username(self):
        return self._Username

    def get_password(self):
        return self._Password

    def get_confirm_password(self):
        return self._Confirm_Password

    def get_email(self):
        return self._Email

    def get_gender(self):
        return self._Gender

    def get_phone_number(self):
        return self._Phone_Number

    def get_license_no(self):
        return self._License_No

    # Setter methods
    def set_driver_id(self, driver_id):
        self._Driver_Id = driver_id

    def set_name(self, name):
        self._Name = name

    def set_address(self, address):
        self._Address = address

    def set_username(self, username):
        self._Username = username

    def set_password(self, password):
        self._Password = password

    def set_confirm_password(self, confirm_password):
        self._Confirm_Password = confirm_password

    def set_email(self, email):
        self._Email = email

    def set_gender(self, gender):
        self._Gender = gender

    def set_phone_number(self, phone_number):
        self._Phone_Number = phone_number

    def set_license_no(self, license_no):
        self._License_No = license_no






