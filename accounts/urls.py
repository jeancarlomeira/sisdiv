# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^alterar-dados/$', views.update_user, name='update_user'),
    url(r'^alterar-senha/$',views.password_change,name='password_change'),
    url(r'^usuarios/$',views.userlist,name='userlist'),
    url(r'^registro/$', views.register, name='register')
]
