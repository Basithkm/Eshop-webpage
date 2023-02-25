from django.urls import path
from . import views


urlpatterns = [
    path('',views.product,name='product'),
    path('insert_category',views.insert_category,name='insert_category'),
    path('insert_product',views.insert_product,name='insert_product'),
    path('delete_product/<int:id>',views.delete_product,name='delete_product'),
    path('update_product/<int:id>',views.update_product,name='update_product'),
    path('update_category/<int:id>',views.update_category,name='update_category'),
]
