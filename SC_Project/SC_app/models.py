from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Booking(models.Model):
    First_name = models.CharField(max_length=300)
    Last_name = models.CharField(max_length=300)
    Address = models.CharField(max_length=300)
    Phone_no = models.IntegerField()
    Check_in = models.DateField()
    Check_out = models.DateField()
    Number_of_visitors = models.IntegerField()
    Bed_type = models.CharField(max_length=35)
    def __str__(self):
        return self.First_name

