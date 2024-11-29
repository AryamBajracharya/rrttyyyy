import mysql.connector

def registerCustomer(register):
    try:
        dbConnect = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database = "taxibookingsystem"
        )

        myCursor = dbConnect.cursor()
        sql = "INSERT INTO `customers`(`Name`, `Address`, `Username`, `Password`, `Confirm_Password`, `Email`, `Gender`, `Date_Of_Birth`, `Phone_Number`, `Card_Number`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        values = (register.get_name(),register.get_address(),register.get_username(),register.get_password(),register.get_confirm_password(),register.get_email(),register.get_gender(),register.get_date_of_birth(),register.get_phone_number(),register.get_card_number())

        myCursor.execute(sql,values)
        dbConnect.commit()

        myCursor.close()
        dbConnect.close()
        return True
    except Exception as error:
        print(error)
        return False


def registerDriver(driver):
    try:
        dbConnect = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="taxibookingsystem"
        )

        myCursor = dbConnect.cursor()
        sql = "INSERT INTO `drivers`(`Name`, `Address`, `Username`, `Password`, `Confirm_Password`, `Email`, `Gender`, `Phone_Number`, `License_No`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        values = (
            driver.get_name(), driver.get_address(), driver.get_username(), driver.get_password(),
            driver.get_confirm_password(), driver.get_email(), driver.get_gender(),
            driver.get_phone_number(), driver.get_license_no()
        )

        myCursor.execute(sql, values)
        dbConnect.commit()

        myCursor.close()
        dbConnect.close()
        return True
    except Exception as error:
        print(error)
        return False

def login_customer(customer):
    result = None
    try:
        dbConnect = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database = "taxibookingsystem"
        )

        myCursor = dbConnect.cursor()
        sql = "SELECT * FROM `customers` WHERE username=%s and password=%s"
        values = (customer.get_username(),customer.get_password())

        myCursor.execute(sql,values)
        result = myCursor.fetchone()

        myCursor.close()
        dbConnect.close()
        return result
    except Exception as error:
        print(error)
        return result