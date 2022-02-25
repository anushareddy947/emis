#The aim of the assessment is to convert the JSON file into a workable format such as CSV that can readily used for data analysis. My implementation has been divided into different procudural steps for the given dataset.

#STEP1: Selection of Pycharm virtual enivronment for data conversion. processing

Initially, for implementation I have choose PyCharm and I have activated the virtual environment using python -m venv myenv. I have a created a directory named as project. Installed all dependency modules available in requirements.txt. All required packages are loaded and is set to run in the main program.

#STEP2: Data Loading

I have used list function to pull the raw JSON file to convert into data frame. I have create list to add mutiple files for further extensions. I have used pandas library to convert the json data into data frames, which is normalised and easily readable format. However, converting files into data frames isn’t enough to handle the real time errors. So, data has been normalised to reduce the data compression errors at this stage and the normalised data is executable in main.py().

#Main.py: Main.py() is a starting function and this file is set to run the main program and holds JSON files that are normalized into readable format. Selected necessary fields from converted data frame and inserted into a variable. Rename the variable columns in a convenient way. The inserted data is connected to a database and returns retrieved data from the MySQL database. Separate files are created to write code inserted data and retrieve data.

#STEP 3: Handling the data compression errors

I have obsered that the converted data frame was having data compression errors. To handle this errors I have used normalisation further. Using the selected functions. Data normalisation is done in a separate file called Normalize.py which holds the main code in an understandable format. For handling low volumes of data jason_normalised( ) can be used.But the given jason file is complex and integrated with data in a nested form such lists and dictionaries. The flatten function() is used to implement iterations in loops and to convert nested data into seperate accessable columns and returns the normalized data. Below is the presentation of the normalized data.

![Normalized](https://user-images.githubusercontent.com/81103191/155490828-ab0174c7-5df5-484c-bd69-9c71321965e0.PNG)

#STEP 4: Data preparation.

The main.py file which holds the normalized data into separate columns. I have renamed the selected columns headers into convenient labels which are important and necessary for data analysis. The fillna() function is used to fill the empty rows into 0.

#STEP 5: MYsql Database

The selected file is stored in MySql database. So the retrived data in the form of CSV file. Conn.Cursor() is used in Insert_data file and retrived_data file to fetch the data stored in database. buffer() function is used to retrieve the data from each row into CSV format. The below picture shows the retrived data in tabular format in database.

![Filtered data](https://user-images.githubusercontent.com/81103191/155578992-e465cd99-a37a-4adf-9fe4-efa2b93443be.PNG) 

Retrived data as showing in console.
![console](https://user-images.githubusercontent.com/81103191/155579492-5ec52506-62b5-4cfb-9d8d-5a3ab8cb2288.PNG)

#Conclusion: Finally I could analyse the raw json file and convert it into the readable csv format using Pycharm and retrieve data from database that can be used for further pateint data analysis.

FUTURE GOALS:

#My future goal is to explore on new method to handle the large volume of complex data and process quickly in less time frame by designing a user interface to upload the json file and create a dashboard which displays the patient data in a meaning full way. I'll create a NoSql database to store and retrieve data which will save time. Within less time frame we can process the data quickly.
