
from django.db import models

class CarBrand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CarPart(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    photos = models.ManyToManyField('Photo', blank=True)


    def __str__(self):
        return self.name

class Photo(models.Model):
    image = models.ImageField(upload_to='carpart_photos/')
