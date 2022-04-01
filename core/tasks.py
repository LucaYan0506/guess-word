from __future__ import absolute_import, unicode_literals
from celery import shared_task
from Guess_word.celery import app
import random,os
import requests
app.conf.update(BROKER_URL=os.environ['REDIS_URL'],
        CELERY_RESULT_BACKEND=os.environ['REDIS_URL'])

@shared_task
def get_random_word():
        today_word = generate_word() 
      
        url = 'http://127.0.0.1:8000/ksdjlfasadfasjfklha/'
        
        myobj = {
            'token':'jqw"£fds}dsfefhqwjehf23kasdfa!£*(£*$^"whfja"*JFKEAHr439',
            'new_word': today_word
            }

        x = requests.post(url, data = myobj)

        return x.text

def generate_word():
    random_n = random.randint(1, 5756)

    f = open("guess_word_list.txt", "r")
    for x in range(random_n):
        res = f.readline().replace("\n","")
    f.close()

    return res

@shared_task
def test1(test):
    return test