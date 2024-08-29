from django.contrib import admin
from .models import Job, Candidate

# Admin view for job
class AdminJob(admin.ModelAdmin):
    list_display = ["owner", "position", "salary", "location", "workingTime", "field"]

# Admin view for Candidate
class AdminCandidate(admin.ModelAdmin):
    list_display = ["appliedPerson", "job"]

# Register your models here.
admin.site.register(Job, AdminJob)
admin.site.register(Candidate, AdminCandidate)
