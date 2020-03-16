# Django Logger

## Steps

- check and make sure your python version is python 3: `python -V`
  - install python 3 if it is not installed (google it if you don't know how)
- go to this project root directory: `cd logger`
- create virtual environment (venv): `python -m venv venv-logger`
- activate the venv: `source venv-logger/bin/activate`
- install project dependencies: `pip install -r requirements.txt`
  - Note: content in requirements.txt comes from `pip freeze > requirements.txt`

## Deploy on Heroku

```bash
# prerequisites:
# - make sure you are in your project root directory
# - the project is git tracked
# - create your own free heroku account, then log in from the terminal:
$ heroku login -i

# run the following command to check current remote(s) of this repo, if there is any:
git remote -v

# then, in the project root directory, run this to create a heroku app
$ heroku create <appname>
Creating <appname>... done
https://<appname>.herokuapp.com/ | https://git.heroku.com/<appname>.git

For Example:
https://tinas-django-logs.herokuapp.com/ | https://git.heroku.com/tinas-django-logs.git

# run the following command again to confirm that the remote - heroku is added:
git remote -v

# then, push this project repo to heroku
git push heroku master

# now the app should be up running on heroku
# to check the server started correctly, run
heroku ps

# if all is well, you can go check the app on https://<appname>.herokuapp.com/, or run the following to open the link in a browser tab:
heroku open
```

## Logs

```bash
# bootstrap the project
django-admin startproject djlogger .
# apply initial database migration
python manage.py migrate
# start the development server
python manage.py runserver
## check out the website at: http://127.0.0.1:8000/

# create an app
python manage.py startapp djlogs

# add class Topic to app model, then make migrations, then migrate
python manage.py makemigrations djlogs
python manage.py migrate

# create admin superuser
python manage.py createsuperuser
## register Topic in admin.py to allow admin to manage topics, then
## check out the website at: http://127.0.0.1:8000/admin
## now you can add/update/delete/list topics in the Topic table

# add class Entry to app model, then make migrations, then migrate
python manage.py makemigrations djlogs
python manage.py migrate

# introduce Django shell, another way to manage the shell
python manage.py shell
>>> from djlogs.models import Topic
>>> Topic.objects.all()
<QuerySet [<Topic: Python>, <Topic: Django>, <Topic: Flask>, <Topic: Python>]>
>>> from djlogs.models import Entry
>>> Entry.objects.all()
<QuerySet [<Entry: Python is great!...>, <Entry: Flask is cool!...>, <Entry: Django is awesome!...>]>
>>> entries = Entry.objects.all()
>>> for entry in entries:
...   print(entry.text, entry.topic)
...
Python is great! Python
Flask is cool! Flask
Django is awesome! Django


# create anther app for user authentication
python manage.py startapp users
## use Django's default view and user model

>>> from django.contrib.auth.models import User
>>> User.objects.all()
<QuerySet [<User: bob>, <User: john>]>
>>> for user in User.objects.all():
...   print(user.id, user.username)
...
1 bob
2 john

# Migrate the database after adding foreign key relationship between Topic and User tables.
python manage.py makemigrations djlogs
python manage.py migrate

# check if topics have owner now
>>> from djlogs.models import Topic
>>> for topic in Topic.objects.all():
...   print(topic, topic.owner)
...
Django bob
Flask bob
Python bob
PyGame bob

```

## Reference

- [Python Crash Course - Eric Matthes](https://ehmatthes.github.io/pcc_2e/)
- [Django Framework - Documentation](https://docs.djangoproject.com/en/3.0)