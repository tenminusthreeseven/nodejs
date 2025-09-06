from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('chai/', views.all_chai, name='all_chai'),
]
