import mysql.connector

def book(booking):
    try:
        dbConnect = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database = "taxibookingsystem"
        )

        myCursor = dbConnect.cursor()
        sql = "INSERT INTO `booking`(`pickup_address`, `Destination`, `Pickup_date`, `Pickup_Time`, `Customer_Id`, `booking_status`) VALUES (%s,%s,%s,%s,%s,%s)"
        values = (booking.get_pickup_address(),booking.get_destination(),booking.get_pickup_date(),booking.get_time(),booking.get_customer_id(),booking.get_booking_status())

        myCursor.execute(sql,values)
        dbConnect.commit()

        myCursor.close()
        dbConnect.close()
        return True
    except Exception as error:
        print(error)
        return False

def update_booking(update):
    try:
        dbConnect = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database = "taxibookingsystem"
        )

        myCursor = dbConnect.cursor()
        sql = "UPDATE booking SET `pickup_address`=%s, `Destination`=%s,`Pickup_date`=%s,`Pickup_Time`=%s WHERE `Booking_id`=%s"
        values = (update.get_pickup_address(),update.get_destination(),update.get_pickup_date(),update.get_time(),update.get_booking_id())

        myCursor.execute(sql,values)
        dbConnect.commit()

        myCursor.close()
        dbConnect.close()
        return True
    except Exception as error:
        print(error)
        return False

def cancel_booking(cancel):
    try:
        dbConnect = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database = "taxibookingsystem"
        )

        myCursor = dbConnect.cursor()
        sql = "UPDATE booking SET `booking_status`='Cancelled' WHERE `Booking_id`=%s"
        values = (cancel.get_booking_id(),)

        myCursor.execute(sql,values)
        dbConnect.commit()

        myCursor.close()
        dbConnect.close()
        return True
    except Exception as error:
        print(error)
        return False