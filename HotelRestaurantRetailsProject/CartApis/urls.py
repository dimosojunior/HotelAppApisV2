from . import views
from django.urls import path,include

from rest_framework.routers import DefaultRouter






urlpatterns = [


    path('', views.HomeView, name='CartHome'),
    path('HotelFoodCart/', views.HotelFoodCartView.as_view(), name='HotelFoodCart'),
    path('HotelFoodOrder/', views.HotelFoodOrderView.as_view(), name='hotel-food-order-list'),
    path('HotelFoodOrdernNoDelete/', views.HotelFoodOrdernNoDeleteView.as_view(), name='hotel-food-order-list-no-delete'),

    path('DeleteCartItem/', views.DeleteCartItemView.as_view(), name='DeleteCart'),

    
    
]

