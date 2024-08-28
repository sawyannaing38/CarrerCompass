<<<<<<< HEAD
from django.urls import path 
from . import views 
=======
from django.urls import path
from . import views
>>>>>>> 11bd1ef5f14c64eda843754c944c09f05252ca3f

urlpatterns = [
    path("", views.index, name="index")
]