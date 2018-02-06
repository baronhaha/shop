from django.shortcuts import render
from .forms import SubscriberForm
from landing.models import *
from products.models import *



def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_develop = products_images.filter(product__category__id=1)
    products_images_pr = products_images.filter(product__category__id=2)
    return render(request, 'landing/home.html', locals())

def about(request):
    model = About.objects.get()

    return render(request, 'about.html', locals())