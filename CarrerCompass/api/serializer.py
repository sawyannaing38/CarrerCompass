from rest_framework import serializers 
from jobs.models import Job, Candidate
from registration.models import Employee, User

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"
    
class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class EmployeeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Employee
        fields = "__all__"