from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Job

from datetime import datetime
from .helpers import getPostTime

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
    
    # Getting all the available jobs
    jobs = Job.objects.filter(type="open").order_by("-year", "-month", "-day", "-hour", "-minute", "-second")

    # Getting time difference between job posted and now
    today = datetime.now()

    for job in jobs:

        # Calculate time difference
        postedDate = datetime(year=job.year, month=job.month, day=job.day, hour=job.hour, minute=job.minute, second=job.second)

        differenceTime = (today - postedDate).total_seconds()

        job.text = getPostTime(differenceTime)

    # Get all type of field from jobs
    jobFields = Job.objects.filter(type="open").values("field").distinct()

    return render(request, "index.html", {
        "type" : type,
        "user" : request.user,
        "jobs" : jobs,
        "jobFields" : jobFields
    })

# For posting a job offer
def post(request):
    
    # Check valid user or not
    if request.method == "GET":
        if request.user.is_authenticated and hasattr(request.user, "company"):
            return render(request, "post.html", {
                "type" : "company"
            })
        return HttpResponseRedirect(reverse("index"))
    
    
    # For post method
    # Get data
    position = request.POST.get("position")
    salary = request.POST.get("salary")
    location = request.POST.get("location")
    workingTime = request.POST.get("workingTime")
    field = request.POST.get("field")
    description = request.POST.get("description")
    requirement = request.POST.get("requirement")
    benefit = request.POST.get("benefit")

    positionMessage = ""
    salaryMessage = ""
    locationMessage = ""
    workingTimeMessage = ""
    fieldMessage = ""
    descriptionMessage = ""
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
    
    if not description:
        descriptionMessage = "Missing Description"
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
            "descriptionMessage" : descriptionMessage,
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
        description = description,
        requirement = requirement,
        benefit = benefit,
        year = today.year,
        month = today.month,
        day = today.day,
        hour = today.hour,
        minute = today.minute,
        second = today.second
    )

    job.save()

    return HttpResponseRedirect(reverse("index"))


# For job details
def jobDetails(request, id):

    # Getting related job
    job = Job.objects.get(pk=id)

    if not job:
        return HttpResponseRedirect(reverse("index"))
    
    # Getting the type of user
    if hasattr(request.user, "employee"):
        type = "employee"

        # Check that this user already applied this job
        alreadyApplied = False 
        candidates = job.candidates.all()
        
        for candidate in candidates:
            if candidate.appliedPerson == request.user.employee:
                alreadyApplied = True

        return render(request, "job.html", {
            "type" : "employee",
            "job" : job,
            "alreadyApplied" : alreadyApplied
        })
    
    if hasattr(request.user, "company"):
        type = "company"
    
    else:
        type = "guest"
    
    return render(request, "job.html", {
        "type" : type,
        "job" : job
    })

# For offer
def offer(request):
    
    if request.method == "GET":
        if request.user.is_authenticated:
            if hasattr(request.user, "company"):
                # Get all the job related to that user
                openJobs = request.user.company.jobs.filter(type="open").order_by("-year", "-month", "-day", "-hour", "-minute", "-second")
                closeJobs = request.user.company.jobs.filter(type="close").order_by("-year", "-month", "-day", "-hour", "-minute", "-second")
                today = datetime.now()

                # Get total number of employess applied for the open jobs, posted time and total number of employees remaining(not rejected)
                for job in openJobs:
                    postDate = datetime(year=job.year, month=job.month, day=job.day, hour=job.hour, minute=job.minute, second=job.second)
                    differenceTime = (today - postDate).total_seconds()
                    job.text = getPostTime(differenceTime)

                    job.applyCount = job.candidates.count()
                    job.remainingCount = job.candidates.filter(reject=False).count()
                
                
                # Adding Candidate count, posted time and remaining candidates(not rejected) for each close job
                for job in closeJobs:
                    postDate = datetime(year=job.year, month=job.month, day=job.day, hour=job.hour, minute=job.minute, second=job.second)
                    differenceTime = (today - postDate).total_seconds()
                    job.text = getPostTime(differenceTime)

                    job.applyCount = job.candidates.count()
                    job.remainingCount = job.candidates.filter(reject=False).count()
                
                return render(request, "offer.html", {
                    "openJobs" : openJobs,
                    "closeJobs" : closeJobs,
                    "type" : "company"
                })
            return HttpResponseRedirect(reverse("index"))
        return HttpResponseRedirect(reverse("index"))


# For getting candidates of specific job
def getCandidates(request, id):
    
    # Check the user is authenticated, company and owner of job id
    if request.user.is_authenticated:
        if hasattr(request.user, "company"):
            # Getting the job
            try:
                job = Job.objects.get(pk=id)
            except Job.DoesNotExist:
                return HttpResponseRedirect(reverse("offer"))
            if job.owner == request.user.company:
                # Getting all the candidates for that job
                candidates = job.candidates.filter(reject=False)

                if candidates:
                    return render(request, "candidates.html",{
                        "candidates" : candidates,
                        "firstCandidate" : candidates[0],
                        "job" : job,
                        "type" : "company"
                    })
                return HttpResponseRedirect(reverse("offer"))
            return HttpResponseRedirect(reverse("offer"))
        return HttpResponseRedirect(reverse("index"))
    return HttpResponseRedirect(reverse("index"))