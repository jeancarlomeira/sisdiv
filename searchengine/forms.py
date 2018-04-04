# coding=utf-8
from django.contrib.auth. forms import UserCreationForm
from django import forms
from .models import Search


class SearchForm(forms.ModelForm):
    class Meta:
        model = Search
        fields = ['name_search']
