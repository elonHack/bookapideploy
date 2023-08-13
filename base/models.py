from django.db import models

class Shelf(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    shelf = models.ForeignKey(Shelf, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
