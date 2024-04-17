from django.shortcuts import render
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def product(request, pk):
    product=Product.objects.get(id=pk)
    return render(request, 'product.html', {'product': product})

