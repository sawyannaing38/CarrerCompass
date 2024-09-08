from django.urls import path 
from . import views

urlpatterns = [
    path("companyProfile/<int:id>/", views.companyProfile, name="companyProfile")
]