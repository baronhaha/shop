#coding: utf-8
from django.conf.urls import *
from blog.views import PostsListView, PostDetailView, category


urlpatterns = [
url(r'^$', PostsListView.as_view(), name='list'), # то есть по URL http://имя_сайта/blog/
                                               # будет выводиться список постов
url(r'^(?P<pk>\d+)/$', PostDetailView.as_view(), name=''), # а по URL http://имя_сайта/blog/число/
                                              # будет выводиться пост с определенным номером


url(r'^category/(?P<slug>[-\w]+)/$', category, name='category'),

]