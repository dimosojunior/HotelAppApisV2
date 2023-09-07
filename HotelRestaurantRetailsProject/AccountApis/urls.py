from . import views
from django.urls import path


urlpatterns = [

    path('register_user/', views.RegistrationView.as_view(), name='register'),
    path('login_user/', views.ReactLoginView.as_view(), name='login'),
    path('logout_user/', views.LogoutView.as_view(), name='login'),
    path('user_data/', views.UserDataView.as_view(), name='user-data'),

]