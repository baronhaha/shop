from django.conf.urls import url, include
from django.contrib import admin
from landing import views
from django.views.generic import TemplateView


# redirects to static media files (css, javascript, images, etc.)

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),

    url(r'^OneSignalSDKWorker.js', (TemplateView.as_view(
        template_name="../templates/OOneSignalSDKWorker.js",
        content_type='application/javascript',
    )), name=OneSignalSDKWorker.js'),

url(r'^OneSignalSDKUpdaterWorker.js', (TemplateView.as_view(
        template_name="../templates/OneSignalSDKUpdaterWorker.js",
        content_type='application/javascript',
    )), name='OneSignalSDKUpdaterWorker.js'),

url(r'^manifest.json', (TemplateView.as_view(
        template_name="../templates/manifest.json",
        content_type='application/javascript',
    )), name='manifest.json'),

]