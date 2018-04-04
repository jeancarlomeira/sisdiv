# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView, CreateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib import messages

from .forms import ContactForm

User = get_user_model()

class IndexView(TemplateView):
    template_name = 'index.html'

index = IndexView.as_view()

def contact(request):
    success = False
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.send_mail()
        success = True
    elif request.method == 'POST':
        messages.error(request, 'Formulário inválido')
    context = {
        'form': form,
        'success': success
    }
    return render(request, 'contact.html', context)

#def index(request):
#    return render(request, 'index.html')
