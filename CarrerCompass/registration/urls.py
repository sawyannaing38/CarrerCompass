from django.urls import path
from . import views 

urlpatterns = [
    path("", views.index, name="index_registration"),
    path("register/", views.register_view, name="register_view"),
    path("companyRegister/", views.company_register, name="company_register"),
    path("logout/", views.logout_view, name="logout"),
    path("verifyCompany/" , views.verify_company, name="verify_company"),
    path("login/", views.login_view, name="login"),
    path("companyLogin/", views.company_login, name="company_login")
]