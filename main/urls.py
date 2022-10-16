from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexPage, name='home'),
    path('search/', views.DictionarySearch, name='dictionarysearch'),
]
