from django.urls import path
from . import views

urlpatterns = [

    path('', views.register, name="register"),
    path('login', views.loginPage, name="login"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('logout/', views.logoutUser, name="logout"),

]
