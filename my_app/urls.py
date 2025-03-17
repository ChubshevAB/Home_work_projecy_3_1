from django.urls import path
from . import views
from my_app.apps import MyAppConfig
from my_app.views import start_page


app_name = MyAppConfig.name

urlpatterns = [
    path('main_page/', views.main_page, name='main_page'),
    path('contacts/', views.contacts, name='contacts'),
    path('', start_page)
]
