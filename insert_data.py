from db_connection import conn

def insert_data(json_data):
    mycursor = conn.cursor()
    mycursor.execute("CREATE DATABASE json_data")
    mycursor.execute("CREATE TABLE patient_data (id INT(11) AUTO_INCREMENT PRIMARY KEY, resource_type VARCHAR(255), entry_resource_type VARCHAR(255), family_name VARCHAR(200), First_name VARCHAR(200), phone_number INT(100), gender VARCHAR(15), Language VARCHAR(200),address VARCHAR(150),city VARCHAR(200), postalcode INT(100))")
    sql = "INSERT INTO patient_data (resource_type, entry_resource_type,family_name,First_name,phone_number,city,address,state,gender,Language,postalcode) VALUES (%s, %s, %s, %s,%s,%s,%s,%s,%s,%s)"
    json_data = json_data.fillna(0)
    val = list(json_data.itertuples(index=False, name=None))
    print(val)
    for x in val:
        mycursor.execute(sql, x)
    conn.commit()
    print("data inserted")
    pass
