web: gunicorn Guess_word.wsgi
worker: celery -A Guess_word worker -l info
worker: celery -A Guess_word beat -l INFO