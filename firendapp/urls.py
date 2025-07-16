from django.contrib import admin
from django.urls import path, include
from firendapp import views as firend_views

urlpatterns = [
    
    path('home/',firend_views.home,name="home")

]