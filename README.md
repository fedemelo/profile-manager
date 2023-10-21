# profile-manager
Basic web application to observe the profile of employees in a company

## Description

RESTful API to manage the profile of employees in a company. The API is developed in Python using the FastAPI framework and the data is stored in a SQLite relational database.

## Installation

### Requirements

- Python 3.8 or higher
- pip (Python package manager)
- virtualenv (Python virtual environment manager)

## Steps to run the application

1. Clone the repository
You can clone the repository using the following command:
```bash
git clone https://github.com/fedemelo/profile-manager-back
```

2. Create a virtual environment with the dependencies

Install virtualenv using pip:
```bash
pip install virtualenv
```

Create a virtual environment:
```bash
python -m virtualenv env 
```

Activate the virtual environment:
```bash
env\Scripts\activate.bat
```

Install the dependencies:
```bash
pip install -r requirements.txt.
```

3. Run the application

Run the application using the following command:
```bash
uvicorn src.main:app --reload
```

The application will be running on http://127.0.0.1:8000/.

You can access the application through a browser or using a tool like Postman.

## API Documentation

The API documentation is available at http://127.0.0.1:8000/, created automatically by Swagger UI.

The API contains endpoints to manage actions related with employees and their skills.

It contains one extra endpoint to manage logins. The /logins/create endpoint is used to add a valid user that will be able to access the application through the frontend.