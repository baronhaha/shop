# -*- coding: utf-8 -*-

from blog.models import Post
from django.views.generic import ListView, DetailView, TemplateView
from django.views.decorators.csrf import ensure_csrf_cookie
from hitcount.views import HitCountDetailView


class PostsListView(ListView): # представление в виде списка
    model = Post                   # модель для представления

class PostDetailView(DetailView): # детализированное представление модели
    model = Post


