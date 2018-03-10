from django.conf.urls import url, include
from django.contrib import admin
from landing import views
from django.views.generic import TemplateView


# redirects to static media files (css, javascript, images, etc.)

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),

    url(r'^serviceworker.js', (TemplateView.as_view(
        template_name="serviceworker.js",
        content_type='application/javascript',
    )), name='serviceworker.js'),

url(r'^serviceworker-update.js', (TemplateView.as_view(
        template_name="serviceworker-update.js",
        content_type='application/javascript',
    )), name='serviceworker-update.js'),

url(r'^manifest.json', (TemplateView.as_view(
        template_name="manifest.json",
        content_type='application/javascript',
    )), name='manifest.json'),

]