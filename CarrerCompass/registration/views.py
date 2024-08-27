from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.urls import reverse
from .models import User, Employee, Company
from .helpers import validPassword, sendEmail
from random import randint

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        if hasattr(request.user, "company"):
            type = "company"
        
        elif hasattr(request.user, "employee"):
            type = "employee"
        
        else:
            type = "company"
    else:
        type = "guest"
    
    return render(request, "index.html", {
        "type" : type,
        "user" : request.user
    })

# For Registering
def register_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index_registration"))
    return render(request, "choose.html")

# For Company Registering
def company_register(request):

    if request.method == "GET":
        return render(request, "companyRegister.html")
    
    # For post method
    # Get data first
    companyName = request.POST.get("companyName")
    location = request.POST.get("location")
    email = request.POST.get("email")
    image = request.FILES.get("image")
    password = request.POST.get("password")
    confirm = request.POST.get("confirm")
    description = request.POST.get("description").strip()

    # State Variable
    isValid = True 
    companyMessage = ""
    locationMessage = ""
    emailMessage = ""
    imageMessage = ""
    passwordMessage = ""
    confirmMessage = ""
    descriptionMessage = ""

    # Validate the user input
    if not companyName:
        companyMessage = "Missing Company Name"
        isValid = False

    if not location:
        locationMessage = "Missing Location"
        isValid = False 

    if not email:
        emailMessage = "Missing Email"
        isValid = False 
    
    if not image:
        imageMessage = "Missing Image"
        isValid = False 

    if not password:
        passwordMessage = "Missing Password"
        isValid = False 
    
    if not confirm:
        confirmMessage = "Missing Confirm Password"
        isValid = False 
    
    if not validPassword(password):
        passwordMessage = "Password doesn't match specificitaion"
        isValid = False 
    
    if confirm and confirm != password:
        confirmMessage = "Passwords do not match each other"
        isValid = False

    if not description:
        descriptionMessage = "Missing Description"
        isValid = False

    if image:
        _, extension = image.name.split(".", 1)

        if extension not in ["jpg", "jpeg", "png"]:
            imageMessage = "Invalid Image Format"
            isValid = False 
    
    if not isValid:
        return render(request, "companyRegister.html", {
            "companyMessage" : companyMessage,
            "locationMessage" : locationMessage,
            "emailMessage" : emailMessage,
            "imageMessage" : imageMessage,
            "passwordMessage" : passwordMessage,
            "confirmMessage" : confirmMessage,
            "descriptionMessage" : descriptionMessage,
            "data" :
            {
                "companyName" : companyName,
                "location" : location,
                "email" : email,
                "password" : password,
                "confirm" : confirm,
                "description" : description
            }
        })
    # Try to create a user
    try:
        user = User.objects.create_user(username=companyName, password=password, email=email)

    # Catch IntegrityError
    except IntegrityError:
        return render(request, "companyRegister.html", {
            "errorMessage" : "Username already exists",
            "data" : 
            {
                "companyName" : companyName,
                "location" : location,
                "email" : email,
                "password" : password,
                "confirm" : confirm,
                "description" : description
            }
        })
    
    # If error doesn't happen
    else:
        
        # Generating verification code
        verificationCode = randint(11111, 99999)

        # Saving the data
        request.session["verificationCode"] = verificationCode
        request.session["data"] = {
            "companyName" : companyName,
            "location" : location,
            "email" : email,
            "image" : image,
            "password" : password,
            "confirm" : confirm,
            "description" : description
        }

        # Sending Email
        sendEmail("Verification Code", f"{verificationCode}", email)

        return render(request, "verify.html")


# For Loggout Out
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index_registration"))

# For Verification
def verify_company(request):

    if request.method == "GET":
        return HttpResponseRedirect(reverse("register_view"))
    
    # Getting code
    verificationCode = request.POST.get("verification")

    if int(verificationCode) == request.session["verificationCode"]:
        user = User.objects.create_user(username=request.session["companyName"], password=request.session["data"]["password"], email=request.session["data"]["email"])
        user.save()

        company = Company(user=user, image=request.session["data"]["image"], location=request.session["data"]["location"], description=request.session["data"]["description"])
        company.save()
        login(request, user)
        return HttpResponseRedirect(reverse("register_index"))