# Employee Management API

This is a simple REST API for managing employees using Flask and SQLite.

#  Setup Instructions

1. ## Clone the repository
   git clone <repo-url>

   cd Employee-Management-API

2. ## Install Python and related packages
    sudo apt install python3.11 python3.11-venv python3.11-distutils

3. ## Create and activate a virtual environment
    python -m venv venv
    source venv/bin/activate 


    python3.11 -m venv venv311
    source venv311/bin/activate

4. ## Install project dependancies
   pip install flask flask_sqlalchemy flask_marshmallow marshmallow-sqlalchemy



5. ## Run the app 
    python app.py


6. ## Test the API using Postman
    Endpoints
    
    POST /employees - Create a new employee

    GET /employees - List of employees

    GET /employees/<id> - Get a single employee

    PUT /employees/<id> - Update employee details

    DELETE /employees/<id> - Delete an employee

# CONTRIBUTORS #
1. Alex Macharia.
   



