from django import forms
from .models import *

class CheckoutContactForm(forms.Form):
    name = forms.CharField(required=True)
    phone = forms.CharField(required=True)

#Форма обратной связи
class ContactForm(forms.ModelForm):
    #fields

    class Meta:
        model = Ordercontact
        fields = "__all__"

