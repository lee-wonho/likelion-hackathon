from django.shortcuts import render
from .models import Category,Good

# Create your views here.

def home(request):
    categories = Category.objects.all()
    context ={
        'categories':categories
    }
    return render(request, 'home.html',context)

def detail(request,category_pk):

    category_obj = Category.objects.get(pk=category_pk)
    goods_obj = Good.objects.filter(category=category_pk)

    context = {
        'category_pk': category_pk,
        'category_obj': category_obj,
        'goods_obj' : goods_obj,
    }

    return render(request,'detail.html',context)