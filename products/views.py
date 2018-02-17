from django.conf import settings

from products.models import *
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import auth, messages
from django.core.mail import *
#send_mail, BadHeaderError
from .forms import ContactForm




def product(request, product_id):
    product = Product.objects.get(id=product_id)


    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            recipients = ['goldteamus@mail.tu']
            try:
                send_mail(email, message, settings.EMAIL_HOST_USER, ['goldteamus@mail.ru'])
                #send_mail(subject, message, 'e-mail отправителя', recipients)
            except BadHeaderError: #Защита от уязвимости
                return HttpResponse('Invalid header found')
            post = form.save()
            post.save()
            return render(request, 'thanks.html')
    else:
            form = ContactForm()



    print(request.session.session_key)


    return render(request, 'products/product.html', locals())



