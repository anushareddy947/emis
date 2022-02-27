from db_connection import conn

def insert_data(json_data):
    mycursor = conn.cursor()
    sql = "INSERT INTO patient_data (resource_type, entry_resource_type,family_name,First_name,phone_number,city,address,state,gender,Language,postalcode) VALUES (%s, %s, %s, %s,%s,%s,%s,%s)"
    json_data = json_data.fillna(0)
    val = list(json_data.itertuples(index=False, name=None))
    print(val)
    for x in val:
        mycursor.execute(sql, x)
    conn.commit()
    print("data inserted")
    pass
