from django.urls import path
from . import views


app_name = 'main_page'

urlpatterns = [
    path('main_page/', views.main_page, name='main_page'),
    path('contacts/', views.contacts, name='contacts'),
]
