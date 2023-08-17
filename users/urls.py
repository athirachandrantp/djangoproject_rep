from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginpage, name="login"),
    path('logout/', views.logoutuser, name="logout"),
    path('register/', views.registeruser, name="register"),
    path('user/', views.profiles, name="users"),
    path('profile/<str:pk>/', views.userprofile, name="users-profile"),
    path('account/', views.user_account, name="account"),
    path('edit-account/', views.edit_account, name="edit-account"),
    path('create-skill/', views.createskill, name="create-skill"),
    path('update-skill<str:pk>/', views.updateskill, name="update-skill"),
    path('delete-skill<str:pk>/', views.deleteskill, name="delete-skill"),
    path('inbox/', views.inbox, name="inbox"),
    path('message/<str:pk>/', views.viewMessage, name="message"),
    path('create-message/<str:pk>/', views.createMessage, name="create-message"),

]