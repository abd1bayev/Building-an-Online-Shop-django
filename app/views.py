from django.shortcuts import render
from django.utils import timezone
from .models import Post


def home(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})