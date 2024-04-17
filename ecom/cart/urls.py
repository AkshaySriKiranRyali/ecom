from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('shipping_page/',views.shipping_page,name="shipping_page"),
   path('',views.cart_summary,name="cart_summary"),
   path('add/',views.cart_add,name="cart_add"),
   path('delete/',views.cart_delete,name="cart_delete"),
   path('update/',views.cart_update,name="cart_update"),
   path('clear_cart/',views.clear_cart,name="clear_cart"),
   
] 
