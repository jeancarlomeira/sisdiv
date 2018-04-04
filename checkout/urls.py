from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^pedido/adicionar/(?P<slug>[\w_-]+)/$', views.add_cart, name='add_cart'),
   	url(r'^relacao/$', views.cart_item, name='cart_item'),
   	url(r'^finalizar/$', views.checkout, name='checkout'),
   	url(r'^finalizando/$', views.confirmation, name='confirmation'),
   	url(r'^meus-pedidos/$', views.order_list, name='order_list'),
   	url(r'^meus-pedidos/(?P<pk>\d+)/$', views.order_detail, name='order_detail'),
   	url(r'^imprimir/(?P<pk>\d+)/$', views.printpdf, name='printpdf'),
]
