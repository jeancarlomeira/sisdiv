# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.generic import View, TemplateView, CreateView, ListView, UpdateView, FormView
from .models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import UserAdminCreationForm
from django.core.urlresolvers import reverse_lazy,reverse
from django.contrib.auth.forms import PasswordChangeForm

class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/index.html'

index = IndexView.as_view()

class RegisterView(CreateView):
    model = User
    template_name = 'accounts/register.html'
    form_class = UserAdminCreationForm
    success_url = reverse_lazy('index')

register = RegisterView.as_view()

class UpdateUserView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'accounts/update_user.html'
    fields = ['name', 'email']
    success_message = 'Usuario atualizado com sucesso'
    #success_url = reverse_lazy('accounts:index')
    def get_object(self):
        return self.request.user

    def get_success_url(self):
        view_name = 'accounts:index'
        return reverse_lazy(view_name)

update_user = UpdateUserView.as_view()

class UpdatePasswordView(LoginRequiredMixin,FormView):
    template_name = 'accounts/password_change.html'
    form_class = PasswordChangeForm
    success_url = reverse_lazy('accounts:index')
    def get_form_kwargs(self):
        kwargs = super(UpdatePasswordView,self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

password_change = UpdatePasswordView.as_view()

class UsersListView(ListView):
    model = User
    template_name = 'accounts/userlist.html'
    context_object_name = 'users'

userlist = UsersListView.as_view()
