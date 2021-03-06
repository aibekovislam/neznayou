from django import contrib
from django.shortcuts import render, redirect, HttpResponse
import rest_framework
from .models import Products, Users, AboutUs, ContactUs
from django.db.models import Q
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .serializers import *



# Create your views here.

def index(request):
    return render(request, "main.html")


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
    return redirect(index)



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


def create_products(request):
    if request.method == 'POST':
        title = request.POST['title']
        text = request.POST['text']
        date = request.POST['date']
        picture = request.FILES.get('picture')
        product = Products(title=title, text=text, date=date, picture=picture)
        product.save()
        return redirect('products')
    return render(request, "create_products.html")


def delete_products(request, pk):
    product = Products.objects.get(pk=pk)
    product.delete()
    return redirect('products')


def edit_products(request, pk):
    product = Products.objects.get(pk=pk)
    if request.method == 'POST':
        product.title = request.POST.get('title')
        product.text = request.POST.get('text')
        product.date = request.POST.get('date')
        product.picture = request.POST.get('picture')
        product.save()
        return redirect('products')
    return render(request, "edit_product.html", {"product": product})


def about_us(request):
    about_us_all = AboutUs.objects.all()
    context = {
        "about_us": about_us_all
    }
    return render(request, "about_us.html", context)



def search(request):
    word = request.GET.get("word")
    products = Products.objects.filter(
        Q(title__icontains=word) | Q(text__icontains=word),
        is_active=True)
    return render(request, "products.html", {"products": products})





        

def create_contact(request):
    if request.method == 'POST':
        name = request.POST["name"]
        phone_number = request.POST["phone_number"]
        contact_us = ContactUs(name=name, phone_number=phone_number)
        contact_us.save() 
        return redirect('products')
    return render(request, "main.html",)