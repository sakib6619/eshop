from django.shortcuts import render,redirect
from .models import *
from django.db.models import Max, Min
# Create your views here.
def all_product(request):
    category = Category.objects.all()
    all_product = Products.objects.all()
    min_price = Products.objects.all().aggregate(Min('price'))
    max_price = Products.objects.all().aggregate(Max('price'))
    color = Color.objects.all()
    brand = Brand.objects.all()
    colorID = request.GET.get('colorID')    
    FilterPrice = request.GET.get('FilterPrice')
    if FilterPrice:
        Int_FilterPrice = int(FilterPrice)
        product = Products.objects.filter(price__lte = Int_FilterPrice)
    elif colorID:
        product = Products.objects.filter(color = colorID)
    else:
        product = Products.objects.all()
        
    return render(request, 'Products/all_products.html', locals())

def product_details(request,slug):
    single_product = Products.objects.filter(slug=slug)
    if single_product.exists():
        single_product = Products.objects.get(slug=slug)
    else:
        return redirect('error404')
    return render(request, 'Products/product_details.html', locals())
