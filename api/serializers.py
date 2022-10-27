from rest_framework import serializers
from api.models import User, Patient, Scheduling

class UserSerializer(serializers.ModelSerializer):
   class Meta:
       model = User
       fields = ('name', 'email', 'password', 'createat')

class PatientSerializer(serializers.ModelSerializer):
   class Meta:
       model = Patient
       fields = ('name', 'phone', 'adress', 'number', 'city', 'uf', 'country', 'createat')

class SchedulingSerializer(serializers.ModelSerializer):
   class Meta:
       model = Scheduling
       fields = ('description', 'status', 'medic', 'patient', 'createat')