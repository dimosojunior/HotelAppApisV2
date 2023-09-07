from rest_framework.validators import UniqueValidator
#from rest_framework_jwt.settings import api_settings
from rest_framework import serializers
#from django.contrib.auth.models import User
from HotelApis.models import *




#--------------------------------------------------------------

from rest_framework import serializers
#from django.contrib.auth.models import User

class RestaurantInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantInventory
        fields = '__all__'

class RestaurantFoodCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantFoodCategories
        fields = '__all__'

class RestaurantDrinksCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantDrinksCategories
        fields = '__all__'