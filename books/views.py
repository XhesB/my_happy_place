from django.http import HttpResponse
from django.shortcuts import render
from .models import Books

# Create your views here.

def index(request):
    books = Books.objects.all()
    return render(request, 'books/index.html', {'books': books})
