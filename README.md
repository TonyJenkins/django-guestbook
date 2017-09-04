# Django Guestbook

A simple guestbook in Django.

* Uses Python 3.x. Tested with Django 1.11.4.
* Can use MySQL or SQLite.
  * (Configuration for both is in `settings.py`.)
  * MySQL requires `mysqlclient` installed via `pip3`.
  
To run:

* If using MySQL, create the database, user, and grant permissions.
* `$ python3 manage.py runserver`
* App is at `localhost:8000/guestbook`.
