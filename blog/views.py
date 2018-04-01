# -*- coding: utf-8 -*-

from blog.models import Post
from django.views.generic import ListView, DetailView, TemplateView
from django.views.decorators.csrf import ensure_csrf_cookie



class PostsListView(ListView): # представление в виде списка
    model = Post               # модель для представления
    paginate_by = 15




class PostDetailView(DetailView): # детализированное представление модели
    model = Post

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PostDetailView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['object_list'] = Post.objects.all()
        return context







