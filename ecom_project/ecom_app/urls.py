from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('categories/<slug:c_slug>/', views.catergories, name='categories'),
    path('product_detail/<slug:c_slug>/<slug:p_slug>', views.product_detail, name='product_detail'),
    path('search', views.search, name='search'),
]
