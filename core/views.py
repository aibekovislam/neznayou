from django.shortcuts import render, redirect, HttpResponse
from .models import Products
from django.db.models import Q

# Create your views here.

def index(request):
    return render(request, "index.html")


def products(request):
    all_products = Products.objects.all()
    context = {
        "products": all_products
    }
    return render(request, "products.html", context)