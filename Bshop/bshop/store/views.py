from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Category

# Create your views here.
def index(request):
    products=Product.get_all_products()
    category=Category.get_all_category()
    data={}
    data['products'] = products
    data['category'] = category

    # print(products_list)
    return render(request,'index.html',data)
