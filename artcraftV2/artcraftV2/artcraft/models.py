from django.db import models

# Create your models here.

class Artist(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    birthDate = models.DateField()
    address = models.CharField(max_length=50)
    phoneNumber = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    class Meta:
        db_table = "Artist"
        

class Customer(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=50)
    phoneNumber = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    class Meta:
        db_table = "Customer"

class Artwork(models.Model):
    year = models.DateField(max_length=50)
    title = models.CharField(max_length=50)
    price = models.IntegerField()
    type = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    artistID = models.ForeignKey(Artist, on_delete=models.CASCADE)

    class Meta:
        db_table = "Artwork"
        

class Order(models.Model):
    orderPrice = models.IntegerField() # there will be a shipping fee teehee
    orderDate = models.DateField(max_length=20)
    artworkID = models.ForeignKey(Artwork, on_delete=models.CASCADE)
    customerID = models.ForeignKey(Customer, on_delete=models.CASCADE)

    class Meta:
        db_table = "Order"
        