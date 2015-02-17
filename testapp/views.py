# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.views.generic import View
from models import *

class HomeView(View):
	def get(self,request):
			category_list=Category.objects.all()
			topMenu=TopMenu.objects.all()
			for i in range(len(topMenu)):
				if topMenu[i].url=='/':
					topMenu[i].active=True
				else:
					topMenu[i].active=False
			return render_to_response('index.html',{
				'category_list':category_list,
				'topMenu_list':topMenu,
				})
class ProductDetailView(View):
	def get(self,request,id):
			product=Product.objects.get(id=id)
			category_list=Category.objects.all()
			topMenu=TopMenu.objects.all()
			for i in range(len(topMenu)):
				if topMenu[i].url=='/catalog':
					topMenu[i].active=True
				else:
					topMenu[i].active=False
			return render_to_response('item.html',{
				'category_list':category_list,
				'product':product,
				'topMenu_list':topMenu,
				})
class CatalogView(View):
	def get(self,request):
			category_list=Category.objects.all()
			product_list=Product.objects.all()
			topMenu=TopMenu.objects.all()
			for i in range(len(topMenu)):
				if topMenu[i].url=='/catalog':
					topMenu[i].active=True
				else:
					topMenu[i].active=False
			return render_to_response('catalog.html',{
				'category_list':category_list,
				'product_list':product_list,
				'topMenu_list':topMenu,
				})
