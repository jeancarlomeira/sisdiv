# coding=utf-8

from django.shortcuts import get_object_or_404,redirect, render
from django.views.generic import RedirectView, TemplateView, ListView, DetailView, View
from django.forms import modelformset_factory
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from catalog.models import Product, Unidades
from .models import CartItem,Order
from django.http import HttpResponse

class CreateCartItemView(LoginRequiredMixin,RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        product = get_object_or_404(Product, slug=self.kwargs['slug'])
        if self.request.session.session_key is None:
            self.request.session.save()
        cart_item, created = CartItem.objects.add_item(
            self.request.session.session_key, product
        )
        if created:
            messages.success(self.request, 'Produto adicionado com sucesso')
        else:
            messages.success(self.request, 'Produto atualizado com sucesso')
        return reverse('checkout:cart_item')

add_cart = CreateCartItemView.as_view()

class CartItemView(LoginRequiredMixin,TemplateView):
    template_name = 'checkout/cart.html'
    def get_formset(self, clear=False):
        CartItemFormSet = modelformset_factory(
            CartItem, fields=('quantity',), can_delete=True, extra=0
        )

        session_key = self.request.session.session_key
        if session_key:
            if clear:
                formset = CartItemFormSet(
                    queryset=CartItem.objects.filter(cart_key=session_key)
                )
            else:
                formset = CartItemFormSet(
                    queryset=CartItem.objects.filter(cart_key=session_key),
                    data=self.request.POST or None
                )
        else:
            formset = CartItemFormSet(queryset=CartItem.objects.none())
        return formset

    def get_context_data(self, **kwargs):
        context = super(CartItemView, self).get_context_data(**kwargs)
        context['formset'] = self.get_formset()
        return context

    def post(self, request, *args, **kwargs):
        formset = self.get_formset()
        context = self.get_context_data(**kwargs)
        if formset.is_valid():
            formset.save()
            messages.success(request, 'Pedido atualizado com sucesso')
            context['formset'] = self.get_formset(clear=True)
        return self.render_to_response(context)

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

cart_item = CartItemView.as_view()

class CheckoutView(LoginRequiredMixin,TemplateView):
    template_name = 'checkout/checkout.html'
    def get(self,request,*args,**kwargs):
        session_key = request.session.session_key
        if session_key and CartItem.objects.filter(cart_key = session_key).exists():
            cart_itens = CartItem.objects.filter(cart_key = session_key)
            order = Order.objects.create_order(user=request.user,cart_itens = cart_itens)
            cart_itens.delete()
        else:
            messages.warning(request,'Não há itens no pedido')
            return redirect('checkout:cart_item')
        return super(CheckoutView,self).get(request,*args,**kwargs)

checkout = CheckoutView.as_view()

class OrderListView(LoginRequiredMixin, ListView):
    template_name = 'checkout/order_list.html'
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

order_list = OrderListView.as_view()

class OrderDetailView(LoginRequiredMixin, DetailView):
    template_name = 'checkout/order_detail.html'
    paginate_by = 2
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

order_detail = OrderDetailView.as_view()

class Confirmation(LoginRequiredMixin, TemplateView):
    template_name = 'checkout/confirmation.html'
    def get(self,request,*args,**kwargs):
        session_key = request.session.session_key
        if session_key and CartItem.objects.filter(cart_key = session_key).exists():
            return render(request,'checkout/confirmation.html')
        else:
            messages.warning(request,'Não há itens no pedido')
            return redirect('checkout:cart_item')

confirmation = Confirmation.as_view()

class PrintPdf(LoginRequiredMixin, DetailView):
    template_name = 'checkout/printpdf.html'
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

printpdf = PrintPdf.as_view()
