from django.shortcuts import render
from registration.models import Company, Employee
from django.urls import reverse
from django.db.models import Avg
from django.http import HttpResponseRedirect

# Create your views here.
def companyProfile(request, id):

    # Getting the company
    try:
        company = Company.objects.get(pk=id)
    except Company.DoesNotExist:
        return HttpResponseRedirect(reverse("index"))
    else:
        # Getting the type of request user
        if hasattr(request.user, "company"):
            type = "company"
            
            # Check request user is same as this company
            if request.user.company == company:
                owner = True

        elif hasattr(request.user, "employee"):
            type = "employee"
            owner = False 
        else:
            type = "guest"
            owner = False 

        # Getting 5 review of company
        reviews = company.reviews.all().order_by("-rating")
        reviews = reviews[0:5]

        if reviews:
            # Getting reviewRating and reviewRemainRating for each review
            for review in reviews:
                review.reviewRating = range(review.rating)
                review.reviewRemainRating = range(5 - review.rating)
                review.type = "company" if hasattr(review.writer, "company") else "employee"
        
        if reviews:
            # Getting average rating for the company
            avgRating = company.reviews.all().aggregate(Avg("rating"))
            avgRating = round(avgRating["rating__avg"])
        else:
            avgRating = 0

        company.rating = range(avgRating)
        company.remainRating = range(5 - avgRating)

        return render(request, "companyProfile.html", {
            "company" : company,
            "reviews" : reviews,
            "type" : type,
            "owner" : owner
        })

        
def employeeProfile(request, id):
    # Getting the type request user
    if hasattr(request.user, "company"):
        type = "company"
    elif hasattr(request.user, "employee"):
        type = "employee"
    else:
        type = "guest"
    
    # Try to get the employee
    try:
        employee = Employee.objects.get(pk=id)
    except Employee.DoesNotExist:
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "employeeProfile.html", {
            "type" : type,
            "employee" : employee
        })