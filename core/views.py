from django.shortcuts import render, redirect, HttpResponse
from .models import Products
from django.db.models import Q
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User


# Create your views here.

def index(request):
    return render(request, "index.html")


def products(request):
    all_products = Products.objects.all()
    context = {
        "products": all_products
    }
    return render(request, "products.html", context)



def product_page(request, pk):
    product_page = Products.objects.get(pk=pk)
    context = {
        "product": product_page
    }
    return render(request, "product_page.html", context)


def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)  
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('products')
    return render(request, "sign-in.html")



def sign_out(request):
    logout(request)
    return redirect('products')



def reg(request):
    if request.method == 'GET':
        return render(request, "register.html")
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create_user(
            username=username,
            password=password
        )
        user.save()
        return redirect('products')
