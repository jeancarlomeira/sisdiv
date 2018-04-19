from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, TemplateView
from .models import Product, Category
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


class ProductListView(LoginRequiredMixin,ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'product_list'
    paginate_by = 10

product_list = ProductListView.as_view()

class CategoryListView(LoginRequiredMixin,ListView):
    template_name = 'catalog/category.html'
    context_object_name = 'product_list'
    paginate_by = 10

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self,**kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['current_category'] = get_object_or_404(Category, slug=self.kwargs['slug'])
        return context

category = CategoryListView.as_view()

def product(request, slug):
    product = Product.objects.get(slug=slug)
    context = {
        'product': product,
    }
    return render(request, 'catalog/product.html', context)

class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'catalog/index.html'

index = IndexView.as_view()





#def unidade(request, slug):
#    unidade = Product.objects.get(slug=slug)
#    unid_filter = UnidadeFilter(request.GET, queryset=unidade)
#    return render(request, 'catalog/product.html', {'filter': unid_filter})

#def product_list(request):
#    context = {
#        'product_list': Product.objects.all()
#    }
#    return render(request, 'catalog/product_list.html', context)

#def category(request, slug):
#    category = Category.objects.get(slug=slug)
#    context = {
#        'current_category': category,
#        'product_list': Product.objects.filter(category=category),
#    }
#    return render(request, 'catalog/category.html', context)
