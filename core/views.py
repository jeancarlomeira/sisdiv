# coding=utf-8
from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse
from django.views.generic import View, TemplateView, CreateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

User = get_user_model()

class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

index = IndexView.as_view()

class ContactView(LoginRequiredMixin, TemplateView):
    template_name = 'contact.html'

contact = ContactView.as_view()

class LawsView(LoginRequiredMixin, TemplateView):
    template_name = 'laws.html'

laws = LawsView.as_view()
