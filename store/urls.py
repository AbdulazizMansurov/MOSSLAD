from django.urls import path
from .views import *

urlpatterns = [
    path('', Products_list_4.as_view(), name='index'),
    path('products/', Products_list.as_view(), name='product_list'),
    path('product/<int:pk>', Product_detail.as_view(), name='detail_view'),
    path('category/<int:pk>', ProductsListByCategory.as_view(), name='products_by_cat'),

    path('profile/<int:user_id>/', profile, name='profile'),
    path('about/', about, name='about'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),
]
