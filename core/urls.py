from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path('',views.index_view, name="index"),
    path('validating_word/',views.validating_word, name="validating_word"),
    path('ksdjlfasadfasjfklha/',views.update_word, name="update_word"),
]
