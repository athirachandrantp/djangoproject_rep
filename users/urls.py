from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginpage, name="login"),
    path('logout/', views.logoutuser, name="logout"),
    path('register/', views.registeruser, name="register"),
    path('user/', views.profiles, name="users"),
    path('profile/<str:pk>/', views.userprofile, name="users-profile"),

]