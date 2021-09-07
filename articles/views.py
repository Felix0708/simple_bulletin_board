from django import forms
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from articles.models import Article
from articles.forms import ArticleForm


# Create your views here.
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        img_path = request.POST.get('img_path')
        if form.is_valid():
            article = form.save()
            article = Article(img_path=img_path)
            article.user = request.user
            article.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/form.html', context)


@require_safe
def home(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles
    }
    return render(request, 'articles/home.html', context)


@require_safe
def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)


@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        if article.user == request.user:
            form = ArticleForm(request.POST, instance=article)
            article.img_path = request.POST.get('img_path')
            if form.is_valid():
                form.save()
                article.user = request.user
                article.save()
                return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form
    }
    return render(request, 'articles/form.html', context)


@require_POST
def delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if article.user == request.user:
        article.delete()
        return redirect('articles:home')
    else:
        return redirect('articles:detail', article.pk)
