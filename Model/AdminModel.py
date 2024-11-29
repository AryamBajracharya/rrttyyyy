class Admin:
    def __init__(self, admin_id=0, name=None, username=None, password=None):
        self._admin_id = admin_id
        self._name = name
        self._username = username
        self._password = password

    def get_admin_id(self):
        return self._admin_id

    def get_name(self):
        return self._name

    def get_username(self):
        return self._username

    def get_password(self):
        return self._password

        # Setters

    def set_admin_id(self, admin_id):
        self._admin_id = admin_id

    def set_name(self, name):
        self._name = name

    def set_username(self, username):
        self._username = username

    def set_password(self, password):
        self._password = password