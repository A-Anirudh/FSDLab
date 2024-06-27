Commands:
Create Virtual Environment on windows: `python -m venv venv`
on Linux: `python3 -m venv venv`

Activate venv: `venv\Scripts\Activate`
on Linux: `source venv\Scripts\Activate`

Install Djangoa and Pillow:
`pip install django pillow`

create project:
`django-admin startproject myproject`

`cd myproject`

`python manage.py startapp myapp`
# Add app in INSTALLED_APPS = [] in settings.py

`python manage.py makemigrations`
`python manage.py migrate`

`python manage.py createsuperuer`
`python manage.py shell` to open shell

`python manage.py runserver`
