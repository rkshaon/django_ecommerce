from django.shortcuts import render
from store.models import *

def store(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'store.html', context)

def cart(request):
    context = {}
    return render(request, 'cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'checkout.html', context)
