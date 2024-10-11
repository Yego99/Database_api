# Database_api
 Read_me.
This project is a flask-based web app that allows users to query a timesheet database through a REST API and display the results in a web frontend. 

Requirements:
To run this project, you’ll need these programs installed on your device:
1.	Python
2.	Pip installer
3.	Required Python libraries: pandas, numpy, sqlite3, logging, flask(Flask, jsonify, request, render_template)
4.	Virtual environment tool

SETUP: 
1)	Please download the following 4 folders and put them in a file on your desktop.
  •	Coding_Exercise_Sample_Data
  •	Coding_assessment
  •	api
  •	fe (IMPORTANT: After you download ‘fe’ create a new folder in the folder you are saving all of these files in called ‘templates’ and put fe into that folder)

**I will walk you through how to set up the program assuming the name of the folder you saved all the files too is called my_flask_app**
(code snipits are for windows computers)

1)	Open command prompt and navigate to the my_flask_app current directly 
  a)	cd path\to\my_flask_app
2)	(Optional but recommended) set up and activate a virtual environment 
  a)	Set up: python -m venv venv 
  b)	Activate: venv\Scripts\activate
3)	Install the pip requirements mentioned above
  a)	Pip install xxx
4)	Load data into sql databse by running coding_assessment.py file (python coding_assessment.py)
5)	Activate the api and web server by running api.py file (python api.py)
6)	You should get a notification that that a server is running locally on http://127.0.0.1:5000
7)	Click on that link

Front end
By default, when you first open the browser, it will immediately pull all the data. You can type in the name of any client you want in the search bar and all their projects will come up. If you want to go back to the original full data set you can refresh the page. 

Back end
Adding entries to the data table can only be done on the back end through the command prompt. Enter this code into the command prompt while the server is running. You may have to open a new command prompt window to do so.  
•	curl -X POST http://127.0.0.1:5000/timesheet_entries -H "Content-Type: application/json" -d "{\"name\":\"Test_User\",\"client\":\"Test_Client\",\"hours\":5.0,\"billable_rate\":100,\"billable_amount\":500}" 
You can replace the test_user, test_client, 5.0, 100, and 500 with your own numbers and names

DISCLAIMER: You cannot delete entries and all new entries that are entered will not be saved to the database so when you take the server down then they will be lost. This was made for demonstration purposes. 

You can also query the database through the command prompt on the back end. Use the following commands in the command prompt to call data:
  a.	To get all entries enter: curl http://127.0.0.1:5000/timesheet_entries into the command prompt as is
  b.	To get entries by client enter: curl http://127.0.0.1:5000/timesheet_entries/’client’%20’name’ into the command prompt but replace ‘client’%20’name’ with the client name you want in-between ‘ ‘. The %20 acts as a space 
