release: python3 manage.py migrate && python3 manage.py migrate userapp
web: gunicorn core.wsgi --preload --log-file