release: sh -c 'python3 manage.py migrate && python3 manage.py makemigrations userapp && python3 manage.py migrate userapp'
web: gunicorn core.wsgi --preload --log-file