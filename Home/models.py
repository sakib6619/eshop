from django.db import models

# Create your models here.
class Slider(models.Model):
    DEALS =(
    ('HOT DEALS','HOT DEALS'),
    ('New Arraivels','New Arraivels'),
    ('New DEALS','New DEALS'),
    )
    Image = models.ImageField(upload_to='media/slider_image/')
    Deals = models.CharField(choices=DEALS ,max_length=100)
    Sale = models.IntegerField()
    Brand_name = models.CharField(max_length=200)
    Discounts = models.IntegerField()
    link = models.CharField(max_length=200)
    
    def __str__(self):
        return self.Brand_name
    
class BannerArea(models.Model):
    BannerImage = models.ImageField(upload_to='media/banner_image/')
    BannerDeals = models.CharField(max_length=100)
    Quote = models.CharField(max_length=100)
    Discounts = models.IntegerField()
    
    def __str__(self):
        return self.Quote