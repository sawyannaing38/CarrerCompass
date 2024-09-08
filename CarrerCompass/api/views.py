from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import JobSerializer, CandidateSerializer, EmployeeSerializer, CompanyReviewSerializer
from rest_framework import status
from jobs.models import Job, Candidate
from registration.models import Employee, Company
from registration.helpers import sendEmail

# For Closing Job

@api_view(["PATCH"])
def closeJob(request, id):

    # Try to create a job object
    try:
        job = Job.objects.get(pk=id)
    except Job.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = JobSerializer(job, data=request.data, partial=True)

    
    if request.user.company == job.owner:
        if serializer.is_valid():
            serializer.save()
            print("Save")
            return Response(serializer.data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    

# For Creating Candidate
@api_view(["POST"])
def createCandidate(request, id):
    
    if request.user.is_authenticated:

        if hasattr(request.user, "employee"):
            
            # Try to get the job
            try:
                job = Job.objects.get(pk=id)
            except Job.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            
            data = {"appliedPerson" : request.user.employee.id, "job" : job.id}
            # Create serializer
            serializer = CandidateSerializer(data=data)

            if serializer.is_valid():
                serializer.save()

                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_421_MISDIRECTED_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_400_BAD_REQUEST)

# For Deleting Candidate
@api_view(["PATCH"])
def rejectCandidate(request, id):
    
    if request.user.is_authenticated:
        if hasattr(request.user, "company"):
            
            # Try to get the candidate of id
            try:
                candidate = Candidate.objects.get(pk=id)
            except Candidate.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            
            # Check the request user is the onwer of the job
            if request.user.company == candidate.job.owner:
                
                # Create serializer
                serializer = CandidateSerializer(candidate, data=request.data, partial=True)

                if serializer.is_valid():
                    serializer.save()
                    sendEmail("Rejection", f"Your are rejected from {candidate.job.position} at {candidate.job.owner.user.username}", candidate.job.owner.user.email)
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
            return Response(status=status.HTTP_403_FORBIDDEN)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_400_BAD_REQUEST)

# For Getting specific employee
@api_view(["GET"])
def getEmployee(request, id):

    try:
        employee = Employee.objects.get(pk=id)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND) 
    
    # Create serializer
    serializer = EmployeeSerializer(employee)
    return Response(serializer.data, status=status.HTTP_200_OK)

# Creating Review for company
@api_view(["POST"])
def createCompanyReview(request, id):
    if request.user.is_authenticated:

        # Try to get company of id
        try:
            company = Company.objects.get(pk=id)
        except Company.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        data = request.data.copy()
        data["company"] = id
        data["writer"] = request.user.id

        # Create serializer
        seralizer = CompanyReviewSerializer(data=data)

        if seralizer.is_valid():
            seralizer.save()
            return Response(seralizer.data, status=status.HTTP_201_CREATED) 
        return Response(seralizer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_403_FORBIDDEN)

