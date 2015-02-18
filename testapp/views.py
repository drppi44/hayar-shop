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

class HomeView(MainView):
	def get(self,request):
			self.set_params_home()
			return render_to_response(self.html,self.render_dict)

class ProductDetailView(MainView):
	def get(self,request,id):
			self.set_params_productDetail(id)
			return render_to_response(self.html,self.render_dict)
class CatalogView(View):
	def get(self,request):
			category_list=Category.objects.all()
			category_list[0].active=True
			product_list=Product.objects.all()
			topMenu=TopMenu.objects.all()
			for i in range(len(topMenu)):
				if topMenu[i].url=='catalog':
					topMenu[i].active=True
			return render_to_response('catalog.html',{
				'category_list':category_list,
				'product_list':product_list,
				'topMenu_list':topMenu,
				})
class CatalogCategoryView(View):
	def get(self,request,filter):
			category_list=Category.objects.all()
			try:
				category=Category.objects.get(url=filter)
				subcategory_list=SubCategory.objects.filter(category=category)
				product_list=Product.objects.filter(subcategory__in=subcategory_list)
				for i in range(len(category_list)):
					if category_list[i].url==filter:
						category_list[i].active=True
			except:
				print 'filter = %s, cannot fild'%filter
			topMenu=TopMenu.objects.all()
			for i in range(len(topMenu)):
				if topMenu[i].url=='catalog':
					topMenu[i].active=True
				else:
					topMenu[i].active=False
			return render_to_response('catalog.html',{
				'category_list':category_list,
				'product_list':product_list,
				'topMenu_list':topMenu,
				})
