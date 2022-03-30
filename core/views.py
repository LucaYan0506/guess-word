from django.shortcuts import render
from django.http import JsonResponse
from .tasks import get_random_word
from datetime import datetime
from core.models import Words
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
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
    if Words.objects.last().date != datetime.today().date():
        get_random_word()
        print('not match')

    today_word = Words.objects.last().word
    word = request.GET.get('word')
    word = word.lower()

    check_letter = []

    for i in range(5):
                        #if letter is correct  #if position is correct
        check_letter.append([word[i] in today_word, word[i] == today_word[i]])
        if (word[i] in today_word):
            today_word = today_word[:today_word.find(word[i])] + " " + today_word[today_word.find(word[i]) + 1:]

    f = open("word_list.txt", "r")
    for x in f:
        if (x.replace("\n","") == word):
            f.close()
            return JsonResponse({
                'result': True,
                "0": check_letter[0],
                "1": check_letter[1],
                "2": check_letter[2],
                "3": check_letter[3],
                "4": check_letter[4],
                },safe=False)
    f.close()

    return JsonResponse({'result': False},safe=False)


@csrf_exempt
def update_word(request):
    if (request.method == 'POST'):
        if (request.POST['token'] == 'jqw"£fds}dsfefhqwjehf23kasdfa!£*(£*$^"whfja"*JFKEAHr439'):
            today_word = request.POST['new_word']
            words = Words(word=today_word, date=datetime.now())
            words.save()
            print('dd')
            return JsonResponse({'result':'1'},safe=False)
    return JsonResponse({'result':'0'},safe=False)
    