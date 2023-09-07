from rest_framework.validators import UniqueValidator
#from rest_framework_jwt.settings import api_settings
from rest_framework import serializers
#from django.contrib.auth.models import User
from .models import *




#--------------------------------------------------------------

from rest_framework import serializers
#from django.contrib.auth.models import User

class HotelFoodProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelFoodProducts
        fields = '__all__'

class HotelInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelInventory
        fields = '__all__'


class HotelFoodCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelFoodCategories
        fields = '__all__'


class HotelDrinksCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelDrinksCategories
        fields = '__all__'


class RoomsClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomsClasses
        fields = '__all__'









#---------------------FOOD CART SERIALIZER---------




class HotelFoodCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelFoodCart
        fields = '__all__'


class HotelFoodCartItemsSerializer(serializers.ModelSerializer):
    cart = HotelFoodCartSerializer()
    product = HotelFoodProductsSerializer()
    class Meta:
        model = HotelFoodCartItems
        fields = '__all__'



class HotelFoodOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelFoodOrder
        fields = '__all__'


class HotelFoodCartItemsSerializer(serializers.ModelSerializer):
    order = HotelFoodOrderSerializer()
    product = HotelFoodProductsSerializer()
    class Meta:
        model = HotelFoodOrderItems
        fields = '__all__'

