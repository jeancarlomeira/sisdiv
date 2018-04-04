# coding=utf-8

from django.db import models
from django.core.urlresolvers import reverse
from django.forms.models import ModelForm
from django.forms.widgets import CheckboxSelectMultiple

class Category(models.Model):
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Identificador', max_length=100, unique=True, help_text="Preenchido automaticamente, não editar.",)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog:category', kwargs={'slug':self.slug})


class Unidades(models.Model):
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Identificador', max_length=100, unique=True, help_text="Preenchido automaticamente, não editar.",)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Unidade'
        verbose_name_plural = 'Unidades'
        ordering = ['name']

    def __str__(self):
        return self.name

class Product(models.Model):
    codigo = models.CharField('Código Comprasnet', max_length=6)
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Identificador', max_length=100, unique=True, help_text="Preenchido automaticamente, não editar.",)
    category = models.ForeignKey('catalog.Category', verbose_name='Categoria')
    description = models.TextField('Descrição')
    unid = models.ForeignKey('catalog.Unidades', verbose_name='Unidades')
    price = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    pregao = models.CharField('Pregão da última aquisição', max_length=8, help_text="Preencher no formato nnn/aaaa",)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog:product', kwargs={'slug':self.slug})
