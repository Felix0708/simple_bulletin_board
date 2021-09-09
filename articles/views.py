from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@require_safe
def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save()
            article.user = request.user
            article.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


@require_safe
def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comment_form = CommentForm()
    context = {
        'article': article,
        'comment_form': comment_form
    }
    return render(request, 'articles/detail.html', context)


@require_POST
def delete(request, pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=pk)
        if article.user.username == request.user.username:
            article.delete()
    return redirect('articles:index')


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if article.user.username == request.user.username:
        if request.method == 'POST':
            form = ArticleForm(request.POST, request.FILES, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
        context = {
            'article': article,
            'form': form,
        }
        return render(request, 'articles/update.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def comment_create(request, article_pk):
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.article_id = article_pk
            comment.save()
            return redirect('articles:detail', article_pk)
    else:
        comment_form = CommentForm()
    context = {
        'comment_form': comment_form,
    }
    return render(request, 'articles/detail.html', context)


@require_POST
def comment_delete(request, article_pk, pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=pk)
        if comment.user.username == request.user.username:
            comment.delete()
    return redirect('articles:detail', article_pk)


@require_http_methods(['GET', 'POST'])
def comment_edit(request, article_pk, pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment = get_object_or_404(Comment, pk=pk)
    if comment.user.username == request.user.username:
        if request.method == 'POST':
            form = CommentForm(request.POST, instance=comment) 
            if form.is_valid():
                comment = form.save()
                return redirect('articles:detail', article_pk)
        else : 
            form = CommentForm(instance=comment)
        context ={
            'article': article,
            'form' : form,
        }
        return render(request,'articles/comment_edit.html', context)