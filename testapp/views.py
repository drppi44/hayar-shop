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
	#Ф-я для задания содержимого Верхнего меню
	def get_topMenu(self,param=None):
		topMenu=TopMenu.objects.all()
		if param!='cart':
			for i in range(len(topMenu)):
				if topMenu[i].url==param:
					topMenu[i].active=True
		return topMenu
	#------------------------------------
	#Ф-я для задания параметров Home страници
	def set_params_home(self):
		self.html='index.html'
		self.render_dict={
			'topMenu_list':self.get_topMenu(''),
		}
	#--------------------------------------------------
	#Ф-я для задания параметров для страницы подробного описания выбраного товара
	def set_params_productDetail(self,id):
		self.html='item.html'
		self.render_dict={
			'topMenu_list':self.get_topMenu('catalog'),
			'category_list':Category.objects.all(),
			'product':Product.objects.get(id=id),
		}
	#--------------------------------------------------
	#Ф-я для задания параметров для страницы каталога товаров
	def set_params_catalog(self):
		self.html='catalog.html'
		self.render_dict={
			'topMenu_list':self.get_topMenu('catalog'),
			'category_list':Category.objects.all(),
			'product_list':Product.objects.all(),
		}
	#---------------------------------------
	#Ф-я для задания параметров для страниц которые показывают категорию товара
	def set_params_catalogCategory(self,filter):
		self.html='catalog.html'
		self.render_dict={
			'topMenu_list':self.get_topMenu('catalog'),
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
	#---------------------------------------
	#Ф-я для задания параметров Cart корзины
	def set_params_cart(self,request):
		self.html='cart.html'
		cart=Cart(request)
		cart_list=[]
		for item in Item.objects.filter(cart=cart.cart):
			product=item.product
			quantity=item.quantity
			total_price=item.total_price
			cart_list.append({
				"product":product,
				"quantity":quantity,
				"total_price":int(total_price),
				})
		self.render_dict={
			'topMenu_list':self.get_topMenu('cart'),
			'cart_list':cart_list,
			'cart_active':True,
			'cart_summary':int(cart.summary),
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
	product_id=request.POST['id']
	product=Product.objects.get(id=product_id)
	cart=Cart(request)
	cart.add(product,product.price)
	return HttpResponse()
def remove_from_cart(request):
	product_id=request.POST['id']
	product=Product.objects.get(id=product_id)
	cart=Cart(request)
	cart.remove(product)
	return HttpResponse()
def update_cart_item(request):
	product_id=request.POST['id']
	quanity=request.POST['value']
	cart=Cart(request)
	cart.update(product_id,quanity)
	return HttpResponse()

