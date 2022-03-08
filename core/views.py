from django.shortcuts import render
from django.http import JsonResponse
import random
from datetime import datetime

# Create your views here.
today_word = "world"
def index_view(request):
    diff = datetime.strptime("23:59:59", "%H:%M:%S") - datetime.strptime(datetime.now().time().strftime("%H:%M:%S" ), "%H:%M:%S")
    diff = str(diff).replace(":","h ",1)
    if (diff[1] == 'h'):
        diff = f"0{diff}"
    diff = str(diff).replace(":","min ",1)
    diff = f"{diff}sec"
    return render(request,'index.html',{
        'range':range(30),
        'time': diff
    })

def validating_word(request):
    global today_word
    temp = today_word
    word = request.GET.get('word')
    word = word.lower()

    check_letter = []

    for i in range(5):
        check_letter.append([word[i] in temp, word[i] == today_word[i]])
        if (word[i] in temp):
            temp = temp[:temp.find(word[i])] + " " + temp[temp.find(word[i]) + 1:]

    f = open("word_list.txt", "r")
    for x in f:
        if (x.replace("\n","") == word):
            f.close()
            return JsonResponse({
                'result': True,
                        #if letter is correct  #if position is correct
                "0": check_letter[0],
                "1": check_letter[1],
                "2": check_letter[2],
                "3": check_letter[3],
                "4": check_letter[4],
                },safe=False)
    f.close()

    return JsonResponse({'result': False},safe=False)

def get_random_word(request):
    global today_word
    random_n = random.randint(1, 32246)

    f = open("word_list.txt", "r")
    for x in range(random_n):
        f.readline()
    today_word = f.readline().replace("\n","")
    f.close()

    return JsonResponse({'today_word': today_word},safe=False)
