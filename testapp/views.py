# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.views.generic import View
from models import *
from cart import Cart

#----------------------
#Вьюшка для наследования
class MainView(View):
	render_dict={}
	html=''
	#------------------
	#Ф-я для задания параметров Home страници
	def set_params_home(self):
		self.html='index.html'
		self.render_dict={
			'topMenu_list':TopMenu.objects.all(),
			'category_list':Category.objects.all(),
		}
		for i in range(len(self.render_dict['topMenu_list'])):
			if self.render_dict['topMenu_list'][i].url=='':
				self.render_dict['topMenu_list'][i].active=True
	def set_params_productDetail(self,id):
		self.html='item.html'
		self.render_dict={
			'topMenu_list':TopMenu.objects.all(),
			'category_list':Category.objects.all(),
			'product':Product.objects.get(id=id),
		}
		for i in range(len(self.render_dict['topMenu_list'])):
			if self.render_dict['topMenu_list'][i].url=='catalog':
				self.render_dict['topMenu_list'][i].active=True
	def set_params_catalog(self):
		self.html='catalog.html'
		self.render_dict={
			'topMenu_list':TopMenu.objects.all(),
			'category_list':Category.objects.all(),
			'product_list':Product.objects.all(),
		}
		for i in range(len(self.render_dict['topMenu_list'])):
			if self.render_dict['topMenu_list'][i].url=='catalog':
				self.render_dict['topMenu_list'][i].active=True
	def set_params_catalogCategory(self,filter):
		self.html='catalog.html'
		self.render_dict={
			'topMenu_list':TopMenu.objects.all(),
			'category_list':Category.objects.all(),
		}
		try:
			category=Category.objects.get(url=filter)
			subcategory_list=SubCategory.objects.filter(category=category)
			self.render_dict['product_list']=Product.objects.filter(subcategory__in=subcategory_list)
			for i in range(len(self.render_dict['category_list'])):
				if self.render_dict['category_list'][i].url==filter:
					self.render_dict['category_list'][i].active=True
		except:
			print 'filter = %s, cannot field'%filter
		for i in range(len(self.render_dict['topMenu_list'])):
			if self.render_dict['topMenu_list'][i].url=='catalog':
				self.render_dict['topMenu_list'][i].active=True
	def get_topMenu(self,param=None):
		topMenu=TopMenu.objects.all()
		print 123444444444444444444444444444444
		if param:
			for i in range(len(topMenu)):
				if topMenu[i].url==param:
					topMenu[i].active=True
		return topMenu
	def set_params_cart(self,request):
		self.html='cart.html'

		cart=Cart(request)
		cart_list=[]
		for item in Item.objects.filter(cart=cart.cart):
			product=item.product
			quantity=item.quantity
			item_price=item.item_price
			total_price=item.total_price
			cart_list.append({
				"product":product,
				"quantity":quantity,
				"item_price":int(item_price),
				"total_price":total_price,
				})
		self.render_dict={
			'topMenu_list':self.get_topMenu(),
			'category_list':Category.objects.all(),
			'cart_list':cart_list,
			'cart_active':True,
		}

class HomeView(MainView):
	def get(self,request):
		self.set_params_home()
		return render_to_response(self.html,self.render_dict)
class ProductDetailView(MainView):
	def get(self,request,id):
		self.set_params_productDetail(id)
		return render_to_response(self.html,self.render_dict)
class CatalogView(MainView):
	def get(self,request):
		self.set_params_catalog()
		return render_to_response(self.html,self.render_dict)
class CatalogCategoryView(MainView):
	def get(self,request,filter):
		self.set_params_catalogCategory(filter)
		return render_to_response(self.html,self.render_dict)
class CartView(MainView):
	def get(self,request):
		self.set_params_cart(request)
		return render_to_response(self.html,self.render_dict)

def add_to_cart(request):
	id=request.POST['id']
	product=Product.objects.get(id=id)
	cart=Cart(request)
	cart.add(product,product.price)
	return HttpResponse()
def remove_from_cart(request):
	product=Product.objects.get(id=request.POST['id'])
	cart=Cart(request)
	cart.remove(product)
	return HttpResponse()

