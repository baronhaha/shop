from django.conf.urls import url, include
from django.contrib import admin
from landing import views

# redirects to static media files (css, javascript, images, etc.)

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^landing/$', views.landing, name='landing'),
]