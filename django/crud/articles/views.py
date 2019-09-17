from django.shortcuts import render, redirect
from .models import Article


# Create your views here.

def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'index.html', context)

def new(request):
    return render(request, 'new.html')

def create(request):
    title = request.GET.get("title")
    content = request.GET.get("content")

    article = Article()
    article.title = title
    article.content = content
    article.save()
    
    return redirect(index)

    