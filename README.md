#  project name:
NEIGHBORHOOD_WATCH


# AUTHOR
-EDWIKE NYAUNCHO

-FAITH MUTHONI


## Project description
This is a web application that allows the user to be in the loop about everything happening in his/her neighborhood and can find contact information of different facilities and businesses.


## USER STORY
-The user is able to sign in to the application to start using

-User is able to set a profile

-User can be able find a list of different businesses in the neighborhood 

-User is able to find important contact information like health departments

-User is able to create post visible for people of the neighbourhood

-User is able to change neighborhood when user moves out

-User is able to view details for a single neighborhood


## Setup Instructions and Installation
For the application to run, you have to install:

- python3.8

- Django framework

- virtual environment

- Postgres

Setup and Installation
- open terminal

- git clone this repository https://github.com/Edwike12/Neighborhood_Watch

- use a code editor

- Actvate the virtual env 

        -$ source venv/bin/activate

- Install dependancies 

        -$ pip install -r requirements.txt

- Create a database

        -psql

        -CREATE DATABASE neighborhood;

- .env file- create  .env file and hve the following filling where appropriate:

            -SECRET_KEY = '<Secret_key>'

            -DBNAME = 'neighborhood'

            -USER = '<Username>'

            -PASSWORD = '<password>'

            -DEBUG = True

- Run initial migration

        -$ python3.8 manage.py makemigrations share

        -$ python3.8 manage.py migrate

- Run the app

        -$ python3.8 manage.py runserver


## Technologies used
- python3.8

- Django

- Html, Css and Bootstrap

- postgreSql

- Heroku

- Restframework


## Known Bugs
There are no known bugs currently but pull requests are allowed incase you spot a bug


## Development 
Want to contribute? Great!

To fix a bug or enhance an existing module, follow these steps:
- Fork the repo
- Create a new branch (git checkout -b improve-feature)
- Make the appropriate changes in the files
- Add changes to reflect the changes made
- Commit your changes (git commit -am 'Improve feature')
- Push to the branch (git push origin improve-feature)
- Create a Pull Request


### Testing Application
-To run the tests for the class files:

    -$ python3.6 manage.py test




### contact information
Feel free to reach out:

Email: nyaunchoedwike@gmail.com




