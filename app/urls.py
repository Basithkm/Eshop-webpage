from django.urls import path
from . import views


# urlpatterns = [
#     # path('',views.product,name='product'),
#     # path('insert_category',views.insert_category,name='insert_category'),
#     # path('insert_product',views.insert_product,name='insert_product'),
#     # path('delete_product/<int:id>',views.delete_product,name='delete_product'),
#     # path('update_product/<int:id>',views.update_product,name='update_product'),
#     # path('update_category/<int:id>',views.update_category,name='update_category'),
#     # # path('get_city/',views. get_city, name='get_city')

#     # # path('way',views.way,name='way'),
#     # # path('get_city/',views.get_city, name='get_city'),
    
#     # # path('abc',views.dependantfield,name='product'),
#     # path('district-city/',views. district_city, name='district_city'),
#     # path('get_cities/', views.get_cities, name='get_cities'),
#     # #  path('map/', views.place_map, name='place_map'), 
#     # path('reg/', views.register, name='register'),


    
# ]


urlpatterns = [
#     path('', views.property_list, name='property_list'),
#     path('add_property/', views.add_property, name='add_property'),
#     path('property_details/<int:property_id>/', views.property_detail, name='property_details'),
#     path('edit_property/<int:property_id>/', views.edit_property, name='edit_property'),
#     path('edit_property_details/<int:property_id>/', views.edit_property_details, name='edit_property_details'),
#     path('edit_rental_details/<int:property_details_id>/', views.edit_rental_details, name='edit_rental_details'),
#     path('edit_sale_details/<int:property_details_id>/', views.edit_sale_details, name='edit_sale_details'),
#     path('add_property_details/<int:property_id>/', views.add_property_details, name='add_property_details'),
#     path('add_rental_details/<int:property_details_id>/', views.add_rental_details, name='add_rental_details'),
#     path('add_sale_details/<int:property_details_id>/', views.add_sale_details, name='add_sale_details'),
     # path('dfdsfd',views.add_product, name='add_product'),
     # path('display/',views. product_list, name='product_list'),
     # # path('fi/', views.product_list, name='product_list'),
     # path('filter/', views.product_filter, name='product_filter'),
     path('', views.add_data, name='add_data'),
     path('success/', views.success, name='success'),
     path('show', views.show_data, name='my-view'),


]
