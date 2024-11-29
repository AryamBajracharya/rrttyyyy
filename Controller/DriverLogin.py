import mysql.connector

def login_driver(customer):
    result = None
    try:
        dbConnect = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database = "taxibookingsystem"
        )

        myCursor = dbConnect.cursor()
        sql = "SELECT * FROM `drivers` WHERE Username=%s and Password=%s"
        values = (customer.get_username(),customer.get_password())

        myCursor.execute(sql,values)
        result = myCursor.fetchone()

        myCursor.close()
        dbConnect.close()
        return result
    except Exception as error:
        print(error)
        return result