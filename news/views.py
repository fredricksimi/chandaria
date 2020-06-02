from django.shortcuts import render, get_object_or_404, redirect
from .models import News
from .forms import CreateNewsForm, EditNewsForm
from django.utils.text import slugify
from django.utils import timezone


def news_view(request):
    news_posts = News.objects.all().order_by('-date_posted')[:5]
    context = {
        'news_posts': news_posts
    }
    return render(request, 'news/front-page.html', context)


def news_details_page(request, id, slug):
    news_post = get_object_or_404(News, id=id, slug=slug)
    context = {
        'news_post': news_post
    }
    return render(request, 'news/detail.html', context)
