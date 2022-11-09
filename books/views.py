from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Books

# Create your views here.

def index(request):
    books = Books.objects.all()
    return render(request, 'books/index.html', {'books': books})

def detail(request, books_id):

    books = get_object_or_404(Books, id=books_id)
    return render(request, 'books/detail.html', {'books': books})
