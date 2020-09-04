
This API automation framework is developed using python requests library and pytest unit testing framework.
request library has methods which helps to make REST calls to the any application which exposes APIs.
pytest is an unit test framework which helps in writing test cases.

This framework uses the API exposed by https://reqres.in/  to illustrate how API calls can made using python. This framework can be used against other applications which exposes APIs.

``` Note: Make sure python and pip are installed on the system. Have tested the framework on Python 3.8.2 and pip 20.2.2```  

To install the framework follow below steps:  
 
1. Download the project or clone the project.  

 ```git clone https://github.com/gurudattvshenoy/api_automation.git```
 
2. Change the directory to api_automation.  

   ```Eg: cd api_automation```
   
3.Install dependencies for the framework using requirements.txt.  

  ```pip install requirements.txt```
  
4.Navigate to tests folder and run the below command:  

 ``` pytest -s --html=reports/relayrapi-users-crud.html```  
 
```
├── conf    - Contains configuration files like URL and base path,
│   ├── RelayrApiConstants.py  - Read the configurations and stores the as CONSTANT.
│   └── relayrapi.json         - Contains URL and base path
├── libs             - Core libraries or utilities which are often used by test cases
│   ├── common       
│   │   ├── ApiHelper.py  - Generic functions for making GET,POST,DELETE, UPDATE REST calls.
│   │   ├── Assertion.py  - wrapper over asser function for better usage
│   │   ├── ExecTime.py   - Decorator to show execution time and start and end of functions
│   │   ├── Logger.py     - Customizes log to print in testcase.log
│   └── userapi
│       └── UserApi.py    - Allow operations provided by /user. This will be for CRUD operations supported by API.
├── logs                  - Execution logs having steps done during execution
│   └── testcase.log
├── pytest.ini            - Overrides the pytest defaults i.e. pytest searches test in "tests" folder, test case should start with Verify etc.
├── reports     - Execution reports   
│   └── relayrapi-users-crud.html
├── requirements.txt - Dependencies of the project to run.
└── tests            - test cases written using pytest framework.
    └── test_users.py
```

API Reference: https://reqres.in/

This will run the tests and generates html reports in reports folder and execution logs will reside in logs folder for tracing the execution.

Tests automated are 
1. Create User:  

POST REST call to URL - https://reqres.in/api/users   

Request payload:
{
    "name": "guru",
    "job": "Software SDET"
}  

HTTP Response status:201  


2. List User:  

Fetches the user details whose id is 2.
GET REST call to URL - https://reqres.in/api/users/2  


API Response:
{
    "data": {
        "id": 2,
        "email": "janet.weaver@reqres.in",
        "first_name": "Janet",
        "last_name": "Weaver",
        "avatar": "https://s3.amazonaws.com/uifaces/faces/twitter/josephstein/128.jpg"
    },
    "ad": {
        "company": "StatusCode Weekly",
        "url": "http://statuscode.org/",
        "text": "A weekly newsletter focusing on software development, infrastructure, the server, performance, and the stack end of things."
    }
} 

