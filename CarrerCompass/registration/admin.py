from django.contrib import admin
from . import models

# Admin view for company
class AdminCompany(admin.ModelAdmin):
    list_display = ["companyName", "location", "email", "description", "image"]

# Admin view for Employee
class AdminEmployee(admin.ModelAdmin):
    list_display = ["userName", "location", "email", "age", "gender", "education", "experience", "profession","currentCompany", "skills", "description", "image"]

# Register your models here.
admin.site.register(models.Company, AdminCompany)
admin.site.register(models.Employee, AdminEmployee)
