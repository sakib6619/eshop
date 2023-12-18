from django.shortcuts import render
from .models import *
from Products.models import *
# Create your views here.
def home(request):
    sliders = Slider.objects.all()
    banners = BannerArea.objects.all()
    allCategory = MainCategory.objects.all()
    top_deals_product = Products.objects.filter(sections__name = "Top Deals Of The Day")
    Top_Selling_Products = Products.objects.filter(sections__name = "Top Selling Products")
    
    CatID = request.GET.get('Categories')
    if CatID:
        allCategory = MainCategory.objects.filter(Category_name=CatID)
    else:
        allCategory = MainCategory.objects.all()
    return render(request,'Home/home.html', locals())
def about(request):
    return render(request, 'Home/about.html')
def contact(request):
    return render(request, 'Home/contact.html')
def faq(request):
    return render(request, 'Home/faq.html')
def blog(request):
    return render(request, 'Home/blog.html')
def blog_details(request):
    return render(request, 'Home/blog_details.html')

def error4040(request):
    return render(request, 'Errors/404.html')