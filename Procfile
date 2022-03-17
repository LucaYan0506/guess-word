web: gunicorn Guess_word.wsgi
worker: celery -A Guess_word beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
