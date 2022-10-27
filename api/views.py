from rest_framework import viewsets

from api.serializers import UserSerializer, PatientSerializer, SchedulingSerializer
from api.models import User, Patient, Scheduling


class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer

class PatientViewSet(viewsets.ModelViewSet):
   queryset = Patient.objects.all()
   serializer_class = PatientSerializer


class SchedulingViewSet(viewsets.ModelViewSet):
   queryset = Scheduling.objects.all()
   serializer_class = SchedulingSerializer