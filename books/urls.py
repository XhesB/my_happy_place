from django.urls import path 
from . import views
from django.urls import path, include


app_name = 'books'


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:books_id>', views.detail, name='detail'),
]