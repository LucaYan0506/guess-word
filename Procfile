web: gunicorn Guess_word.wsgi
worker: celery -A Guess_word worker --beat --scheduler django --loglevel=info