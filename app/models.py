from django.db import models

# # Create your models here.

# # category model
# class CategoryModel(models.Model):
#     category_name=models.CharField(max_length=100)

#     def __str__(self) -> str:
#         return self.category_name
    

# # product model
# class Product(models.Model):
#     product_name=models.CharField(max_length=100)
#     product_category=models.CharField(max_length=100)
#     product_image=models.ImageField(upload_to="product_images")
#     product_price =models.IntegerField()

#     def __str__(self) -> str:
#         return self.product_name


# # class Country(models.Model):
# #     name = models.CharField(max_length=100)

# #     def __str__(self) -> str:
# #         return self.name

# class District(models.Model):
#     # country = models.ForeignKey(Country, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)

#     def __str__(self) -> str:
#         return self.name



# class City(models.Model):
#     district = models.ForeignKey(District,on_delete=models.CASCADE)
#     name =models.CharField(max_length=100)

#     def __str__(self) -> str:
#         return self.name
    

# # from geoposition.fields import GeopositionField

# # class Place(models.Model):
# #     name = models.CharField(max_length=100)
# #     location = GeopositionField()

# #     def __str__(self):
# #         return self.name





# class User(models.Model):
#     name = models.CharField(max_length=255)
#     age = models.IntegerField()
#     location = models.CharField(max_length=255)
#     latitude = models.DecimalField(max_digits=9, decimal_places=6)
#     longitude = models.DecimalField(max_digits=9, decimal_places=6)

#     def __str__(self):
#         return self.name


# from django.db import models

# class Category(models.Model):
#     name = models.CharField(max_length=50)

#     def __str__(self):
#         return self.name

# class City(models.Model):
#     name = models.CharField(max_length=50)

#     def __str__(self):
#         return self.name

# class District(models.Model):
#     name = models.CharField(max_length=50)
#     city = models.ForeignKey(City, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name

# class Product(models.Model):
#     name = models.CharField(max_length=50)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     city = models.ForeignKey(City, on_delete=models.CASCADE)
#     district = models.ForeignKey(District, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name




# class Property(models.Model):
#     CATEGORIES = (
#         ('rent', 'Rent'),
#         ('sale', 'Sale')
#     )

#     name = models.CharField(max_length=255)
#     category = models.CharField(choices=CATEGORIES, max_length=10)

#     def __str__(self):
#         return self.name


# class PropertyDetails(models.Model):
#     property = models.OneToOneField(Property, on_delete=models.CASCADE, related_name='details')
#     location = models.CharField(max_length=255)
#     images = models.ManyToManyField('Image')

#     def __str__(self):
#         return f"{self.property.name} Details"


# class RentalDetails(models.Model):
#     property_details = models.OneToOneField(PropertyDetails, on_delete=models.CASCADE, related_name='rental_details')
#     rent_price = models.DecimalField(decimal_places=2, max_digits=10)

#     def __str__(self):
#         return f"{self.property_details.property.name} Rental Details"


# class SaleDetails(models.Model):
#     property_details = models.OneToOneField(PropertyDetails, on_delete=models.CASCADE, related_name='sale_details')
#     price = models.DecimalField(decimal_places=2, max_digits=10)

#     def __str__(self):
#         return f"{self.property_details.property.name} Sale Details"


# class Image(models.Model):
#     image = models.ImageField(upload_to='property_images')

#     def __str__(self):
#         return self.image.url


# class Category(models.Model):
#     name = models.CharField(max_length=255)

#     def __str__(self):
#         return self.name


class MyModel(models.Model):
    name = models.CharField(max_length=50)
    images = models.ManyToManyField('Image')

    def __str__(self) -> str:
        return self.name
    
class Image(models.Model):
    file = models.ImageField(upload_to='images/')


  

