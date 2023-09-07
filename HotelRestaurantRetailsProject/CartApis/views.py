from django.shortcuts import render
from django.shortcuts import render,redirect

from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render,get_object_or_404
from HotelApis.serializers import *
from HotelApis.models import *
from HotelApis.serializers import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, auth
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib import messages


#REST FRAMEWORK
from rest_framework import status
from rest_framework.response import Response

#---------------------FUNCTION VIEW-------------------------
from rest_framework.decorators import api_view

#------------------------CLASS BASED VIEW-------------------
from rest_framework.views import APIView


#------------------------GENERIC VIEWs-------------------
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


#------------------------ VIEW SETS-------------------
from rest_framework.viewsets import ModelViewSet


#------FILTERS, SEARCH AND ORDERING
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.filters import SearchFilter,OrderingFilter

#------PAGINATION-------------
from rest_framework.pagination import PageNumberPagination




#----------------CREATING A CART------------------------
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from HotelApis.serializers import *
from RestaurantApis.serializers import *
from RetailsApis.serializers import *
from drf_yasg.utils import swagger_auto_schema

from rest_framework import generics,status
from rest_framework.decorators import api_view

# Create your views here.

# class UserView(APIView):

# 	def get(self,request, format=None):
# 		return Response("User Account View", status=200)

# 	def post(self,request, format=None):

# 		return Response("Creating User", status=200)



from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView



import jwt, datetime
from rest_framework.exceptions import AuthenticationFailed










#-----------------------------------------------


from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from HotelApis.models import MyUser  # Make sure to import your MyUser model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

def HomeView(request):

	return HttpResponse("CART APIS")




#---------------HOTEL CART FOOD APIS--------------------------




class HotelFoodCartView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    # kama unatumia JWT weka hiyo tu
    # permission_classes =[IsAuthenticated]

#RETRIEVE CART ITEMS FROM A CART
    def get(self, request):
        user = request.user
        cart = HotelFoodCart.objects.filter(user=user, ordered=False).first()
        queryset = HotelFoodCartItems.objects.filter(cart=cart)
        serializer = HotelFoodCartItemsSerializer(queryset, many=True)

        return Response(serializer.data)


    def post(self, request):
        data = request.data
        user = request.user
        cart, _ = HotelFoodCart.objects.get_or_create(user=user, ordered=False)
        product = HotelFoodProducts.objects.get(id=data.get('product'))
        price = product.price
        quantity = data.get('quantity')

        # Check if the requested quantity is available in stock
        if product.ProductQuantity < quantity:
            return Response({'error': 'Not enough quantity in stock'}, status=status.HTTP_400_BAD_REQUEST)

        cart_items = HotelFoodCartItems(cart=cart, user=user, product=product, price=price, quantity=quantity)
        cart_items.save()

        # Decrease the product quantity in stock
        product.ProductQuantity -= quantity
        product.save()

        cart_items = HotelFoodCartItems.objects.filter(user=user, cart=cart.id)

        total_price = 0
        for items in cart_items:
            total_price += items.price
        cart.total_price = total_price
        cart.save()
        return Response({'success': 'Items Added To Your Cart'})










    #TO UPDATE CART ITEMS
    #Eg:
    # {
    #     "id":11,
    #     "quantity":6
    # }
    def put(self, request):
        data = request.data
        cart_item = HotelFoodCartItems.objects.get(id=data.get('id'))
        quantity = data.get('quantity')
        cart_item.quantity += quantity
        cart_item.save()
        return Response({'success': 'Item Updated Sccussfully'})







    #TO DELETE ITEM IN A CART
    #Eg:
    #Pass id of the product
    # {
    #     "id":9

    # }
    def delete(self, request):
        user = request.user
        data = request.data
        cart_item = HotelFoodCartItems.objects.get(id=data.get('id'))
        cart_item.delete()

        cart = HotelFoodCart.objects.filter(user=user, ordered=False).first()
        queryset = HotelFoodCartItems.objects.filter(cart=cart)
        serializer = HotelFoodCartItemsSerializer(queryset, many=True)

        return Response(serializer.data)














class DeleteCartItemView(APIView):
    def delete(self, request):
        user = request.user
        data = request.data  # Ensure you are sending the 'id' in the request data

        try:
            cart_item = HotelFoodCartItems.objects.get(id=data.get('id'), cart__user=user, cart__ordered=False)
            cart_item.delete()

            # Fetch the updated cart items
            cart = HotelFoodCart.objects.filter(user=user, ordered=False).first()
            queryset = HotelFoodCartItems.objects.filter(cart=cart)
            serializer = HotelFoodCartItemsSerializer(queryset, many=True)

            return Response(serializer.data)

        except HotelFoodCartItems.DoesNotExist:
            return Response({"error": "Product not found in the cart"}, status=status.HTTP_404_NOT_FOUND)
















# Enter id of the Cart
# Eg:
# {
#     "id":2
    
# }

#AFTER MAKING ORDER IF YOU WANT TO DELETE A CART ITEMS USE THIS
class HotelFoodOrderView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # Create a new order
    def post(self, request):
        user = request.user
        total_price = request.data.get('total_price', 0)  # You may calculate this on the server
        cart = HotelFoodCart.objects.filter(user=user, ordered=False).first()
        
        if not cart:
            return Response({'error': 'No items in the cart'}, status=status.HTTP_400_BAD_REQUEST)

        # Create an order
        order = HotelFoodOrder.objects.create(user=user, total_price=total_price)

        total_cart_items = HotelFoodCartItems.objects.filter(user=user)

        total_price = 0
        for items in total_cart_items:
            total_price += items.price
        order.total_price = total_price
        order.save()
        
        # Retrieve cart items and add them to the order
        cart_items = HotelFoodCartItems.objects.filter(user=user, cart=cart)
        for cart_item in cart_items:
            HotelFoodOrderItems.objects.create(
                user=user,
                order=order,
                product=cart_item.product,
                price=cart_item.price,
                quantity=cart_item.quantity
            )

        # Clear the user's cart
        cart_items.delete()
        cart.total_price = 0
        cart.ordered = True
        cart.save()

        return Response(HotelFoodOrderSerializer(order).data, status=status.HTTP_201_CREATED)

    def get(self, request):
        user = request.user
        orders = HotelFoodOrder.objects.filter(user=user)
        serializer = HotelFoodOrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



#AFTER MAKING ORDER IF YOU DON'T WANT TO DELETE A CART ITEMS USE THIS
class HotelFoodOrdernNoDeleteView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # Create a new order
    def post(self, request):
        user = request.user
        total_price = request.data.get('total_price', 0)  # You may calculate this on the server
        order = HotelFoodOrder.objects.create(user=user, total_price=total_price)

        cart_items = HotelFoodCartItems.objects.filter(user=user)

        total_price = 0
        for items in cart_items:
            total_price += items.price
        order.total_price = total_price
        order.save()

        # Clear the user's cart
        # cart_items.delete()
        # cart = HotelFoodCart.objects.get(user=user, ordered=False)
        # cart.total_price = 0
        # cart.save()

        return Response(HotelFoodOrderSerializer(order).data, status=status.HTTP_201_CREATED)
        #return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)

    def get(self, request):
        user = request.user
        orders = HotelFoodOrder.objects.filter(user=user)
        serializer = HotelFoodOrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
