# Django Logger

## Steps

- check and make sure your python version is python 3: `python -V`
  - install python 3 if it is not installed (google it if you don't know how)
- go to this project root directory: `cd logger`
- create virtual environment (venv): `python -m venv venv-logger`
- activate the venv: `source venv-logger/bin/activate`
- install project dependencies: `pip install -r requirements.txt`
  - Note: content in requirements.txt comes from `pip freeze > requirements.txt`

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

```

## Reference

- [Python Crash Course - Eric Matthes](https://ehmatthes.github.io/pcc_2e/)
- [Django Framework - Documentation](https://docs.djangoproject.com/en/3.0)