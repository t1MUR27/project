from django.shortcuts import render
from .models import Category, Article

# Create your views here.


def index(request):
    articles = Article.objects.all()
    categories = Category.objects.all()
    contex = {
        'articles': articles,
        'categories': categories
    }
    return render(request, 'blog/index.html', contex)
