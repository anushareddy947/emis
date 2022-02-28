import mysql.connector

# Connecting from the server
conn = mysql.connector.connect(user='root',
                               password='abc',
                               host='localhost',
                               database='json_data',
                               auth_plugin='mysql_native_password')

