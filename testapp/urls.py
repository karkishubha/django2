from django.contrib import admin
from django.urls import path, include
from testapp import views as testapp_views

urlpatterns = [
    
    path('home/', testapp_views.home,name="testhome"),

]
