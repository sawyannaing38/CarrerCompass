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
# For Registering
def register_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))
    return render(request, "choose.html")

# For Company Registering
def company_register(request):

    if request.method == "GET":
        return render(request, "companyRegister.html")
    
    # For POST method
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
    
    # Check that username already exist or not
    try:
        usernames = User.objects.values("username")

        if companyName in usernames:
            raise IntegrityError

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
        # Storing image
        img_path = default_storage.save(f"images/{image.name}", image)

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
    return HttpResponseRedirect(reverse("index"))

# For Verification
def verify_company(request):

    if request.method == "GET":
        return HttpResponseRedirect(reverse("register_view"))
    
    # Getting code
    verificationCode = request.POST.get("verification")

    if not verificationCode:
        return render(request, "verify.html", {
            "message" : "Missing Verification Code"
        })
    
    try:
        verificationCode = int(verificationCode)
    
    except ValueError:
        return render(request, "verify.html", {
            "message" : "Invalid Verify Code"
        })
    else:
        if not 11111 <= verificationCode <= 99999:
            return render(request, "verify.html", {
                "message" : "Invalid Verification code"
        })
    data = request.session["companyData"]


    if verificationCode == request.session["verificationCode"]:
        user = User.objects.create_user(username=data["companyName"], password=data["password"], email=data["email"])
        user.save()

        company = Company(user=user, image=data["image"], location=data["location"], description=data["description"])
        company.save()
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    
    return render(request, "verify.html", {
        "message" : "Invalid Verification Code"
    })

