from django.contrib import admin
from .models import Words
from .tasks import  get_random_word,test1
# Register your models here.

admin.site.register(Words)