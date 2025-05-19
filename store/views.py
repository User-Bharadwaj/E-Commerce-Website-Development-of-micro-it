from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Cart, CartItem

def home(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'store/product_detail.html', {'product': product})

def get_cart(request):
    cart_id = request.session.get('cart_id')
    if cart_id:
        cart = Cart.objects.filter(id=cart_id).first()
        if cart:
            return cart
    cart = Cart.objects.create()
    request.session['cart_id'] = cart.id
    return cart

def add_to_cart(request, product_id):
    cart = get_cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart_detail')

def cart_detail(request):
    cart = get_cart(request)
    items = cart.items.select_related('product').all()
    return render(request, 'store/cart_detail.html', {'cart_items': items})
