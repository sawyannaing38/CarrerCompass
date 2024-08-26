from django.contrib import admin
from .models import User, Employee, Company

# Register your models here.
class AdminCompany(admin.ModelAdmin):
    list_display = ["user", "image", "location", "description"]


class AdminEmployee(admin.ModelAdmin):
    list_display = ["user", "image", "location", "age", "gender", "education", "experience", "profession", "skills", "description"]

class AdminUser(admin.ModelAdmin):
    list_display = ["username", "email", "password"]

admin.site.register(Employee, AdminEmployee)
admin.site.register(Company, AdminCompany)
admin.site.register(User, AdminUser)
