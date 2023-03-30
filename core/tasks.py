from __future__ import absolute_import, unicode_literals
import random
import requests

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

    f = open("/home/lucayan4/guess-word/guess_word_list.txt", "r")
    for x in range(random_n):
        res = f.readline().replace("\n","")
    f.close()

    return res