from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LoginUserForm(forms.Form):
    username = forms.CharField(
        max_length=200, 
        required=True,
        help_text='Enter username',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Username'}
        )
        )

    password = forms.CharField(
        required=True,
        help_text="Enter password again",
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Repeat Password'}
        )
    )

    class Meta:
        model = User
        fields = ['username', 'password']

class NewUserForm(UserCreationForm):

    username = forms.CharField(
        max_length=200,
        required=True,
        help_text="Enter username",
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Username'}
        )
    )

    first_name = forms.CharField(
        max_length=100,
        required=False,
        help_text='Enter first name',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'First Name'}
        )
    )

    last_name = forms.CharField(
        max_length=100,
        required=False,
        help_text='Enter last name',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Last Name'}
        )
    )

    email = forms.EmailField(
        max_length=255,
        required=True,
        help_text='Enter email',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Email'}
        )
    )

    password1 = forms.CharField(
        required=True,
        help_text="Enter password",
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Password'}
        )
    )

    password2 = forms.CharField(
        required=True,
        help_text="Enter password again",
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Repeat Password'}
        )
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name',
                   'last_name', 'password1', 'password2']