from django.db import models
from registration.models import Employee, Company

# Create your models here.
class Job(models.Model):
    owner = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="jobs")
    position = models.CharField(max_length=64)
    salary = models.IntegerField()
    location = models.TextField()
    workingTime = models.IntegerField()
    field = models.CharField(max_length=64)
    description = models.TextField()
    requirement = models.TextField()
    benefit = models.TextField()
    type = models.CharField(max_length=5, default="open")
    year = models.IntegerField()
    month = models.IntegerField()
    day = models.IntegerField()
    hour = models.IntegerField()
    minute = models.IntegerField()
    second = models.IntegerField()

class Candidate(models.Model):
    appliedPerson = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="applied_job")
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="candidates")
    reject = models.BooleanField(default=False)