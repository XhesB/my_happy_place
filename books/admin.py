from django.contrib import admin
from .models import Author, Books, Publishing_house, Translater, Genre, Client, Staff, Invoice, InvoiceItem

# Register your models here.


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'genre_name')

class AuthorAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "foreign_author")

class TranslaterAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name")

class Publishing_house_Admin(admin.ModelAdmin):
    list_display = ("id", "publishing_house_name", "manager_first_name", "manager_last_name", "manager_contact_number", "manager_email")

class BooksAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "number_in_stock")

class ClientAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "surname", "birthday", "email")

class StaffAdmin(admin.ModelAdmin):
    list_display = ("id", "name")

class InvoiceAdmin(admin.ModelAdmin):
    list_display = ("id", "client", "date")

class InvoiceItemAdmin(admin.ModelAdmin):
    list_display = ("id", "book", "invoice", "quantity", "price", "total")


admin.site.register(Books, BooksAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Translater, TranslaterAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Publishing_house, Publishing_house_Admin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(InvoiceItem, InvoiceItemAdmin)



