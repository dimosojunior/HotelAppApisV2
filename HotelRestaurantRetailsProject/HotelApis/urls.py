
from django.urls import path
from . import views

# MWANZO IN ORDER TO USE MODEL VIEW SET
from rest_framework.routers import DefaultRouter

router = DefaultRouter()


router.register('HotelFoodProducts', views.HotelFoodProductsViewSet)

router.register('HotelInventory', views.HotelInventoryViewSet)
router.register('HotelFoodCategories', views.HotelFoodCategoriesViewSet)
router.register('HotelDrinksCategories', views.HotelDrinksCategoriesViewSet)
router.register('RoomsClasses', views.RoomsClassesViewSet)






urlpatterns = router.urls