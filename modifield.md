py.exe -m venv venv OU pyhon -m venv venv
Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser
.\venv\Scripts\activate.ps1
pip install djangorestframework
django-admin startproject projeto .
    Em seguida: Pasta Projetos > settings.py  em INSTALED APPS acrescentar 'rest_framework'

python .\manage.py startapp todo
    'todo'
python migrate
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

nome, autor, preço
