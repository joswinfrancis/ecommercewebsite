from django.shortcuts import render,redirect,get_object_or_404
from products.models import Product
from .models import Cart,CartItem
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart
@login_required(login_url='login')
def add_cart(request,product_id):
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )
    cart.save()

    try:
        cart_item = CartItem.objects.get(product=product,cart=cart)
        cart_item.quantity+=1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product=product,
            quantity=1,
            cart=cart,
        )
        cart_item.save()
    return redirect('cart')
@login_required(login_url='login')
def remove_cart_item(request,product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product,id=product_id)
    cart_item = CartItem.objects.get(product=product,cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity-=1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')
@login_required(login_url='login')
def delete_cart_item(request,product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product,id=product_id)
    cart_item = CartItem.objects.get(product=product,cart=cart)
    
    cart_item.delete()
    return redirect('cart')
        
@login_required(login_url='login')
def cart(request,total=0,quantity=0,cart_items=None):
    error_message=None
    tax = 0
    grand_total = 0
    try:
        cart=Cart.objects.get(cart_id=_cart_id(request))
        cart_items=CartItem.objects.filter(cart=cart,is_active=True)
        for cart_item in cart_items:
            total+=(cart_item.product.price*cart_item.quantity)
            quantity+=cart_item.quantity
        tax = (total*2)/100
        grand_total = total+tax
        if grand_total == 0:
            error_message = 'YOUR CART IS EMPTY'
        else:
            grand_total = total+tax
    except Cart.DoesNotExist:
        pass

    context = {
            'total':total,
            'quantity':quantity,
            'cart_items':cart_items,
            'tax':tax,
            'grand_total':grand_total,
            'error_message': error_message
        }
    return render(request,'cart.html',context)