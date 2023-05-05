from django.shortcuts import render,redirect
# from . models import CategoryModel,Product,District

# import os

# # Create your views here.

# # showing products
# def product(request):
#     products=Product.objects.all()
#     cate=CategoryModel.objects.all()
#     return render(request,'index.html',{'products':products,'cate':cate})


# # insert Category
# def insert_category(request):
#     if request.method=="POST":
#         category_name=request.POST['category_name']
#         data=CategoryModel(category_name=category_name)
#         data.save()
#         info=CategoryModel.objects.all()
#         return render(request,'category.html',{'info':info})
#     else:
#         info=CategoryModel.objects.all()
#         return render(request,'category.html',{'info':info})
    
# # Update Category
# def update_category(request,id):
#     update= CategoryModel.objects.get(pk=id)
#     if request.method=="POST":
#         update.category_name=request.POST.get('category_name')
#         update.save()
#         info =CategoryModel.objects.all()
#         return render(request,'category.html',{'info':info})
#     context = {'update':update}
#     return render(request,"edit_category.html",context)

# # insert Product
# def insert_product(request):
#     if request.method=="POST":
#         product_name= request.POST['product_name']
#         product_category= request.POST['product_category']
#         product_image=request.FILES['product_image']
#         product_price=request.POST['product_price']
#         prod=Product(product_name=product_name,product_image=product_image,product_price=product_price,product_category=product_category)
#         prod.save()
#         products=Product.objects.all()
#         return render(request,'index.html',{'products':products})
#     else:
#         products=Product.objects.all()
#         return render(request,'index.html',{'products':products})



# # update product


# def update_product(request,id):
#     update = Product.objects.get(pk=id)
#     cate=CategoryModel.objects.all()
#     if request.method=="POST":
#         if len(request.FILES)!=0:
#             if len(update.product_image)>0:
#                 os.remove(update.product_image.path)
#             update.product_image=request.FILES['product_image']  
#         update.product_name=request.POST.get('product_name')
#         update.product_price=request.POST.get('product_price')
#         update.save()
#         products=Product.objects.all()
#         return render(request,'index.html',{'products':products})
#     context = {'update':update,'cate':cate}
#     return render(request,"edit_product.html",context)





# # delete products
# def delete_product(request,id):
#     datas =Product.objects.get(pk=id)
#     datas.delete()
#     products = Product.objects.all()
#     return render(request,'index.html',{'products':products})
# from django.shortcuts import render, redirect
# from .models import Product, Category, City, District
# from django.template.loader import render_to_string
# from django.shortcuts import render
# from django.http import JsonResponse
# from .models import Product


# # views.py

# from django.shortcuts import render, redirect
# from .models import Product, Category, City, District

# def add_product(request):
#     categories = Category.objects.all()
#     cities = City.objects.all()
#     districts = District.objects.all()

#     if request.method == 'POST':
#         name = request.POST['name']
#         category_id = request.POST['category']
#         price = request.POST['price']
#         city_id = request.POST['city']
#         district_id = request.POST['district']

#         product = Product(name=name, category_id=category_id, price=price, city_id=city_id, district_id=district_id)
#         product.save()

#         return redirect('add_product')

#     else:
#         return render(request, 'product_form.html', {'categories': categories, 'cities': cities, 'districts': districts})


# def product_list(request):
#     products = Product.objects.all()
#     return render(request, 'product_list.html', {'products': products})


# def product_filter(request):
#     categories = Category.objects.all()
#     cities = City.objects.all()
#     districts = District.objects.all()

#     products = Product.objects.all()

#     # Filter by price
#     price = request.GET.get('price')
#     if price:
#         if price == '0-50':
#             products = products.filter(price__lte=50)
#         elif price == '50-100':
#             products = products.filter(price__range=(50, 100))
#         elif price == '100-200':
#             products = products.filter(price__range=(100, 200))
#         elif price == '200+':
#             products = products.filter(price__gte=200)
        
#         # Filter by category
#     category = request.GET.get('category')
#     if category:
#             products = products.filter(category_id=category)
            
#         # Filter by city
#     city = request.GET.get('city')
#     if city:
#         products = products.filter(city_id=city)
            
#     # Filter by district
#     district = request.GET.get('district')
#     if district:
#         products = products.filter(district_id=district)

