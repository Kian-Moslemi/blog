from django.shortcuts import render,get_object_or_404
from .models import Article
from django.contrib.auth.models import User
import re
# Create your views here.

def post_lists(request):
    articles = Article.publish.all()
    return render(request,'blogs/list.html',{'articles':articles})

def post_detail(request, slug):
    article = Article.publish.get(slug=slug)
    return render(request,'blogs/detail.html',{'article':article})

def author(request):
    authors = User.objects.filter(Articles__isnull = False).distinct()
    return render(request,'blogs/authors.html',{'authors':authors})

def author_list(request,username):
    author = get_object_or_404(User,username=username)
    articles = Article.objects.filter(author=author)
    return render(request,'blogs/author_list.html',{'author':author,'articles':articles})

def author_detail(request,id,slug):
    author = Article.publish.get(id=id, slug=slug)
    return render(request,'blogs/author.html',{'author':author})


def search_articles(request):
    query = request.GET.get('q','')
    query = re.sub(r'\s+',' ',query).strip()
    results = []
    if query:
        results = Article.publish.filter(title__icontains=query)
    return render(request,'blogs/search_results.html',{'results':results,'query':query})

