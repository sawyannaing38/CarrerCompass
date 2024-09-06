from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)

class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="company")
    image = models.ImageField(upload_to='images/')
    location = models.TextField()
    description = models.TextField()  

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="employee")
    image = models.ImageField(upload_to="images/")
    location = models.TextField()
    description = models.TextField()
    age = models.IntegerField()
    currentCompany =models.CharField(max_length=64)
    gender = models.TextField(choices=[("male", "Male"), ("female", "Female")])
    education = models.CharField(max_length=64)
    experience = models.TextField()
    profession = models.TextField()
    skills = models.TextField()