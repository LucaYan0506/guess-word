from __future__ import absolute_import, unicode_literals
from celery import shared_task
from Guess_word.celery import app
import random,datetime,os
from . import views

app.conf.update(BROKER_URL=os.environ['REDIS_URL'],
        CELERY_RESULT_BACKEND=os.environ['REDIS_URL'])

@shared_task
def get_random_word():
    random_n = random.randint(1, 32246)

    f = open("word_list.txt", "r")
    for x in range(random_n):
        f.readline()
    views.today_word = f.readline().replace("\n","")
    f.close()
    print(views.today_word)
    return 1

@shared_task
def test1(test):
    return test