# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from blog.models import *
from django.utils import timezone
from django.views.generic import ListView, DetailView, TemplateView
from django.views.decorators.csrf import ensure_csrf_cookie
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class PostsListView(ListView): # представление в виде списка
    model = Post # модель для представления

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PostsListView, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        return context



class PostDetailView(DetailView): # детализированное представление модели
    model = Post

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PostDetailView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['object_list'] = Post.objects.all()

        context['category_list'] = Category.objects.all()
        return context




def category(request, slug):
    category = Category.objects.get(slug=slug)
    post = Post.objects.filter(category=category)
    paginator = Paginator(post, 3)
    page = request.GET.get('page')
    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)
    return render(request, 'blog/category.html', {
        'category': category,
        'page': page,
        'post': post})





