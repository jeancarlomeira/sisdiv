from django.db import models
from django.core.urlresolvers import reverse
from django.forms.models import ModelForm

class Search(models.Model):
    name_search = models.CharField('', max_length=500)
    slug = models.CharField('', default="1", max_length=1)

    class Meta:
        verbose_name = 'Nome'
        ordering = ['name_search']

    def __str__(self):
        return self.name_search
