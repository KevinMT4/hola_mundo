from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .models import Product, Order

def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    order, created = Order.objects.get_or_create(user=request.user, is_completed=False)
    order.products.add(product)
    order.total_price += product.price
    order.save()
    return redirect('product_list')

def view_cart(request):
    if request.user.is_authenticated:
        try:
            order = Order.objects.get(user=request.user, is_completed=False)
        except Order.DoesNotExist:
            order = None
    else:
        # Carrito de ejemplo para usuarios no autenticados
        example_products = Product.objects.all()[:3]  # Obtén los primeros 3 productos como ejemplo
        order = {
            'products': example_products,
            'total_price': sum([product.price for product in example_products]),
            'is_completed': False
        }

    return render(request, 'store/view_cart.html', {'order': order})
