from django.forms import ModelForm
from .models import Page
from django import forms

class PageForm(ModelForm):
    class Meta:
       model = Page
       fields = ['title', 'body', 'page_date', 'picture']
       widgets = {
           'page_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'style': 'width: 200px'})
       }