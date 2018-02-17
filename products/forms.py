from django import forms
from .models import Contact
from .models import *

#class SubscriberForm(forms.ModelForm):
#
#    class Meta:
#        model = Subscriber#        exclude = [""]
#Форма обратной связи
class ContactForm(forms.ModelForm):
    #fields

    class Meta:
        model = Contact
        fields = "__all__"