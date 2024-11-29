class Customer:
    def __init__(self, Customer_Id=0, Name=None, Address=None, Username=None, Password=None, Confirm_Password=None, Email=None, Gender=None, Date_Of_Birth=None, Phone_Number=None, Card_Number=None):
        self._Customer_Id = Customer_Id
        self._Name = Name
        self._Address = Address
        self._Username = Username
        self._Password = Password
        self._Confirm_Password = Confirm_Password
        self._Email = Email
        self._Gender = Gender
        self._Date_Of_Birth = Date_Of_Birth
        self._Phone_Number = Phone_Number
        self._Card_Number = Card_Number

    def get_customer_id(self):
        return self._Customer_Id

    def set_customer_id(self, customer_id):
        self._Customer_Id = customer_id

    def get_name(self):
        return self._Name

    def set_name(self, name):
        self._Name = name

    def get_address(self):
        return self._Address

    def set_address(self, address):
        self._Address = address

    def get_username(self):
        return self._Username

    def set_username(self, username):
        self._Username = username

    def get_password(self):
        return self._Password

    def set_password(self, password):
        self._Password = password

    def get_confirm_password(self):
        return self._Confirm_Password

    def set_confirm_password(self, confirm_password):
        self._Confirm_Password = confirm_password

    def get_email(self):
        return self._Email

    def set_email(self, email):
        self._Email = email

    def get_gender(self):
        return self._Gender

    def set_gender(self, gender):
        self._Gender = gender

    def get_date_of_birth(self):
        return self._Date_Of_Birth

    def set_date_of_birth(self, date_of_birth):
        self._Date_Of_Birth = date_of_birth

    def get_phone_number(self):
        return self._Phone_Number

    def set_phone_number(self, phone_number):
        self._Phone_Number = phone_number

    def get_card_number(self):
        return self._Card_Number

    def set_card_number(self, card_number):
        self._Card_Number = card_number

