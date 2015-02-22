# -*- coding: utf-8 -*-
import models

class Cart(object):
	def __init__(self,request):
		cart_id=request.session.get('cart_id')
		if cart_id:
			try:
				cart=models.Cart.objects.get(id=cart_id)
			except:
				cart=self.new(request)
		else:
			cart=self.new(request)
		self.cart=cart
	def new(self,request):
		cart=models.Cart()
		cart.save()
		request.session['cart_id']=cart.id
		return cart
	def add(self,product,item_price,quantity=1):
		Item=models.Item(cart=self.cart,)
		try:
			item=models.Item.objects.get(cart=self.cart,product_id=product.id)
			item.quantity+=quantity
			item.save()
			print item,item.quantity
		except:
			item=models.Item(
				cart=self.cart,
				quantity=quantity,
				item_price=item_price,
				product_id=product.id,
				)
			item.save()
	def remove(self,product):
		try:
			item=models.Item.objects.get(cart=self.cart,product_id=product.id)
			item.delete()
		except:
			pass