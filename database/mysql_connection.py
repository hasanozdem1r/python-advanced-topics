import mysql.connector
from configparser import ConfigParser

# create a ConfigParser class instance
conf_obj = ConfigParser()

# read all information from config file
conf_obj.read('database_config.ini')
user_info = conf_obj["MYSQL_USER_INFO"]
db_info = conf_obj["MYSQL_DB_CONFIG"]

db_connection = mysql.connector.connect(
  host="{}".format(db_info["host"]),
  user="{}".format(user_info["user"]),
  password="{}".format(user_info['password'])
)

if __name__=='__main__':
  mysql_obj=db_connection.connect()
  print('Connected')