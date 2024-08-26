from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        if hasattr(request.user, "company"):
            return render(request, "index.html", {
                "type" : "company",
                "company" : request.user.company
            })
        
        elif hasattr(request.user, "employee"):
            return render(request, "index.html", {
                "type" : "employee",
                "employee" : request.user.employee
            })

    return render(request, "index.html", {
        "type" : "guest"
    })

# For Registering
def register_view(request):
    return render(request, "choose.html")

# For Company Registering
def company_register(request):

    if request.method == "GET":
        return render(request, "companyRegister.html")