# For Login
def login_view(request):
    if request.method == "GET":
        if not request.user.is_authenticated:
            return render(request, "login.html")
        return HttpResponseRedirect(reverse("index"))
    
    # For get method
    username = request.POST.get("username")
    password = request.POST.get("password")

    isValid = True
    usernameMessage = ""
    passwordMessage = ""

    if not username:
        usernameMessage = "Missing User Name"
        isValid = False 
    
    if not password:
        passwordMessage = "Missing Password"
        isValid = False 
    
    if not isValid:
        return render(request, "login.html", {
            "usernameMessage" : usernameMessage,
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
        return HttpResponseRedirect(reverse("index"))
    
    return render(request, "login.html", {
        "message" : "Invalid Username or Password"
    })
    

# For Registering Employee
def employee_register(request):

    if request.method == "GET":
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("index"))
        return render(request, "employeeRegister.html")
    
    # Get method
    # Getting data
    username = request.POST.get("username")
    location = request.POST.get("location")
    email = request.POST.get("email")
    age = request.POST.get("age")
    gender = request.POST.get("gender")
    education = request.POST.get("education")
    experience = request.POST.get("experience")
    profession = request.POST.get("profession")
    currentCompany = request.POST.get("currentCompany")
    image = request.FILES.get("image")
    password = request.POST.get("password")
    confirm = request.POST.get("confirm")
    skills = request.POST.get("skills")
    description = request.POST.get("description")

    # Vaidte the user input
    isValid = True 
    usernameMessage = ""
    locationMessage = ""
    emailMessage = ""
    ageMessage = ""
    genderMessage = ""
    educationMessage = ""
    experienceMessage = ""
    professionMessage = ""
    currentCompanyMessage = ""
    passwordMessage = ""
    confirmMessage = ""
    imageMessage = ""
    skillsMessage = ""
    descriptionMessage = ""

    if not username:
        usernameMessage = "Missing Username"
        isValid = False 
    
    if not location:
        locationMessage = "Missng Location"
        isValid = False 
    
    if not email:
        emailMessage = "Missing Email"
        isValid = False

    if not age:
        ageMessage = "Missing Age"
        isValid = False
    
    if not gender:
        genderMessage = "Missing Gender"
        isValid = False 
    
    if not experience:
        experienceMessage = "Missing Email"
        isValid = False 
    
    if not profession:
        professionMessage = "Missing Profession"
        isValid = False 
    
    if not currentCompany:
        currentCompanyMessage = "Missing Current Company"
        isValid = False 
    
    if not password:
        passwordMessage = "Missing Password"
        isValid = False 
    
    if not confirm:
        confirmMessage = "Missing Confirm Message"
        isValid = False

    if not skills:
        skillsMessage = "Missing Skills"
        isValid = False 
    
    if not description:
        descriptionMessage = "Missing Description"
        isValid = False 

    if not education:
        educationMessage = "Missing Education"
        isValid = False 
    
    if not image:
        imageMessage = "Missing Image"
        isValid = False
    
    # Check age is greater than 13
    try:
        age = int(age)
    except ValueError:
        ageMessage = "Invalid Age"
        isValid = False
    else:
        if age < 13:
            ageMessage = "Age must be larger than 12"
            isValid = False 
        
    # Check gender is either male or female
    if gender not in ["male", "female"]:
        genderMessage = "Invalid Gender"
        isValid = False 
    
    # Check valid password
    if not validPassword(password):
        passwordMessage = "Invalid Password"
        isValid = False 
    
    if password != confirm:
        confirmMessage = "Passwords do not match"
        isValid = False

    if not isValid:
        return render(request, "employeeRegister.html", {
            "usernameMessage" : usernameMessage,
            "location" : locationMessage,
            "emailMessage" : emailMessage,
            "ageMessage" : ageMessage,
            "genderMessage" : genderMessage,
            "educationMessage" : educationMessage,
            "experienceMessage" : experienceMessage,
            "professionMessage" : professionMessage,
            "currentCompanyMessage" : currentCompanyMessage,
            "imageMessage" : imageMessage,
            "passwordMessage" : passwordMessage,
            "confirmMessage" : confirmMessage,
            "skillsMessage" : skillsMessage,
            "descriptionMessage" : descriptionMessage,
            "data" : {
                "username" : username,
                "location" : location,
                "email" : email,
                "age" : age,
                "gender" : gender,
                "education" : education,
                "experience" : experience,
                "profession" : profession,
                "currentCompany" : currentCompany,
                "password" : password,
                "confirm" : confirm,
                "skills" : skills,
                "description" : description
            }
        })

    # Check username already exists or not
    try:
        usernames = User.objects.values("username")

        if username in usernames:
            raise IntegrityError
    
    except IntegrityError:
        return render(request, "employeeRegister.html",{
            "errorMessage" : "Username already exists",
            "data" : {
                "username" : username,
                "location" : location,
                "email" : email,
                "age" : age,
                "gender" : gender,
                "education" : education,
                "experience" : experience,
                "profession" : profession,
                "currentCompany" : currentCompany,
                "password" : password,
                "confirm" : confirm,
                "skills" : skills,
                "description" : description
            }
        })
    
    else:

        # Storing image 
        img_path = default_storage.save(f"images/{image.name}", image)

        verificationCode = randint(11111, 99999)

        # Storing data in session
        request.session["verificationCode"] = verificationCode
        request.session["employeeData"] = {
            "username" : username,
            "location" : location,
            "password" : password,
            "email" : email,
            "age" : age,
            "gender" : gender,
            "education" : education,
            "experience" : experience,
            "profession" : profession,
            "currentCompany" : currentCompany,
            "image" : img_path,
            "skills" : skills,
            "description" : description
        }

        # send email
        sendEmail("Verification Code", f"{verificationCode}", email)
        return render(request, "employeeVerify.html")
    
# For Verifying Employee
def verify_employee(request):

    if request.method == "GET":
        return HttpResponseRedirect(reverse("register_view"))
    
    # Getting Verification code
    verificationCode = request.POST.get("verification")

    # Validate Verification Code
    if not verificationCode:
        return render(request, "employeeVerify.html", {
            "message" : "Missing Verification Code"
        })
    
    try:
        verificationCode = int(verificationCode)
    
    except ValueError:
        return render(request, "employeeVerify.html", {
            "message" : "Not a number"
        })
    else:
        if not 11111 <= verificationCode <= 99999:
            return render(request, "employeeVerify.html", {
                "message" : "Out of range"
        })
    
    # Check same verify code
    if int(verificationCode) == request.session["verificationCode"]:
        data = request.session["employeeData"]

        user = User.objects.create_user(username=data["username"], password=data["password"], email=data["email"])
        user.save()
        
        # Creating Employee
        employee = Employee(
            user=user,
            location=data["location"],
            age = data["age"],
            gender = data["gender"],
            education = data["education"],
            experience = data["experience"],
            profession = data["profession"],
            currentCompany = data["currentCompany"],
            image = data["image"],
            skills = data["skills"],
            description = data["description"]
        )

        employee.save()
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    
    return render(request, "employeeVerify.html", {
        "message" : "Invalid Verification Code"
    })