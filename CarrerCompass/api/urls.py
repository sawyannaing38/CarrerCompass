from django.urls import path 
from . import views

urlpatterns = [
    path("closeJob/<int:id>", views.closeJob, name="closeJob")
]