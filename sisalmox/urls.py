# coding=utf-8

from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login, logout

from core import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    #url(r'^requisicao/$', views.requisicao, name='requisicao'),
    url(r'^contato/$', views.contact, name='contact'),
    url(r'^legislacao/$', views.laws, name='laws'),
    url(r'^entrar/$', login,{'template_name': 'login.html'}, name='login'),
    url(r'^sair/$', logout,{'next_page': 'index'}, name='logout'),
    url(r'^conta/', include('accounts.urls', namespace='accounts')),
    url(r'^pedidos/', include('checkout.urls', namespace='checkout')),
    url(r'^requisicao/', include('catalog.urls', namespace='catalog')),
    url(r'^pesquisar/', include('searchengine.urls', namespace='searchengine')),
]
