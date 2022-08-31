### QA Interview


Hi, If you are viewing this, it is because you scaled through to the next round of the recruitment for the  QA position at Wafi. Congratulations 🎉✨.

WAFi is a fintech company, code must be thoroughly tested before deployed to production. As part of the QA Engineer interview process, candidates are asked to showcase their ability in both manual and automated testing.


## Getting Setup

Packages and Programs to Install

## Install Python
  Refer to the link to install [Python](https://www.python.org/downloads/)

## APP
The application  is a simple crud django app to manage employee records.
The  allowed operations are post, delete , update and edit employee tables.

| Endpoint  | GET | POST | PUT | DELETE |
| ------------- | ------------- |  ------------- |  ------------- |  ------------- |
| apis/emp | List all employee | Create: Add an employee. **Body** - {id: "id" ,"name": "name","email": "email","Phone_Number": "number"} | 	N/A |	N/A
| apis/emp/<int: employee_id> | Retrieve: Get an employee with employee_id|	N/A	| Update: Update a employee with given employee_id	| Delete: Delete a employee with given employee_id


## Running the App

Open your terminal and navigate to where you'd like this repo to be downloaded. You can clone the repo by typing the following into the command line:

```
git clone https://github.com/Wafi-inc/qa-interview-assignment.git
```

To start the app,

```
cd  qa-interview-assignment
pip install -r requirements.txt
python manage.py runserver
```
Visit http://127.0.0.1:8000/emp on your browser to the default page. 

## Your task

### Manual QA
-  Take note of bugs (logic or function) found in the application. Report as many as possible.
-  Kindly organize your feedback on how you went about the testing and feedback. Report your feedback as if you were talking to a Developer.
- Feel free to use any program to take notes. Don't forget to make it accessbile.


### Automated QA

 - Write a postman test collection  for the endpoint, the test must cover both working and failed functionality.
 - Feel free to report any bug noticed in the endpoints
 - Using selenium, Write a test script to test the submit button. Include the selenium script and relevenant steps to run it.

Feel free to dazzle with your solutions.

###  Submission

Upon completion, please email with attachement
1. Digital report of your findings.
2. Postman test collections and selenium script.


See you soon 👋🏻.
