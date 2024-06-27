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
 Add app in INSTALLED_APPS = [] in settings.py

`python manage.py makemigrations`
<br>
`python manage.py migrate`
<br>

`python manage.py createsuperuer`
<br>

`python manage.py shell` to open shell
<br>

`python manage.py runserver`
