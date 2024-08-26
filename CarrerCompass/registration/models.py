from django.db import models

# Model
class Company(models.Model):
    companyName = models.CharField(max_length=64)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to="images/")

# For Employee
class Employee(models.Model):
    userName = models.CharField(max_length=64)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=6)
    education = models.CharField(max_length=100)
    experience = models.CharField(max_length=64)
    currentCompany = models.CharField(max_length=64)
    profession = models.CharField(max_length=64)
    skills = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to="images/")
