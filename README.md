# public-property-reservations
Public property reservation manager for Hackl 2023 hackathon

# Quick setup

```console
pip install -r requirements.txt
python manage.py migrate webapp
python manage.py migrate admin
python manage.py migrate sessions
python manage.py createsuperuser webapp
python manage.py runserver
```
