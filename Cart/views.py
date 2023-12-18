from django.shortcuts import render, redirect
from Products.models import *
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from django.db.models import Min,Max,Sum

@login_required(login_url="Accounts/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Products.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="Accounts/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Products.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="Accounts/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Products.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="Accounts/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Products.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="Accounts/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/Accounts/login")
def cart_detail(request):
    cart = request.session.get('cart')
    packing_cost = sum(i['packing_cost'] for i in cart.values() if i)
    tax = sum(i['tax'] for i in cart.values() if i)

    coupon = None
    valid_coupon = None
    invalid_coupon = None
    if request.method == "GET":
        coupon_code = request.GET.get('coupon_code')
        if coupon_code:
            try:
                coupon = Coupon_code.objects.get(code = coupon_code)
                valid_coupon = "Coupon apply success "
            except:
                invalid_coupon = "Sorry Invalid coupon"
    
    return render(request, 'Cart/cart_detail.html', locals())

@login_required(login_url="/Accounts/login")
def checkout(request):
    checkout = request.session.get('cart')
    print(checkout)
    return render(request, 'Cart/checkout.html', locals())