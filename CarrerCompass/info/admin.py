from django.contrib import admin
from .models import WebsiteReview, CompanyReview

# Admin view
class WebsiteReviewAdmin(admin.ModelAdmin):
    list_display = ["id", "writer", "rating", "description"]

class CompanyReviewAdmin(admin.ModelAdmin):
    list_display = ["id", "company", "writer", "rating", "description"]

# Register your models here.
admin.site.register(WebsiteReview, WebsiteReviewAdmin)
admin.site.register(CompanyReview, CompanyReviewAdmin)