from django.urls import path
from . import views 

urlpatterns = [
    path("", views.index, name="index_registration"),
    path("register/", views.register_view, name="register")
]