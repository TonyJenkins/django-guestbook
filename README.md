# Django Guestbook

A simple guestbook in Django.

## Requirements

Uses Python 3.x. and tested with Django 1.11.4.

Database can use MySQL or SQLite. Configuration for both 
is in `settings.py`. Set to use SQLite by default. MySQL 
requires `mysqlclient` installed via `pip3`.
  
## To Run

If using MySQL, create the database, user, and grant 
permissions. Settings for these are in `settings.py`.

If using SQLite, create the database:

`$ python3 manage.py makemigrations`

`$ python3 manage.py migrate`

The program `populate_guestbook.py` can be used
load some sample data. (There is also a
`JSON` file in `fixtures`.)

`$ python3 populate_guestbook.py`

(The program includes some random pauses to 
prevent all the initial comments being at
precisely the same time.)

Then start the development server:

`$ python3 manage.py runserver`

The application will make itself available 
on port 8000 of `localhost`.
