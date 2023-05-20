from django.db import models
from django import forms
# Create your models here.
class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone_number = forms.IntegerField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)