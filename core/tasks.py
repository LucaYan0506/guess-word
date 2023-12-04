from __future__ import absolute_import, unicode_literals
from core.models import Words
import random
import requests
from datetime import datetime


def get_random_word():
        if Words.objects.last() == None or Words.objects.last().date != datetime.today().date():
            today_word = generate_word() 
            words = Words(word=today_word, date=datetime.now())
            words.save()
        else:
            print('word already exists')

def generate_word():
    random_n = random.randint(1, 4580)

    f = open("/home/lucayan4/guess-word/guess_word_list.txt", "r")
    for x in range(random_n):
        res = f.readline().replace("\n","")
    f.close()

    return res