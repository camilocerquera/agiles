from django.db import models
from django import forms
from django.forms import ModelForm
from django.forms.widgets import DateInput,TextInput

class Urls(models.Model):
 url=models.CharField(max_length=2048)
 date=models.DateTimeField()
 user=models.CharField(max_length=16)
 
class UrlsForm(forms.Form):
	url 							= forms.CharField(required=True,widget=TextInput)
	user							= forms.CharField(required=True,widget=TextInput)

