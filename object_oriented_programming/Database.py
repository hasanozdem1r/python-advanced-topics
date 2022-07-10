import psycopg2


class Database:
    def __init__(self, host, db_name, user, password):
        self._host = host
        self._db_name = db_name
        self._user = user
        self._password = password
        try:
            self._connection = psycopg2.connect(
                host=self._host,
                database=self._db_name,
                user=self._user,
                password=self._password,
            )
            print("Connection Successful")
        except Exception as Error:
            print(Error)

    def connect_db(self):
        try:
            connection = psycopg2.connect(
                host=self._host,
                database=self._db_name,
                user=self._user,
                password=self._password,
            )
            print("Connection Successful")
        except Exception as Error:
            print(Error)

    def read_db(self):
        cursor = self._connection.cursor()
        query = "SELECT * FROM public.users"
        cursor.execute(query)
        for row in cursor.fetchall():
            print(row)

    def insert_db(self, email, full_name, username, password):
        """
        :param email:
        :param full_name:
        :param username:
        :param password:
        :return: log message about process result (inserted, failed)
        """
        cursor = self._connection.cursor()
        sql_query = "INSERT INTO public.users(email,full_name,username,password) VALUES(%s,%s,%s,%s);"
        cursor.execute(sql_query, (email, full_name, username, password))
        self._connection.commit()
        print("Successfully inserted")
        cursor.close()


db = Database("localhost", "User", "postgres", "Hsn58.34")
db.read_db()
