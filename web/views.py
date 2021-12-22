from django.shortcuts import render
from django.http.response import HttpResponse
from products.models import Product

# Create your views here.
def index(request):
    products = Product.objects.all()

    context = {
        "products" : products,
    }
    return render(request,"index.html",context=context)