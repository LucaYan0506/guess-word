from __future__ import absolute_import, unicode_literals
from celery import shared_task
from Guess_word.celery import app
from .models import Words
import random,datetime,os

app.conf.update(BROKER_URL=os.environ['REDIS_URL'],
        CELERY_RESULT_BACKEND=os.environ['REDIS_URL'])

@shared_task
def get_random_word():
    random_n = random.randint(1, 32246)

    f = open("word_list.txt", "r")
    for x in range(random_n):
        f.readline()
    today_word = f.readline().replace("\n","")
    f.close()
    words = Words(word=today_word, date=datetime.datetime.now())
    words.save()

@shared_task
def test1(test):
    return test