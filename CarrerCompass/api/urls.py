from django.urls import path 
from . import views

urlpatterns = [
    path("closeJob/<int:id>", views.closeJob, name="closeJob"),
    path("createCandidate/<int:id>", views.createCandidate, name="createCandidate"),
    path("rejectCandidate/<int:id>", views.rejectCandidate, name="rejectCandidate"),
    path("getEmployee/<int:id>", views.getEmployee, name="getEmployee"),
    path("createCompanyReview/<int:id>", views.createCompanyReview, name="createCompanyReview"),
    path("createWebsiteReview/", views.createWebsiteReview, name="createWebsiteReview")
]