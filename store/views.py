from django.shortcuts import render
from django.http import HttpResponse
from.models import Category,Product
from django.shortcuts import get_object_or_404
#
# def home(request):
#     return render(request,'home.html')


def product_all(request):
    products = Product.objects.all()
    # products = Product.products.all()
    return render(request, 'store/home.html',{'products': products})


def category_list(request, category_slug):
     category =  get_object_or_404(Category, slug=category_slug)
     #we need all the producs in that respective category
     products = Product.objects.filter(category=category)
     return render(request, 'store/products/category.html', {'category': category, 'products': products})


def product_detail(request, pro_slug):#slug here is the reference from the url
    # we have pro_slug that should match with this slug of te url
    product = get_object_or_404(Product, slug=pro_slug, in_stock=True)
    return render(request, 'store/products/single.html', {'product':product})