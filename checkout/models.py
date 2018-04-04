from django.db import models
from django.conf import settings
from catalog.models import Product, Unidades

class CartItemManager(models.Manager):
	def add_item(self,cart_key,product):
		if self.filter(cart_key=cart_key, product=product).exists():
			created = False
			cart_item = self.get(cart_key=cart_key, product=product)
			cart_item.quantity = cart_item.quantity + 1
			cart_item.save()
		else:
		    created = True
		    cart_item = CartItem.objects.create(
		        cart_key=cart_key, product=product, price=product.price, unid=product.unid, codigo=product.codigo, description=product.description
		    )
		return cart_item, created

class CartItem(models.Model):
	cart_key = models.CharField('Chave do Carrinho',max_length=40,db_index=True)
	product = models.ForeignKey('catalog.Product',verbose_name='Produto')
	quantity = models.PositiveIntegerField('Quantidade',default=1)
	price = models.DecimalField('Preço',decimal_places=2,max_digits=8)
	unid = models.ForeignKey('catalog.Unidades', verbose_name='Unidades')
	sub = models.DecimalField('Sub',decimal_places=2,max_digits=8)
	codigo = models.CharField('Código Comprasnet', max_length=6)
	description = models.TextField('Descrição')

	objects = CartItemManager()

	class Meta:
		verbose_name = 'Item do Carrinho'
		verbose_name_plural = 'Itens do Carrinho'
		unique_together = (('cart_key','product'),)

	def sub(self):
		return self.price * self.quantity

	def __str__(self):
		return '{} [{}]'.format(self.product,self.quantity, self.sub)

	def total(self):
		return "teste"

class OrderManager(models.Manager):
	def create_order(self,user,cart_itens):
		order = self.create(user = user)
		for cart_item in cart_itens:
			order_item = OrderItem.objects.create(order = order,product=cart_item.product,quantity=cart_item.quantity,price=cart_item.price,unid=cart_item.unid,codigo=cart_item.codigo,description=cart_item.description)
		return order

	def create_list(self,user,cart_itens):
		lista = self.create(user = user)
		for cart_item in cart_itens:
			list_item = OrderItem.objects.create(order = order,product=cart_item.product,quantity=cart_item.quantity,price=cart_item.price,unid=cart_item.unid,codigo=cart_item.codigo,description=cart_item.description)
		return lista

class Order(models.Model):

	STATUS_CHOICES = (
		(0,'Aguardando Publicação'),
		(1,'Concluida'),
		(2,'Cancelada'),
	)

	user = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name = "Usuário")
	status = models.IntegerField('Situação',choices=STATUS_CHOICES,default=0,blank=True)
	created = models.DateTimeField('Criado em',auto_now_add=True)
	modified = models.DateTimeField('Atualizado em',auto_now=True)

	objects = OrderManager()

	class Meta:
		verbose_name = 'Pedido'
		verbose_name_plural = 'Pedidos'

	def __str__(self):
		return 'Pedido #{}'.format(self.pk)

	def products(self):
		products_ids = self.itens.values_list('product')
		return Product.objects.filter(pk__in=products_ids)

	def total(self):
		aggregate_queryset = self.itens.aggregate(
			total=models.Sum(
				models.F('price') * models.F('quantity'), output_field=models.DecimalField()
			)
		)
		return aggregate_queryset['total']

class OrderItem(models.Model):
	order = models.ForeignKey(Order,verbose_name='Pedido',related_name='itens')
	product = models.ForeignKey('catalog.Product',verbose_name='Produto')
	quantity = models.PositiveIntegerField('Quantidade',default=1)
	price = models.DecimalField('Preço',decimal_places=2,max_digits=8)
	unid = models.ForeignKey('catalog.Unidades', verbose_name='Unidades')
	sub = models.DecimalField('Sub',decimal_places=2,max_digits=8,default='0.0')
	codigo = models.CharField('Código Comprasnet', max_length=6)
	description = models.TextField('Descrição', blank=True)

	class Meta:
		verbose_name = 'Item do Pedido'
		verbose_name_plural = 'Itens do Pedido'

	def sub(self):
		return self.price * self.quantity

	def __str__(self):
		return 'Pedido:{}, Produto:{}'.format(self.order,self.product,self.sub)

def post_save_cart_item(instance,**kwargs):
	if instance.quantity < 1:
		instance.delete()

models.signals.post_save.connect(post_save_cart_item,sender=CartItem,dispatch_uid='post_save_cart_item')
