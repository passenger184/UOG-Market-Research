from django.db import models
from django.contrib.auth import get_user_model   # model of current authenticated user
from datetime import datetime

User = get_user_model()

class Unit(models.Model):
    unit_choice = models.CharField(max_length=255, blank=True, null=True)


    def __str__(self):
        return self.unit_choice


class Product(models.Model):
   
    Availability = (
        ('Yes','Yes'),
        ('No','No')
    )
   
    product_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    quantity = models.IntegerField()
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    availability = models.CharField(max_length=100, choices=Availability, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateTimeField(default=datetime.now)


    def __str__(self):
        return self.product_name   
    







