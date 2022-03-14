class User:
    # User class constructor
    def __init__(self, username, full_name, email, password):
        """
        :param username: <str>
        :param full_name: <str>
        :param email:  <str>
        :param password: <str>
        """
        self._username = username
        self._full_name = full_name
        self._email = email
        self.password = password

    def get_username(self):
        """
        :return: username
        """
        return self._username

    def set_username(self, username):
        """

        :param username: <str> User's username
        :return: None
        """
        self._username = username

    def get_full_name(self):
        """
        :return: full_name
        """
        return self._username

    def set_full_name(self, full_name):
        """

        :param full_name: <str> User name and surname information
        :return: None
        """
        self._full_name = full_name

    def get_email(self):
        """
        :return: email
        """
        return self._email

    def set_email(self, email):
        """

        :param email: <str> User's email information
        :return: None
        """
        self._email = email
