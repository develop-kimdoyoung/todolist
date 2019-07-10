from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list_add/', views.list_add, name='list_add'),
    path('list_delete/', views.list_delete, name='list_delete'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
