from articles.models import Article
from django.shortcuts import render, redirect

# Create your views here.
def new(request):
    return render(request, 'articles/new.html')


def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    img_path = request.POST.get('img_path')

    article = Article(title=title, content=content, img_path=img_path)
    article.save()

    return redirect('articles:detail', article.pk)


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
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.img_path = request.POST.get('img_path')
        article.save()
        return redirect('articles:detail', article.pk)
    else:
        return redirect('articles:detail', article.pk)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:home')
    else:
        return redirect('articles:detail', article.pk)
