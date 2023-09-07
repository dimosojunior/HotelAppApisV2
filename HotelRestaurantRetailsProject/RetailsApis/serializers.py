from rest_framework.validators import UniqueValidator
#from rest_framework_jwt.settings import api_settings
from rest_framework import serializers
#from django.contrib.auth.models import User
from HotelApis.models import *




#--------------------------------------------------------------

from rest_framework import serializers
#from django.contrib.auth.models import User

class RetailsInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RetailsInventory
        fields = '__all__'


class RetailsFoodCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RetailsFoodCategories
        fields = '__all__'

class RetailsDrinksCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RetailsDrinksCategories
        fields = '__all__'