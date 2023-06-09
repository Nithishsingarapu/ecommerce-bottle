from django.shortcuts import render
from .models import category,Brand,Product,ProductAttribute
# Home page
def home(request):
    return render(request,'index.html')


#category
def category_list(request):
    data=category.objects.all().order_by('-id')
    return render(request,'category_list.html',{'data':data})   

#brand
def brand_list(request):
    data=Brand.objects.all().order_by('-id')
    return render(request,'brand_list.html',{'data':data})


#product List
def product_list(request):
    data=Product.objects.all().order_by('-id')
    cats=Product.objects.distinct().values('category__title','category__id')
    brands=Product.objects.distinct().values('brand__title','brand__id')
    colors=ProductAttribute.objects.distinct().values('color__title','color__id','color__color_code')
    sizes=ProductAttribute.objects.distinct().values('size__title','size__id')
    return render(request,'product_list.html',
        {
            'data':data,
            'cats':cats,
            'brands':brands,
            'colors':colors,
            'sizes':sizes,
        }
        )    