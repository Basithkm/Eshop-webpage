from django.shortcuts import render,redirect
from . models import CategoryModel,Product
import os

# Create your views here.

# showing products
def product(request):
    products=Product.objects.all()
    cate=CategoryModel.objects.all()
    return render(request,'index.html',{'products':products,'cate':cate})


# insert Category
def insert_category(request):
    if request.method=="POST":
        category_name=request.POST['category_name']
        data=CategoryModel(category_name=category_name)
        data.save()
        info=CategoryModel.objects.all()
        return render(request,'category.html',{'info':info})
    else:
        info=CategoryModel.objects.all()
        return render(request,'category.html',{'info':info})
    
# Update Category
def update_category(request,id):
    update= CategoryModel.objects.get(pk=id)
    if request.method=="POST":
        update.category_name=request.POST.get('category_name')
        update.save()
        info =CategoryModel.objects.all()
        return render(request,'category.html',{'info':info})
    context = {'update':update}
    return render(request,"edit_category.html",context)

# insert Product
def insert_product(request):
    if request.method=="POST":
        product_name= request.POST['product_name']
        product_category= request.POST['product_category']
        product_image=request.FILES['product_image']
        product_price=request.POST['product_price']
        prod=Product(product_name=product_name,product_image=product_image,product_price=product_price,product_category=product_category)
        prod.save()
        products=Product.objects.all()
        return render(request,'index.html',{'products':products})
    else:
        products=Product.objects.all()
        return render(request,'index.html',{'products':products})



# update product
def update_product(request,id):
    update = Product.objects.get(pk=id)
    cate=CategoryModel.objects.all()
    if request.method=="POST":
        if len(request.FILES)!=0:
            if len(update.product_image)>0:
                os.remove(update.product_image.path)
            update.product_image=request.FILES['product_image']  
        update.product_name=request.POST.get('product_name')
        update.product_price=request.POST.get('product_price')
        update.save()
        products=Product.objects.all()
        return render(request,'index.html',{'products':products})
    context = {'update':update,'cate':cate}
    return render(request,"edit_product.html",context)


# delete products
def delete_product(request,id):
    datas =Product.objects.get(pk=id)
    datas.delete()
    products = Product.objects.all()
    return render(request,'index.html',{'products':products})
