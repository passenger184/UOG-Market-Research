from django.db import models
from django.contrib.auth import get_user_model   # model of current authenticated user

User = get_user_model()

class Catagory(models.Model):
    catagories = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.catagories

# Create your models here.
class Companie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField() 
    companiesName = models.CharField(max_length=60)
    location = models.CharField(max_length=50)
    website = models.URLField(blank=True, null=True)
    active = models.BooleanField(default=False)
    phonenumber = models.CharField(max_length=100, blank=True, null=True)
    categorie = models.ForeignKey(Catagory, on_delete=models.CASCADE, blank=True, null=True)

   
    def __str__(self):
        return self.companiesName




