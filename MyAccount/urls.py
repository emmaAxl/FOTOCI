from django.urls import path 

from . import views

urlpatterns = [
    path('inscription/', views.inscription,name='inscription'),
    path('login/', views.login,name='login'),
 
]