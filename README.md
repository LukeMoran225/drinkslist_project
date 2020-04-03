# Drinkslist

[![Generic badge](https://img.shields.io/badge/Drinkslist-PythonAnywhere-brightgreen.svg)](http://drinkslist.pythonanywhere.com/)

 The web application is designed to provide a one stop portal for both drinks industry professionals and consumers, to share, comment and rate drink specifications. Users will be able to view recipes without logging in, but if they have an account they can upload drinks and recipes, comment on and rate others, as well as follow people whos uploads they are interested in. The web app will provide a search feature for specific drinks, as well as a list of all uploaded drinks and a view of the top-rated ones. So users looking for a specific drink are catered to as well as those just browsing. The user profiles will show, if wanted by the user, email for further communication as well as a profile picture for familiarity.

## Setup

This project is based on Python 3.7.2. To set up the working environment with your own machine, using the following Anaconda command:

* switch to the desired working directory

```cmd
(base) C:\> cd Workspace
```

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

```cmd
(drinkslist) C:\>Workspace>drinkslist_project> pip install -r requirements.txt
```

---

* to initialise the database

```cmd
python manage.py makemigrations drinkslist
python manage.py migrate
python populate_<filename>.py
(drinkslist) C:\>Workspace>drinkslist_project> pip install -r requirements.txt
```

* to create a superuser account for database accessing

```cmd
(drinkslist) C:\>Workspace>drinkslist_project> python manage.py createsuperuser
```

## Running the Project

Once all the steps above are done, the project is already to run locally in [127.0.0.1:8000](http://127.0.0.1:8000/)
```cmd
(drinkslist) C:\>Workspace>drinkslist_project> python manage.py runserver
```

## Projrct Function

The app will offer a menu of drinks that all users can view, allowing you to enter the production of drinks.Interested users can follow the menu prompts to learn how to make their own drinks.Meanwhile, users can create accounts in the app to follow people or drinks they are interested in.The software also allows users to upload their own updates.


## Group members

Yao Du(Team D)
Ruofan Guo(Team D)
Gning Dai(Team D)
Jingqi Li(Team D)
Luke Moran(Team D)





