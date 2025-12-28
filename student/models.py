from django.db import models

# Create your models here.
class StudentModel(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    age = models.IntegerField()
    phone = models.CharField(max_length=14)
    email = models.EmailField(max_length=255)
