from django.db import models
from django.core.validators import MaxValueValidator
from registration.models import User, Company

# Create your models here.
class CompanyReview(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="reviews")
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="company_reviews")
    rating = models.IntegerField(validators=[MaxValueValidator(5)])
    description = models.TextField()

class WebsiteReview(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="website_reviews")
    rating = models.IntegerField(validators=[MaxValueValidator(5)])
    description = models.TextField()