from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),         # homepage
    path('chai/', views.all_chai, name='all_chai'),  # /chai/ page
]
