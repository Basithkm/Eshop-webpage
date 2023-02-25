from django.db import models

# Create your models here.

# category model
class CategoryModel(models.Model):
    category_name=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.category_name
    

# product model
class Product(models.Model):
    product_name=models.CharField(max_length=100)
    product_category=models.CharField(max_length=100)
    product_image=models.ImageField(upload_to="product_images")
    product_price =models.IntegerField()

    def __str__(self) -> str:
        return self.product_name






