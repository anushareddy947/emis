import json
from normalize import json_to_dataframe
from insert_data import insert_data
from retrieve_data import retrieve_inserted_data

# Attribute __name__ is set to __main__ to run the main program
if __name__ == '__main__':
    json_data = []
    files = ['Bill567.json', 'Chase54.json', 'Blanch.json', 'Bob.json']
    for file in files:
    # to read the json file
       with open(file, encoding='utf8') as json_file:
            json_data.append(json.load(json_file))

    # json data is normalized and filtered by calling this method, passing json_data as a parameter
    df = json_to_dataframe(json_data)
    df.drop_duplicates()
    # Converting dataframe to csv
    df.to_csv('normailized_data.csv')

    # selecting only few fields from dataframe into the variable insert as dataframe
    insert = df[['resourceType', 'entry.resource.resourceType', 'entry.resource.name.given', 'entry.resource.name.family', 'entry.resource.address.city', 'entry.resource.address.line', 'entry.resource.gender', 'entry.resource.communication.language.coding.display']]

    # renaming columns of insert dataframe
    insert.rename(columns={"resourceType": "resource_type", "entry.resource.resourceType": "entry_resource_type",
                           "entry.resource.name.family": "family_name", "entry.resource.name.given": "First_name",
                           "entry.resource.address.city": "city", "entry.resource.address.line": "address", "entry.resource.gender": "gender", "entry.resource.communication.language.coding.display": "Language"},
                  inplace=True)
    insert = insert.drop_duplicates()

    # passing dataframe as parameter to insert the select columns into database
    insert_data(insert)

    # Method to retrieve inserted data from mysql database

    retrieve_inserted_data()

