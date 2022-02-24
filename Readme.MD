#The aim of the assessment is to convert the JSON file into a workable format such as CSV or excel sheet. The project has been divided into parts for a better understanding purpose.

#STEP1:  Initially, set a virtual environment, directory and created a project in PyCharm.
#Use python -m venv myenv to create a virtual environment in your project containing a directory. Install all dependency modules available in requirements.txt by using pip install -r requirement.txt
#Required packages are loaded and an attribute is set to run the main program and then loaded the JSON file to convert into data frames.

#STEP2: Loading JSON file to read and convert to data frames.
#Pandas data frame is an easy and readable way that normalizes the JSON data and converts it into data frames. However, converting files into data frames isn’t enough to handle errors. So, data has been normalised further.

#SETP 3: Converting data frames into CSV by normalising the data.
#Data normalisation is done in a separate file called Normalize.py. Just json_normalise() works great to simple JASON file, but here the data is in nested form with list and dictionary. So, flatten function is used in implementing iterator in loops and converting nested data into separate columns and returning normalized data. The below picture shows normalised data.

![Normalized](https://user-images.githubusercontent.com/81103191/155490828-ab0174c7-5df5-484c-bd69-9c71321965e0.PNG)

#Main.py: This file is set to run the main program and JSON files are loaded to read and normalized. Selected necessary fields from converted data frame and inserted into a variable. Rename the variable columns in a convenient way. The inserted data is connected to a database and returns retrieved data from the MySQL database. Separate files are created to write code inserted data and retrieve data.

#STEP 4: Selected fields of data are inserted into the database.
#This file is called an instert_data.py, where connecting cursor to fetch the inserted data from database and filling the empty rows into 0 using fillna() function. Then create a variable to list the values in by iteration and commit the data.

#SETP 5: Finally retrieve the inserted data into a CSV file.
#This method is stored in this Retrieve_data.py file. This file consists of the data, which is connected to a database, by executing the query the cursor will fetch the data in the database and buffer in each row and retrieve the data in CSV format. The below picture shows the inserted data in database.
![Retrived data from DB](https://user-images.githubusercontent.com/81103191/155491555-0c4bd1ad-e6af-447e-b34b-e203b38f8d78.PNG)
