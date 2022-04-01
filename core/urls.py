from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path('',views.index_view, name="index"),
    path('validate_today_word/',views.validate_today_word, name="validate_today_word"),
    path('ksdjlfasadfasjfklha/',views.update_word, name="update_word"),
    path('unlimited/',views.unlimited_view, name="unlimited"),
    path('validate_words/',views.validate_words, name="validate_words"),
    path('next_word/',views.next_word, name="next_word"),
]