#     context = {'products': products,
#                'categories':categories,
#                'cities':cities,
#                'districts':districts

#                }
#     return render(request, 'product_filter.html', context)
        
# from django.shortcuts import render, redirect, get_object_or_404
# from .models import Property, PropertyDetails, RentalDetails, SaleDetails, Image


# def add_property(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         category = request.POST['category']
#         property = Property.objects.create(name=name, category=category)
#         return redirect('add_property_details', property_id=property.id)
#     return render(request, 'add_property.html')


# def add_property_details(request, property_id):
#     property = Property.objects.get(id=property_id)
#     if request.method == 'POST':
#         location = request.POST['location']
#         images = request.FILES.getlist('images')
#         property_details = PropertyDetails.objects.create(property=property, location=location)
#         for image in images:
#             Image.objects.create(image=image, propertydetails=property_details)
#         if property.category == 'rent':
#             return redirect('add_rental_details', property_details_id=property_details.id)
#         else:
#             return redirect('add_sale_details', property_details_id=property_details.id)
#     return render(request, 'add_property_details.html', {'property': property})


# def add_rental_details(request, property_details_id):
#     property_details = PropertyDetails.objects.get(id=property_details_id)
#     if request.method == 'POST':
#         rent_price = request.POST['rent_price']
#         RentalDetails.objects.create(property_details=property_details, rent_price=rent_price)
#         return redirect('property_list')
#     return render(request, 'add_rental_details.html', {'property_details': property_details})


# def add_sale_details(request, property_details_id):
#     property_details = PropertyDetails.objects.get(id=property_details_id)
#     if request.method == 'POST':
#         price = request.POST['price']
#         SaleDetails.objects.create(property_details=property_details, price=price)
#         return redirect('property_list')
#     return render(request, 'add_sale_details.html', {'property_details': property_details})


# def edit_property(request, property_id):
#     property = get_object_or_404(Property, id=property_id)
#     if request.method == 'POST':
#         property.name = request.POST['name']
#         property.category = request.POST['category']
#         property.save()
#         return redirect('edit_property_details', property_id=property.id)
#     return render(request, 'edit_property.html', {'property': property})


# def edit_property_details(request, property_id):
#     property = Property.objects.get(id=property_id)
#     property_details = property.details
#     if request.method == 'POST':
#         location = request.POST['location']
#         images = request.FILES.getlist('images')
#         property_details.location = location
#         property_details.images.clear()
#         for image in images:
#             Image.objects.create(image=image, propertydetails=property_details)
#         property_details.save()
#         if property.category == 'rent':
#             return redirect('edit_rental_details', property_details_id=property_details.id)
#         else:
#             return redirect('edit_sale_details', property_details_id=property_details.id)
#     return render(request, 'edit_property_details.html', {'property': property, 'property_details': property_details})


# def edit_rental_details(request, property_details_id):
#     property_details = PropertyDetails.objects.get(id=property_details_id)
#     rental_details = property_details.rental_details
#     if request.method == 'POST':
#         rent_price = request.POST['rent_price']
#         rental_details.rent_price = rent_price
#         rental_details.save()
#         return redirect('property_list')
#     return render(request, 'edit_rental_details.html', {'property': property_details, 'property_details': property_details})


# def property_list(request):
#     properties = Property.objects.all
#     return render(request, 'property_list.html', {'properties': properties})




from django.shortcuts import render, redirect
from django.conf import settings
import os

from .models import MyModel, Image

def add_data(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        images = request.FILES.getlist('images')
        
        # Save each file to a media folder with a unique file name
        # image_names = [save_uploaded_file(image) for image in images]
        
        # Create a new instance of the model with the name and associated image data and save it to the database
        my_model = MyModel(name=name)
        my_model.save()
        for image_name in images:
            image = Image(file=image_name)
            image.save()
            my_model.images.add(image)
        return redirect('success')
    return render(request,'add_data.html')

# def save_uploaded_file(file):
#     file_name = os.path.join(settings.MEDIA_ROOT, file.name)
#     with open(file_name, 'wb+') as destination:
#         for chunk in file.chunks():
#             destination.write(chunk)
#     return os.path.basename(file_name)


from django.http import HttpResponse
def success(request):
    return HttpResponse("success")


def show_data(request):
    my_models = MyModel.objects.all()
    return render(request, 'show_data.html', {'my_models': my_models})