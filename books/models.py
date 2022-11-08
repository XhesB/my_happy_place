from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    foreign_author = models.BooleanField(default=False)

    def __str__(self):
        return "%s %s %s" % (self.first_name, self.last_name, self.foreign_author)

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
    manager_contact_number = models.IntegerField()
    manager_email = models.EmailField()

    def __str__(self):
        return "'%s', '%s', '%s', '%s', '%s'" % (self.publishing_house_name, self.manager_first_name, self.manager_last_name, self.manager_contact_number, self.manager_email)

class Books(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    price = models.IntegerField()
    number_in_stock = models.IntegerField()
    isbn = models.CharField(max_length=40)
    translater = models.ForeignKey(Translater, on_delete=models.CASCADE)
    publishing_house = models.ForeignKey(Publishing_house, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s %s" % (self.name, self.price, self.number_in_stock)