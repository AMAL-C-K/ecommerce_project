from django.urls import path
from . import views

urlpatterns = [
    path('add_to_cart/<int:product_id>', views.add_to_cart, name='add_to_cart'),
    path('view_cart', views.view_cart, name='view_cart'),
    # path('dec_quantity/<int:product_id>', views.dec_quantity, name='dec_quantity'),
    path('dec_quantity/<int:cart_id>', views.dec_quantity, name='dec_quantity'),
    # path('remove/<int:product_id>', views.remove, name='remove'),
    path('delete/<int:cart_id>', views.delete, name='delete'),
    path('checkout/<int:cart_id>', views.checkout, name='checkout'),
    path('success', views.success, name='success'),
    path('orders', views.orders, name='orders'),
    path('add_quantity/<int:cart_id>', views.add_quantity, name='add_quantity'),
    
]
