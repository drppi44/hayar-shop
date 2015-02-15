# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from models import *


def home(request):
	category_list=Category.objects.all()
	product_list=Product.objects.all()
	return render_to_response('index.html',{
		'category_list':category_list,
		'product_list':product_list,
		})

def full_info(request,id):
	category_list=Category.objects.all()
	product=Product.objects.get(id=id)
	product_list=Product.objects.all()
	return render_to_response('item.html',{
		'category_list':category_list,
		'product':product,
		'product_list':product_list,
		})