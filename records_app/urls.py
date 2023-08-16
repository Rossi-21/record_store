from django.urls import path
from . import views

urlpatterns = [

    path('', views.register),
    path('login', views.login),
    path('dashboard', views.dashboard),

]
