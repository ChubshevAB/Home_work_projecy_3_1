from django.urls import path
from .views import BlogPostListView, BlogPostDetailView, BlogPostCreateView, BlogPostUpdateView, BlogPostDeleteView, StartPageView

app_name = 'blog'

urlpatterns = [
    path('', StartPageView.as_view(), name='start_page'),
    path('post_list/', BlogPostListView.as_view(), name='post_list'),
    path('create/', BlogPostCreateView.as_view(), name='post_create'),
    path('<int:pk>/', BlogPostDetailView.as_view(), name='post_detail'),
    path('<int:pk>/update/', BlogPostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/delete/', BlogPostDeleteView.as_view(), name='post_delete'),
]
