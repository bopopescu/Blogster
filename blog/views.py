from django.shortcuts import render, render_to_response, get_object_or_404
from .models import Category, Blog


def index(request):
    return render_to_response('index.html', {
        # 'latest_post': Blog.objects.latest('posted'),
        'categories': Category.objects.all(),
        'posts': Blog.objects.all()
    })

def view_post(request, post_id):
    return render_to_response('view_post.html', {
        'post': get_object_or_404(Blog, id=post_id)
    })

def view_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    return render_to_response('view_category.html', {
        'category': category,
        'posts': Blog.objects.filter(category=category)[:5]
    })