class Booking:
    def __init__(self, booking_id=0, pickup_address=None, Destination=None, Pickup_date=None, Time=None,Customer_id=0, booking_status=None, driver_id=0, admin_id=0):
        self._booking_id = booking_id
        self._pickup_address = pickup_address
        self._Destination = Destination
        self._Pickup_date = Pickup_date
        self._Time = Time
        self._Customer_id = Customer_id
        self._booking_status = booking_status
        self._driver_id = driver_id
        self._admin_id = admin_id

    # Add getters and setters as needed

    # Getter methods
    def get_booking_id(self):
        return self._booking_id

    def get_pickup_address(self):
        return self._pickup_address

    def get_destination(self):
        return self._Destination

    def get_pickup_date(self):
        return self._Pickup_date

    def get_time(self):
        return self._Time

    def get_customer_id(self):
        return self._Customer_id

    def get_booking_status(self):
        return self._booking_status

    def get_driver_id(self):
        return self._driver_id

    def get_admin_id(self):
        return self._admin_id

    # Setter methods
    def set_booking_id(self, booking_id):
        self._booking_id = booking_id

    def set_pickup_address(self, pickup_address):
        self._pickup_address = pickup_address

    def set_destination(self, destination):
        self._Destination = destination

    def set_pickup_date(self, pickup_date):
        self._Pickup_date = pickup_date

    def set_time(self, time):
        self._Time = time

    def set_customer_id(self, customer_id):
        self._Customer_id = customer_id

    def set_booking_status(self, booking_status):
        self._booking_status = booking_status

    def set_driver_id(self, driver_id):
        self._driver_id = driver_id

    def set_admin_id(self, admin_id):
        self._admin_id = admin_id
