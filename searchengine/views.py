from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.template import RequestContext
from django.contrib import messages
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from .forms import SearchForm
from catalog.models import Product
from .models import Search
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

class ResultsView(LoginRequiredMixin,ListView):
    template_name = 'catalog/product_list.html'
    context_object_name = 'product_list'
    paginate_by = 2

    def get_queryset(self):
        queryset = Product.objects.all()
        q1 = Search.objects.get(slug='1')
        q2 = queryset.filter(name__icontains=q1)
        q3 = queryset.filter(codigo__icontains=q1)
        if queryset.filter(name__icontains=q1):
            return q2
        if queryset.filter(codigo__icontains=q1):
            return q3
        else:
            messages.warning(self.request,'O item pesquisado não existe')
            return queryset

results = ResultsView.as_view()

def search(request):
    itens = Search.objects.all()
    itens.delete()
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('searchengine:results')
    else:
        form = SearchForm()
    return render(request, 'searchengine/search.html', {'form': form})
