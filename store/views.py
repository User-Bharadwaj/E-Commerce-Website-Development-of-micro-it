from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, CartItem

def home(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'store/product_detail.html', {'product': product})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    session_id = request.session.session_key or request.session.create()
    
    cart_item, created = CartItem.objects.get_or_create(
        product=product,
        session_id=session_id
    )
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    return redirect('view_cart')

def view_cart(request):
    session_id = request.session.session_key or request.session.create()
    cart_items = CartItem.objects.filter(session_id=session_id)
    return render(request, 'store/cart.html', {'cart_items': cart_items})
