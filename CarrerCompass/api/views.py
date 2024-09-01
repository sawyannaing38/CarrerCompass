from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializer import JobSerializer 
from rest_framework import status
from jobs.models import Job 

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
        return Response(status.HTTP_400_BAD_REQUEST)
    

