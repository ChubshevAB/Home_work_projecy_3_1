from django.urls import path
from . import views
from my_app.apps import MyAppConfig
from my_app.views import start_page, product_detail


app_name = MyAppConfig.name

urlpatterns = [
    path('', start_page),
    path('catalog/', views.catalog, name='catalog'),
    path('contacts/', views.contacts, name='contacts'),
    path('<int:pk>/', product_detail, name='product_detail')
]
