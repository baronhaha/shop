from django.conf.urls import url, include
from django.contrib import admin
from . import views

# redirects to static media files (css, javascript, images, etc.)

urlpatterns = [
    #url(r'^landing/$', views.landing, name='landing'),
    url(r'^basket_adding/$', views.basket_adding, name='basket_adding'),
    url(r'^checkout/$', views.checkout, name='checkout'),
    url(r'^chat/$', views.chat, name='chat'),
    url(r'^order/$', views.order, name='order'),

]