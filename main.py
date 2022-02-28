import json
from insert_data import insert_data
from normalised import json_to_dataframe
from retrieve_data import retrieve_inserted_data
import os

# Attribute __name__ is set to __main__ to run the main program
if __name__ == '__main__':

    #files = ['Bill567.json', 'Chase54.json', 'Blanch.json', 'Bob.json']
    json_data = []
    path = r'/'
    for root, directories, files in os.walk(path):
        for file in files:
            filepath = os.path.join(root, file)
            if filepath.endswith('.json') or filepath.endswith('.json.gz'):
                with open(filepath, 'r') as json_file:
                    json_data.append(json.load(json_file))

    df = json_to_dataframe(json_data)
    df.drop_duplicates()
    # Converting dataframe to csv
    df.to_csv('normalised_data.csv')

    # selecting only few fields from dataframe into the variable insert as dataframe

    insert = df[['resourceType', 'entry.resource.resourceType', 'entry.resource.name.given', 'entry.resource.name.family','entry.resource.telecom.value', 'entry.resource.address.city', 'entry.resource.address.line', 'entry.resource.gender', 'entry.resource.communication.language.coding.display', 'entry.resource.address.postalCode']]

    # renaming columns of insert dataframe
    insert.rename(columns={"resourceType": "resource_type", "entry.resource.resourceType": "entry_resource_type",
                           "entry.resource.name.family": "family_name", "entry.resource.name.given": "First_name", "entry.resource.telecom.value": "phone_number",
                           "entry.resource.address.city": "city", "entry.resource.address.line": "address", "entry.resource.gender": "gender", "entry.resource.communication.language.coding.display": "Language", "entry.resource.address.postalCode": "postalcode"},
                  inplace=True)

    insert = insert.drop_duplicates()

    # passing dataframe as parameter to insert the select columns into database
    insert_data(insert)
    # Method to retrieve inserted data from mysql database

    retrieve_inserted_data()


