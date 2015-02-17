from django.contrib import admin
from models import *




@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display=['name','description','get_category','subcategory','price','date']
	def get_category(self,obj):
		return obj.subcategory.category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	pass

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
	pass

@admin.register(Param)
class ParamAdmin(admin.ModelAdmin):
	list_display=['name','value','product']

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
	list_display=['first_name','second_name']
@admin.register(TopMenu)
class TopMenuAdmin(admin.ModelAdmin):
	list_display=['name','url']

