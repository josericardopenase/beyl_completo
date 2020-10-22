from django.contrib import admin
from django.urls import path, re_path
from .views import home, plans, team

urlpatterns = [
    path('', home, name="home"),
    path('planes/', plans, name="plans"),
    path('planes/<str:plan>/', plans, name="anual_plans"),
    path('team/', team, name="team" )
    
]
