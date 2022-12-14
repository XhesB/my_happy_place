from django.urls import path 
from . import views
from django.urls import path, include


# app_name = 'books'



urlpatterns = [
    path('', views.index, name='index'),
    path('<int:books_id>', views.detail, name='detail'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('register/', views.registerView, name='register'),
]