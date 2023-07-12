"""
MySQL CRUD Operations with Context Managers
@ Hasan Özdemir 01/09/2022
"""
"""
Following steps required for whom using WSL and connecting Windows Machine
Firstly create user from MySQL Server
CREATE USER 'wsl_root'@'localhost' IDENTIFIED BY 'wsl_12345';
GRANT ALL PRIVILEGES ON *.* TO 'wsl_root'@'localhost' WITH GRANT OPTION;
CREATE USER 'wsl_root'@'%' IDENTIFIED BY 'wsl_12345';
GRANT ALL PRIVILEGES ON *.* TO 'wsl_root'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;
Then run following command
mysql -u wsl_root -p -h 192.168.1.95 (Windows Machine IP)
"""

# pip install mysql-connector-python
from mysql.connector import connect
from configparser import ConfigParser
from contextlib import contextmanager
from pandas import (
    read_sql,
    DataFrame,
)
import os


class MySqlCrud:

    def __init__(self, usr: str, pwd: str, hst: str) -> None:
        """
        MySqlCrud class constructor used to initialize database setups
        :param usr: <str> db username
        :param pwd: <str> db password
        :param hst: <str> db host
        """
        self.user = usr
        self.password = pwd
        self.host = hst

    @contextmanager
    def connect_database(self, database: str) -> None:
        """
        This context manager is created to manage properly external resources
        :param database: <str> Name of database to connect
        :return: None
        """
        # instantiate connection obj __init__ method
        connection_obj = connect(host=self.host,
                                 user=self.user,
                                 password=self.password,
                                 database=database)
        try:
            # connect to db __enter__ method
            yield connection_obj
        except Exception:
            # rollback all changes
            connection_obj.rollback()
        else:
            # apply changes
            connection_obj.commit()
        finally:
            # close connection __exit__ method
            connection_obj.close()

    def read_data_from_db(self, database: str, query: str,
                          output_format) -> DataFrame or list or None:
        """
        This method is created to fetch data from databases with support of context managers
        :param database: <str> Name of database to fetch data
        :param table_name:  <str> Name of table to fetch data
        :param output_format: <str> set the output format. [Dataframe, list , None]
        :return: <DataFrame/list/None> data which is taken from database system
        """
        # we used our built-in context manager
        with self.connect_database(database=database) as connection:
            if output_format == DataFrame:
                # get data as dataframe
                query_data: DataFrame = read_sql(sql=f"{query};",
                                                 con=connection)
                return query_data
            elif output_format == list:
                cursor_obj = connection.cursor()
                cursor_obj.execute(f"{query};")
                query_data: list = cursor_obj.fetchall()
                return query_data
            else:
                return None


# create a ConfigParser class instance
conf_obj = ConfigParser()
cwd = os.path.dirname(__file__)
# read all information from config file
conf_obj.read(f"{cwd}/database_config.ini")
user_info = conf_obj["MYSQL_USER_INFO"]
db_info = conf_obj["MYSQL_DB_CONFIG"]

if __name__ == "__main__":
    # get database configuration files
    user = str(user_info["user"])
    password = str(user_info["password"])
    host = str(db_info["host"])
    # instantiate MySqlCrud object
    mysql_obj = MySqlCrud(usr=user, pwd=password, hst=host)
    # read data from database
    data = mysql_obj.read_data_from_db(database='holibrary',
                                       query='select * from Books;',
                                       output_format=DataFrame)
    print(data)
