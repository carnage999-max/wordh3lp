from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage, name= 'index' ),
    path('form-words/', views.IndexPage, name='home'),
    path('search/', views.DictionarySearch, name='dictionarysearch'),
]