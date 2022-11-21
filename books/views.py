from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Books
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout, models
from .forms import NewUserForm, LoginUserForm
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')

def index(request):
    books = Books.objects.all()
    return render(request, 'books/index.html', {'books': books})

@login_required(login_url='/login/')

def detail(request, books_id):

    books = get_object_or_404(Books, id=books_id)
    return render(request, 'books/detail.html', {'books': books})

def loginView(request):
    form = LoginUserForm()

    if request.method == "POST":
        form = LoginUserForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')

            else:
                messages.error(request, 'An error occurred')

        else: 
            messages.error(request, 'An error occurred')

    return render(request, 'books/login.html', 
    {
        "form": form
    })

def registerView(request):
    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            user = form.save()
            user.is_active = True
            group = models.Group.objects.get(name='my_happy_place_clients')
            group.user_set.add(user)

            login(request, user)

            return redirect('index')
        else: 
            messages.error(request, 'An error occurred')

    return render(request, 'books/register.html', {
        "form": form
    })

def logoutView(request):
    logout(request)
    return redirect('login')
