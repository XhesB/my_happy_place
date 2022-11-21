from django.db import models
from django.utils import timezone
from django.contrib.auth.models import BaseUserManager
from django.conf import settings
from django.db.models import Sum, F
from django.contrib.auth.models import User

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    foreign_author = models.BooleanField(default=False)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

class Genre(models.Model):
    genre_name = models.CharField(max_length=255)
  

    def __str__(self):
        return "%s" % (self.genre_name)

class Translater(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

class Publishing_house(models.Model):
    publishing_house_name = models.CharField(max_length=255)
    manager_first_name = models.CharField(max_length=255)
    manager_last_name = models.CharField(max_length=255)
    manager_contact_number = models.CharField(max_length=255, null=True)
    manager_email = models.EmailField()

    def __str__(self):
        return "'%s', '%s', '%s', '%s', '%s'" % (self.publishing_house_name, self.manager_first_name, self.manager_last_name, self.manager_contact_number, self.manager_email)

class Books(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    price = models.CharField(max_length=255)
    number_in_stock = models.IntegerField()
    # isbn = models.CharField(max_length=255)
    translater = models.ForeignKey(Translater, on_delete=models.CASCADE, null=True, blank=True)
    publishing_house = models.ForeignKey(Publishing_house, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s %s" % (self.name, self.price, self.number_in_stock)

class Client(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    birthday = models.DateField()
    # phone_number = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return "%s %s %s %s" % (self.name, self.surname, self.birthday, self.email)

class Staff(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return "%s" % (self.name)

class Invoice(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    @property
    def total(self):
        return self.invoiceitem_set.all().aggregate(total=Sum(F('quantity') * F('price')))

    def __str__(self):
        return "%s %s" % (self.client, self.date)

class InvoiceItem(models.Model):
    book = models.ForeignKey('books.Books', on_delete=models.CASCADE)
    invoice = models.ForeignKey('books.Invoice', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

    @property
    def total(self):
        return self.price * self.quantity

