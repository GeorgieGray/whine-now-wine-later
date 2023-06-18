from django import forms
from .models import Subscriber

class SubscriberForm(forms.Form):
    email = forms.EmailField(max_length=254)