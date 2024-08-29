from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Job

from datetime import datetime

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

# For posting a job offer
def post(request):
    
    # Check valid user or not
    if request.method == "GET" and request.user.is_authenticated and hasattr(request.user, "company"):
        return render(request, "post.html", {
            "type" : "company"
        })
    
    # For post method
    # Get data
    position = request.POST.get("position")
    salary = request.POST.get("salary")
    location = request.POST.get("location")
    workingTime = request.POST.get("workingTime")
    field = request.POST.get("field")
    requirement = request.POST.get("requirement")
    benefit = request.POST.get("benefit")

    positionMessage = ""
    salaryMessage = ""
    locationMessage = ""
    workingTimeMessage = ""
    fieldMessage = ""
    requirementMessage = ""
    benefitMessage = ""

    # Validate user input
    isValid = True 

    if not position:
        positionMessage = "Missing Position"
        isValid = False 
    
    if not salary:
        positionMessage = "Missing Salary"
        isValid = False 
    
    if not location:
        locationMessage = "Missing Location"
        isValid = False 
    
    if not workingTime:
        workingTimeMessage = "Missing Working Time"
        isValid = False 
    
    if not field:
        fieldMessage = "Missing Field"
        isValid = False 
    
    if not requirement:
        requirementMessage = "Missing Requirement"
        isValid = False 
    
    if not benefit:
        benefitMessage = "Missing Benefit"
        isValid = False 
    
    # Validate salay and workingTime
    if salary:
        try:
            salary = int(salary)
        except ValueError:
            salaryMessage = "Invalid Salary"
            isValid = False 

    if workingTime:
        try:
            workingTime = int(workingTime)
        except ValueError:
            workingTimeMessage = "Invalid Working time"
            isValid = False 
    
    if not isValid:
        return render(request, "post.html", {
            "positionMessage" : positionMessage,
            "salayMessage" : salaryMessage,
            "locationMessage" : locationMessage,
            "workingTimeMessage" : workingTimeMessage,
            "fieldMessage" : fieldMessage,
            "requirementMessage" : requirementMessage,
            "benefitMessage" : benefitMessage
        })
    
    # Getting today
    today = datetime.now()

    # If all user input is Valid
    # Create a job
    job = Job(
        owner = request.user.company,
        position = position,
        salary = salary,
        location = location,
        workingTime = workingTime,
        field = field,
        requirement = requirement,
        benefit = benefit,
        year = today.year,
        month = today.month,
        day = today.day
    )

    job.save()

    return HttpResponseRedirect(reverse("index"))