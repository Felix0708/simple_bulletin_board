from django.contrib.auth.models import User
from articles.models import Article
from django.shortcuts import render, redirect
from django import forms
from articles.forms import ArticleForm


# Create your views here.
def new(request):
    form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/new.html', context)


def create(request):
    form = ArticleForm(request.POST)
    #유효성 검사
    if form.is_valid():
        article = form.save()
        article.user = request.user
        article.save()
        return redirect('articles:detail', article.pk)
    return redirect('articles:new')


    # # if request.user.is_authenticated:
    # if request.method == "POST":
    #     title = request.POST.get('title')
    #     content = request.POST.get('content')
    #     user = request.user
    #     img_path = request.POST.get('img_path')
    #     article = Article(title=title, content=content, user=user, img_path=img_path)
    #     article.save()
    #     return redirect('articles:detail', article.pk)
    # # else:
    # #     return redirect('accounts:login')
    # else:
    #     return redirect('articles:home')


def home(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles
    }
    return render(request, 'articles/home.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)


def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article
    }
    return render(request, 'articles/edit.html', context)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        if article.user == request.user:
            article.title = request.POST.get('title')
            article.content = request.POST.get('content')
            article.user = request.user
            article.img_path = request.POST.get('img_path')
            article.save()
            return redirect('articles:detail', article.pk)
        else:
            return redirect('articles:detail', article.pk)
    else:
        return redirect('articles:detail', article.pk)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        if article.user == request.user:
            article.delete()
            return redirect('articles:home')
        else:
            return redirect('articles:detail', article.pk)
    else:
        return redirect('articles:detail', article.pk)
