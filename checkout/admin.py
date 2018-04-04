# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import CartItem, Order, OrderItem

admin.site.register([CartItem, Order, OrderItem])

# Register your models here.
