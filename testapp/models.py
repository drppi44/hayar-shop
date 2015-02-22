from django.db import models
from django.contrib.contenttypes.models import ContentType

class Product(models.Model):
	name=models.CharField(max_length=100)
	description=models.CharField(max_length=1000,default="description of the Product")
	price=models.IntegerField(default=500)
	date=models.DateTimeField(auto_now_add=True)
	url=models.URLField(max_length=100,blank=True,default='')
	subcategory=models.ForeignKey('SubCategory',blank=True,default='')
	def __unicode__(self):
		return self.name

class Category(models.Model):
	name=models.CharField(max_length=100,blank=True)
	url=models.CharField(max_length=100,blank=True,default='')
	def __unicode__(self):
		return self.name

class SubCategory(models.Model):
	name=models.CharField(max_length=100,blank=True)
	category=models.ForeignKey('Category',blank=True)
	def __unicode__(self):
		return self.name

class Param(models.Model):
	product=models.ForeignKey('Product')
	name=models.CharField(max_length=100)
	value=models.CharField(max_length=100)
	def __unicode__(self):
		return self.name

class Customer(models.Model):
	first_name=models.CharField(max_length=100)
	second_name=models.CharField(max_length=100)
	def __unicode__(self):
		return self.first_name, self.second_name

class Order(models.Model):
	customer=models.ForeignKey('Customer',blank=True,default='')
	list_id_product=models.CharField(max_length=100)

class TopMenu(models.Model):
	name=models.CharField(max_length=100)
	url=models.CharField(max_length=100)
	def __unicode__(self):
		return self.name

class Cart(models.Model):
	date=models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return unicode(self.date)

class Item(models.Model):
	cart=models.ForeignKey(Cart)
	quantity=models.PositiveIntegerField()
	item_price=models.DecimalField(max_digits=18,decimal_places=2)
	product_id=models.PositiveIntegerField()
	@property
	def total_price(self):
		return self.quantity*self.item_price
	@property
	def product(self):
		return Product.objects.get(id=self.product_id)
	@product.setter
	def product(self,product_instance):
		self.product_id=product_instance.id







