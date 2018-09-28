from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path(r'', views.index, name='index-page'),
    path('view/<int:post_id>', views.view_post, name='view_blog_post'),
    path('category/<int:category_id>', views.view_category, name='view_posts_by_category')
]
