from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from articles.models import Article
from articles.forms import ArticleForm, SearchForm


def articles(request):
    draft_count = Article.objects.filter(status=Article.DRAFT).count()
    all_articles = Article.objects.filter(status=Article.PUBLISHED)
    return render(request, 'articles/articles.html', {'articles': all_articles, 'draft_count': draft_count})


def write(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles')
    else:
        form = ArticleForm()
    return render(request, 'articles/write.html', {'form': form})


def drafts(request):
    drafts = Article.objects.filter(status=Article.DRAFT)
    return render(request, 'articles/drafts.html', {'drafts': drafts})


def article(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'articles/article.html', {'article': article})


def edit(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'articles/edit.html', {'form': form})


def delete(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == 'POST':
        article.delete()
        return redirect('articles')
    return render(request, 'articles/delete.html', {'article': article})


def search(request):
    searchform = SearchForm()
    if request.POST:
        search_keyword = request.POST.get('search_term').strip()
        if len(search_keyword) == 0:
            return redirect('/search/')
        articles = Article.objects.filter(Q(title__icontains=search_keyword) | Q(content__icontains=search_keyword))
        form_with_search_term = SearchForm(initial={'search_term': search_keyword})
        return render(request, 'articles/search.html', {'form': form_with_search_term, 'articles': articles, 'search': True})
    return render(request, 'articles/search.html', {'form': searchform})
