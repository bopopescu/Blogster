from django.contrib import admin
from .models import Blog, Category
from django.contrib import admin

# class BlogPostAdmin(admin.ModelAdmin):
#     fields = ('url', 'title', 'body')

admin.site.register(Blog)
admin.site.register(Category)
