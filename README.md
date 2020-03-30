# Drinkslist

[<img src="https://img.shields.io/badge/Drinkslist-PythonAnywhere-brightgreen.svg" alt="made with python">](http://drinkslist.pythonanywhere.com/)

description text here

## Setup

This project is based on Python 3.7.2. To set up the working environment with your own machine, using the following Anaconda command:

* switch to the desired working directory

`(base) C:\> cd Workspace`

* create and activate a virtual environment for the project

```cmd
(base) C:\>Workspace> conda create -n drinkslist python=3.7.2
(base) C:\>Workspace> conda activate drinkslist
(drinkslist) C:\>Workspace>
```

* clone the project repository and hava a check

```cmd
(drinkslist) C:\>Workspace> git clone https://github.com/LukeMoran225/drinkslist_project.git
(drinkslist) C:\>Workspace> cd drinkslist_project
```

## Dependencies & Database Configuration

Note that there are several dependencies required for running the project.

* to install all the dependencies:

`(drinkslist) C:\>Workspace>drinkslist_project> pip install -r requirements.txt`

---

* to initialise the database

```cmd
python manage.py makemigrations drinkslist
python manage.py migrate
python populate_<filename>.py
```

* to create a superuser account for database accessing

`(drinkslist) C:\>Workspace>drinkslist_project> python manage.py createsuperuser`

## Running the Project

Once all the steps above are done, the project is already to run locally in [127.0.0.1:8000](http://127.0.0.1:8000/)

`(drinkslist) C:\>Workspace>drinkslist_project> python manage.py runserver`
