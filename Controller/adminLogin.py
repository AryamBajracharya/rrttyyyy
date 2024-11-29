import mysql.connector

def login_admin(customer):
    result = None
    try:
        dbConnect = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database = "taxibookingsystem"
        )

        myCursor = dbConnect.cursor()
        sql = "SELECT * FROM `admin` WHERE username=%s and password=%s"
        values = (customer.get_username(),customer.get_password())

        myCursor.execute(sql,values)
        result = myCursor.fetchone()

        myCursor.close()
        dbConnect.close()
        return result
    except Exception as error:
        print(error)
        return result