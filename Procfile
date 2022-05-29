release: python3 manage.py migrate
release: python3 manage.py makemigrations userapp
release: python3 manage.py migrate userapp
web: gunicorn core.wsgi --preload --log-file -