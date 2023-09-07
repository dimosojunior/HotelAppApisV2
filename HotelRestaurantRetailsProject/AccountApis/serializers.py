from rest_framework.validators import UniqueValidator
#from rest_framework_jwt.settings import api_settings
from rest_framework import serializers
#from django.contrib.auth.models import User
from HotelApis.models import *




#--------------------------------------------------------------

from rest_framework import serializers
#from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('username', 'email', 'password')



class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = '__all__'
        # fields = ['id', 'username', 'email','phone','first_name','profile_image']





