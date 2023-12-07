from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='store_home'),  # Asociar la vista product_list a la URL raíz
    path('product_list/', views.product_list, name='product_list'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('view_cart/', views.view_cart, name='view_cart'),
]
