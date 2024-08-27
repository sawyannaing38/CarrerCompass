from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.core.files.storage import default_storage
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
    
    # Storing image
    img_path = default_storage.save(f"images/{image.name}", image)
    # Try to create a user
    try:
        user = User(username=companyName, email=email)
        user.set_password(password)

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
        request.session["companyData"] = {
            "companyName" : companyName,
            "location" : location,
            "email" : email,
            "image" : img_path,
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

    data = request.session["companyData"]

    if int(verificationCode) == request.session["verificationCode"]:
        user = User.objects.create_user(username=data["companyName"], password=data["password"], email=data["email"])
        user.save()

        company = Company(user=user, image=data["image"], location=data["location"], description=data["description"])
        company.save()
        login(request, user)
        return HttpResponseRedirect(reverse("index_registration"))
    
    return render(request, "verify.html", {
        "message" : "Invalid Verification Code"
    })

# For Login
def login_view(request):
    if not request.user.is_authenticated:
        return render(request, "chooseLogin.html")
    return HttpResponseRedirect(reverse("index_registration"))
    
# For Company login
def company_login(request):
    if request.method == "GET":
        return render(request, "companyLogin.html")
    
    # For get method
    username = request.POST.get("companyName")
    password = request.POST.get("password")

    isValid = True
    companyNameMessage = ""
    passwordMessage = ""

    if not username:
        companyNameMessage = "Missing Company Name"
        isValid = False 
    
    if not password:
        passwordMessage = "Missing Password"
        isValid = False 
    
    if not isValid:
        return render(request, "companyLogin.html", {
            "companyNameMessage" : companyNameMessage,
            "passwordMessage" : passwordMessage,
            "data" : 
            {
                "companyName" : username,
                "password" : password
            }
        })
    
    user = authenticate(request, username=username, password=password)

    if user:
        login(request, user)
        return HttpResponseRedirect(reverse("index_registration"))
    
    return render(request, "companyLogin.html", {
        "message" : "Invalid Username or Password"
    })