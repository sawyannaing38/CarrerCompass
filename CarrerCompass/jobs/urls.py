from django.urls import path 
from . import views 

urlpatterns = [
    path("", views.index, name="index"),
    path("post/", views.post, name="post"),
    path("jobDetails/<int:id>", views.jobDetails, name="jobDetails"),
    path("offer/", views.offer, name="offer"),
    path("getCandidates/<int:id>", views.getCandidates, name="getCandidates"),
    path("jobs/", views.jobs, name="jobs"),
    path("companyList/", views.companyList, name="companyList"),
    path("getCompanyJobs/<int:id>/", views.getCompanyJobs, name="getCompanyJobs")
]