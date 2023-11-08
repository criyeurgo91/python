from django.urls import path
from .views import *


urlpatterns=[
    path('about/',about_view),
    path('team/',team_view),
    path('contact/',contact_view, name='contact_view'),
    path('product_list/',product_list_view,name='product_list_view'),
    path('add_product/',add_product_view,name='add_product_view'),
    path('see_product/<int:id_product>/', see_product_view,name='see_product_view'),
    path('edit_product/<int:id_product>/', edit_product_view,name='edit_product_view'),
    path('delete_product/<int:id_product>/', delete_product_view,name='delete_product_view'),
    
]