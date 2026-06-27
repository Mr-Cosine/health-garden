"""
URL configuration for health_garden project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name = 'dashboard'),

    path('calories/', views.calories_panel, name = 'calories_panel'),
    path('api/food-list/create/', views.food_add, name='food_create'),
    path('api/food-list/delete/', views.food_delete, name='food_delete'),
    path('api/food-list/get_today/', views.get_food_list_json, name='get_food_list_json'),
    path('api/food-list/get_full/', views.get_food_list_json_full, name='get_food_list_json_full'),

    path('hydration/', views.hydration_panel, name = 'hydration_panel'),
    path('api/water-list/create/', views.water_add, name='water_add'),
    path('api/water-list/delete/', views.water_delete, name='water_delete'),
    path('api/water-list/get_today/', views.get_water_list_json, name='get_water_list_json'),
    path('api/water-list/get_full/', views.get_water_list_json_full, name='get_water_list_json_full'),
    
    path('medication/', views.medication_panel, name='medication_panel'),
]