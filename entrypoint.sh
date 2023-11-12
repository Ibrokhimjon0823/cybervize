python manage.py migrate &&
python fixtures/fixtures.py &&
python manage.py runserver 0.0.0.0:8000