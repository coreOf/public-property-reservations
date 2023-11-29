# Katica: public property reservation app

Public property reservation manager for Hackl 2023 hackathon

# Design resources
 - [wireframe](https://www.figma.com/file/FwuhjTwBp48uJxL4UofQaz/Hackl-Tim-%239?type=design&node-id=0%3A1&mode=design&t=MTpLHrVTZpxMIilI-1) in Figma
 - [tabler.io](https://tabler-icons.io/) icons


# Quick setup

```console
pip install -r requirements.txt
python manage.py migrate webapp
python manage.py migrate admin
python manage.py migrate sessions
python manage.py createsuperuser webapp
python manage.py runserver
```
