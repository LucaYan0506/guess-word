from __future__ import absolute_import, unicode_literals
import random
import requests

def get_random_word():
        today_word = generate_word() 

        url = 'https://lucayan4.pythonanywhere.com/ksdjlfasadfasjfklha/'
        
        myobj = {
            'token':'jqw"£fds}dsfefhqwjehf23kasdfa!£*(£*$^"whfja"*JFKEAHr439',
            'new_word': today_word
            }

        x = requests.post(url, data = myobj)

        return x.text

def generate_word():
    random_n = random.randint(1, 4580)

    f = open("/home/lucayan4/guess-word/guess_word_list.txt", "r")
    for x in range(random_n):
        res = f.readline().replace("\n","")
    f.close()

    return res