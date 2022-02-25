from db_connection import conn
import pandas as pd


def retrieve_inserted_data():
    mycursor = conn.cursor(buffered=True)
    query = "SELECT * FROM patient_data ORDER BY id DESC LIMIT 5"
    mycursor.execute(query)
    df = pd.read_sql(query, conn)
    conn.close()
    print(df)
    df.to_csv('retrieved_data.csv')
    print("Data retrieved from database")
