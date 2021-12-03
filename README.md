# Employee Management System (EMS)
This is a simple EMS based on Django.

## Setup
It is recommended to first make a Python virtual environment.

```
python3 -m venv venv
source venv/bin/activate
```

After initialising the virtual environment, you can install the dependencies using

```
pip install -r requirements.txt
```

Make all necessary migrations, and start the django server!

```
python manage.py migrate
python manage.py runserver
```

You can view the project live at `localhost:8000`.

## Usage
There are two basic models in this project - Departments and Employees. Every employee is associated with a particular department.

For the project to work properly, first start by making a few departments. Then, you can add various employees to the employee register.

## Further Expansion

Add authorisation and authentication, so that only logged in users (preferrably superusers) have access to create, edit and delete functionalities.
