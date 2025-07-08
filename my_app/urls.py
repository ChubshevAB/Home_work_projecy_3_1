from django.urls import path
from . import views
from my_app.apps import MyAppConfig
from my_app.views import (CatalogListView, ProductDetailView, ContactsView, StartPageView, ProductCreateView,
                          ProductUnpublishView, ProductDeleteView, ProductsByCategoryView, CategoriesListView)


app_name = MyAppConfig.name

urlpatterns = [
    path('', StartPageView.as_view(), name='start_page'),
    path('catalog/', CatalogListView.as_view(), name='catalog'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('product/<int:pk>/unpublish/', ProductUnpublishView.as_view(), name='unpublish_product'),
    path('product/<int:pk>/publish/', views.ProductPublishView.as_view(), name='publish_product'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='delete_product'),
    path('category/<int:category_id>/', ProductsByCategoryView.as_view(), name='products_by_category'),
    path('categories/', CategoriesListView.as_view(), name='categories_list'),
]
