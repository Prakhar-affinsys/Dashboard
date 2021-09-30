from django.db import models

# Create your models here.
from django.db import models


class Person(models.Model):
	name = models.CharField(max_length=100,blank=True, null=True)
	income = models.DecimalField(max_digits=10, decimal_places=2)
	age = models.IntegerField(blank=True, null=True)
	hometown = models.CharField(max_length=50, blank=True, null=True)
	zipcode = models.CharField(max_length=6, blank=True, null=True)
	city = models.CharField(max_length=50, blank=True, null=True)
	date = models.DateTimeField(blank=True, null=True)


