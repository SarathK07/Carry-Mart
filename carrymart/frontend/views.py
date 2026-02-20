from django.shortcuts import render

def login_page(request):
    return render(request, "login.html")

def products_page(request):
    return render(request, "products.html")

def cart_page(request):
    return render(request, "cart.html")

def orders_page(request):
    return render(request, "orders.html")

def payment_page(request, order_id):
    return render(request, "payment.html", {"order_id": order_id})

def payment_options_page(request):
    return render(request, "payment_options.html")