import mysql.connector

# Connecting from the server
conn = mysql.connector.connect(user='root',
                               host='mysqldb',
                               password='root',
                               database='json_data')

