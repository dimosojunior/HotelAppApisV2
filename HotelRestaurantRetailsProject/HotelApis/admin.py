from django.contrib import admin
from .models import *
# Register your models here.
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class MyUserAdmin(BaseUserAdmin):
    list_display=('id','username', 'email', 'date_joined', 'last_login', 'is_admin', 'is_active', 'is_hotel_user','is_restaurant_user','is_retails_user')
    search_fields=('email', 'first_name', 'last_name')
    readonly_fields=('date_joined', 'last_login')
    filter_horizontal=()
    list_filter=('last_login',)
    fieldsets=()

    add_fieldsets=(
        (None,{
            'classes':('wide'),
            'fields':('email', 'username', 'password1', 'password2'),
        }),
    )

    ordering=('email',)



#----------------INVENTORIES------------
class HotelInventoryAdmin(admin.ModelAdmin):

    list_display = ["Category","Created","Updated"]
    list_filter =["Created","Updated"]
    search_fields = ["Category"]
class RestaurantInventoryAdmin(admin.ModelAdmin):

    list_display = ["Category","Created","Updated"]
    list_filter =["Created","Updated"]
    search_fields = ["Category"]

class RetailsInventoryAdmin(admin.ModelAdmin):

    list_display = ["Category","Created","Updated"]
    list_filter =["Created","Updated"]
    search_fields = ["Category"]





#-----------------------FOOD CATEGORY--------------------


class HotelFoodCategoriesAdmin(admin.ModelAdmin):

    list_display = ["CategoryName","Store","Created","Updated"]
    list_filter =["Created","Updated"]
    search_fields = ["CategoryName"]


class RestaurantFoodCategoriesAdmin(admin.ModelAdmin):

    list_display = ["CategoryName","Store","Created","Updated"]
    list_filter =["Created","Updated"]
    search_fields = ["CategoryName"]


class RetailsFoodCategoriesAdmin(admin.ModelAdmin):

    list_display = ["CategoryName","Store","Created","Updated"]
    list_filter =["Created","Updated"]
    search_fields = ["CategoryName"]




#-----------------------DRINKS CATEGORY--------------------


class HotelDrinksCategoriesAdmin(admin.ModelAdmin):

    list_display = ["CategoryName","Store","Created","Updated"]
    list_filter =["Created","Updated"]
    search_fields = ["CategoryName"]


class RestaurantDrinksCategoriesAdmin(admin.ModelAdmin):

    list_display = ["CategoryName","Store","Created","Updated"]
    list_filter =["Created","Updated"]
    search_fields = ["CategoryName"]


class RetailsDrinksCategoriesAdmin(admin.ModelAdmin):

    list_display = ["CategoryName","Store","Created","Updated"]
    list_filter =["Created","Updated"]
    search_fields = ["CategoryName"]








#-----------------------ROOM CLASSES----------------------------------

class RoomsClassesAdmin(admin.ModelAdmin):

    list_display = ["RoomClass","Quantity","Created","Updated"]
    list_filter =["Created","Updated"]
    search_fields = ["RoomClass"]











#--------------------------Hotel Food ProductsS--------------------

class HotelFoodProductsAdmin(admin.ModelAdmin):

    list_display = ["id","product_name","product_second_name","productCategory", "price","ProductQuantity","Created","Updated"]
    list_filter =["Created","Updated","productCategory"]
    search_fields = ["product_name","product_second_name"]








#---------------------HOTEL FOOD CART---------------------
class HotelFoodCartAdmin(admin.ModelAdmin):
    list_display = ["id","user","ordered", "total_price", "Created","Updated"]
    list_filter =["Created"]
    search_fields = ["user"]

class HotelFoodCartItemsAdmin(admin.ModelAdmin):
    list_display = ["id","user","cart", "product","price","quantity", "Created","Updated"]
    list_filter =["Created","Updated"]
    search_fields = ["user"]
    
class HotelFoodOrderAdmin(admin.ModelAdmin):
    list_display = ["user","total_price", "created"]
    list_filter =["created"]
    search_fields = ["user"]

class HotelFoodOrderItemsAdmin(admin.ModelAdmin):
    list_display = ["id","user","order", "product","price","quantity", "Created","Updated"]
    list_filter =["Created","Updated"]
    search_fields = ["user"]



admin.site.register(MyUser, MyUserAdmin)


admin.site.register(HotelInventory, HotelInventoryAdmin)
admin.site.register(RestaurantInventory, RestaurantInventoryAdmin)
admin.site.register(RetailsInventory, RetailsInventoryAdmin)


#----------------FOOD CATEGORY-----------------
admin.site.register(RestaurantFoodCategories, RestaurantFoodCategoriesAdmin)
admin.site.register(HotelFoodCategories, HotelFoodCategoriesAdmin)
admin.site.register(RetailsFoodCategories, RetailsFoodCategoriesAdmin)


#----------------DRINKS CATEGORY-----------------
admin.site.register(RestaurantDrinksCategories, RestaurantDrinksCategoriesAdmin)
admin.site.register(HotelDrinksCategories, HotelDrinksCategoriesAdmin)
admin.site.register(RetailsDrinksCategories, RetailsDrinksCategoriesAdmin)


#----------------ROOM CLASSES----------------
admin.site.register(RoomsClasses, RoomsClassesAdmin)


#---------------------HOTEL FOOD PRODUCTS--------------------
admin.site.register(HotelFoodProducts, HotelFoodProductsAdmin)
admin.site.register(HotelFoodCart, HotelFoodCartAdmin)
admin.site.register(HotelFoodCartItems, HotelFoodCartItemsAdmin)
admin.site.register(HotelFoodOrder,HotelFoodOrderAdmin)
admin.site.register(HotelFoodOrderItems,HotelFoodOrderItemsAdmin)