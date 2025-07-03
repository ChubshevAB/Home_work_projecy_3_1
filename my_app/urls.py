from django.urls import path
from . import views
from my_app.apps import MyAppConfig
from my_app.views import CatalogListView, ProductDetailView, ContactsView, StartPageView, ProductCreateView


app_name = MyAppConfig.name

urlpatterns = [
    path('', StartPageView.as_view(), name='start_page'),
    path('catalog/', CatalogListView.as_view(), name='catalog'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('create/', ProductCreateView.as_view(), name='create_product')
]
