from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import JobSerializer, CandidateSerializer
from rest_framework import status
from jobs.models import Job, Candidate

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