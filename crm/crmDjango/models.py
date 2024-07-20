from django.db import models

class Client(models.Model):
    name = models.CharField(blank=True, max_length=20)
    tel = models.CharField(blank=True, max_length=11)
    email = models.CharField(blank=True, max_length=30)
    city = models.CharField(blank=True, max_length=15)

class Product(models.Model):
    name = models.CharField(blank=True, max_length=20)

class Applications(models.Model):
    client = models.ForeignKey(Client, blank=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, blank=True, on_delete=models.CASCADE)
    price = models.IntegerField(blank=True, default=0)
    status = models.CharField(blank=True, default="Активна", max_length=10)

class Sales(models.Model):
    client = models.ForeignKey(Client, blank=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, blank=True, on_delete=models.CASCADE)
    price = models.IntegerField(blank=True, default=0)
    isReady = models.BooleanField(blank=True, default=False)

class Workers(models.Model):
    name = models.CharField(blank=True, max_length=20)
    tel = models.CharField(blank=True, max_length=11)
    email = models.CharField(blank=True, max_length=30)
    jobTitle = models.CharField(blank=True, max_length=20)
    salary = models.IntegerField(default=0)