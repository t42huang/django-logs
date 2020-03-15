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

# apply database migration
python manage.py migrate

# start the development server
python manage.py runserver
```

## Reference

- [Python Crash Course - Eric Matthes](https://ehmatthes.github.io/pcc_2e/)
- [Django Framework - Documentation](https://docs.djangoproject.com/en/3.0)