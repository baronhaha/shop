from django.shortcuts import render
from .forms import *
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

def landing(request):
    name = "Goldteam"
    current_day = "10.02.2018"
    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print (request.POST)
        print (form.cleaned_data)
        data  = form.cleaned_data
        print (data["name"])

        new_form = form.save()

    return render(request, 'products/product.html', locals())

