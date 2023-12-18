from django.db import models
# ckeditor 
from ckeditor.fields import RichTextField
# slug title dynamic
from autoslug import AutoSlugField
# Create your models here.
class MainCategory(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Category(models.Model):
    main_category = models.ForeignKey(MainCategory,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name + '--' +self.main_category.name
    
class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name +  '--' + self.category.name
    
class Section(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
class Color(models.Model):
    code = models.CharField(max_length=100)
    def __str__(self):
        return self.code
class Brand (models.Model):
    name = models.CharField(max_length=256)
    
    def __str__(self):
        return self.name
        
class Coupon_code(models.Model):
    code = models.CharField(max_length=150)
    discount = models.IntegerField()
    def __str__(self):
        return self.code
    
class Products(models.Model):
    total_quantity = models.IntegerField()
    availability = models.IntegerField()
    feature_image = models.CharField(max_length=200)
    product_name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,null=True)
    price = models.IntegerField()
    discount = models.IntegerField()
    tax = models.IntegerField(null=True)
    packing_cost = models.IntegerField(null=True)
    product_information = RichTextField()
    model_name = models.CharField(max_length=100)
    categories = models.ForeignKey(Category,on_delete=models.CASCADE)
    tag = models.CharField(max_length=100)
    description = RichTextField()
    sections = models.ForeignKey(Section,on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from='product_name',unique=True,null=True,default=None)
    color = models.ForeignKey(Color,on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return self.product_name

    
class ProductImage(models.Model):
    products = models.ForeignKey('Products',on_delete=models.CASCADE)
    image_url = models.CharField(max_length=200)
    
class Additional_information(models.Model):
    products = models.ForeignKey('Products',on_delete=models.CASCADE)
    specification = models.CharField(max_length=100)
    details = models.CharField(max_length=100)
    
    