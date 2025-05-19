from django.shortcuts import render, redirect
from .models import Product
from django.core.paginator import Paginator

def product_list(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()

    paginator = Paginator(products, 5)  # 5 products per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'store/product_list.html', {'page_obj': page_obj, 'query': query})

def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    product_id_str = str(product_id)
    cart[product_id_str] = cart.get(product_id_str, 0) + 1  # increment quantity
    request.session['cart'] = cart
    return redirect('product_list')

def cart_summary(request):
    cart = request.session.get('cart', {})
    product_ids = cart.keys()
    products = Product.objects.filter(id__in=product_ids)
    cart_items = []
    total = 0
    for product in products:
        quantity = cart[str(product.id)]
        subtotal = product.price * quantity
        total += subtotal
        cart_items.append({'product': product, 'quantity': quantity, 'subtotal': subtotal})
    return render(request, 'store/cart_summary.html', {'cart_items': cart_items, 'total': total})
