from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('post/<int:post_id>', views.post, name="post"),
    path('all_posts/', views.all_posts, name="all_posts"),
    path('category/<int:cat_id>', views.category, name='category'),
    path('all_categories/', views.all_categories, name="all_categories"),
]