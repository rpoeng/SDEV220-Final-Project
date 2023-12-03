from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# /products --> index
#Uniform Resource Locater
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html',
                  {'products':products}) #context provides date to use in template


def new(request):
    return HttpResponse('New Products')


