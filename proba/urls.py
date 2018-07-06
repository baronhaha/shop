"""proba URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include

from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from blog.models import BlogSitemap
from landing.models import AboutSitemap, Home
from products.models import ProductSitemap

admin.autodiscover() #automatic founding function of admin.py in our app's


sitemaps = {
    'home': Home,
    'posts': BlogSitemap,
    'about': AboutSitemap,
    'product': ProductSitemap,
}



urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('landing.urls')),
    url(r'^', include('products.urls')),
    url(r'^', include('orders.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^ratings/', include('star_ratings.urls', namespace='ratings', app_name='ratings')),
    url(r'hitcount/', include('hitcount.urls', namespace='hitcount')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    url('', include('social_django.urls', namespace='social')),



] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

