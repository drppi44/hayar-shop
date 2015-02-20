# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.views.generic import View
from models import *

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
	def set_params_cart(self,request):
		self.html='cart.html'
		"""
		id_count_list=[[item[0],item[2]] for item in request.session['cart']]
		id_list=[item[0] for item in id_count_list]
		product_list=Product.objects.filter(id__in=id_list)
		for id,count in id_count_list:
			for i in range(len(product_list)):
				if product_list[i].id==id:
					product_list[i].count=count
		"""
		cart_dict=request.session['cart']
		self.render_dict={
			'topMenu_list':TopMenu.objects.all(),
			'category_list':Category.objects.all(),
			'cart_dict':cart_dict,
		}
		for i in range(len(self.render_dict['topMenu_list'])):
			if self.render_dict['topMenu_list'][i].url=='catalog':
				self.render_dict['topMenu_list'][i].active=True

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
	print id
	#if not request.session.__contains__('cart'):
	#	request.session.__setitem__('cart',{})
	if not request.session['cart'].__contains__(id):
		product=Product.objects.get(id=id)
		request.session['cart'].__setitem__(id,{'price':product.price,'count':1})
	else:
		request.session['cart'][id]['count']+=1
	request.session.modified = True
	print request.session['cart']
	product=Product.objects.get(id=id)

	request.session[id]=A(1,product.price)
	print request.session
	print request.META['HTTP_REFERER']
	
	return HttpResponse()

class A:
	def __init__(self,count,price):
		self.count=count
		self.price=price
