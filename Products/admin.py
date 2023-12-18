from django.contrib import admin
from .models import *
# Register your models here.
class Product_img(admin.TabularInline):
    model = ProductImage
    
class AdditionalInformation(admin.TabularInline):
    model = Additional_information
    
class Product_Admin(admin.ModelAdmin):
    inlines = (Product_img, AdditionalInformation)
    list_display = ('product_name','categories','color','sections')
    list_editable = ('categories','sections','color',)
    
    
admin.site.register(Section)
admin.site.register(Products, Product_Admin)
admin.site.register(ProductImage)
admin.site.register(Additional_information)
admin.site.register(Color)
admin.site.register(Brand)


admin.site.register(MainCategory)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Coupon_code)
