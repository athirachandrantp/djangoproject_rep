from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.profiles, name="users"),
    path('profile/<str:pk>/', views.userprofile, name="users-profile"),

]