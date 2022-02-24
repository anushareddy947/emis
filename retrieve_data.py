from db_connection import conn
import pandas as pd

def retrieve_inserted_data():
    mycursor = conn.cursor(buffered=True)
    query = "SELECT * FROM patient_data"
    print("endtest")

    mycursor.execute(query)
    df = pd.read_sql(query, conn)
    conn.close()
    df.to_csv('retrieved_data.csv')
    print("Data retrieved from database")
