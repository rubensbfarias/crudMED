from email.headerregistry import Address
from django.db import models

#Usuario
class User(models.Model):
   name = models.CharField(max_length=100)
   email = models.CharField(max_length=100)
   password = models.CharField(max_length=100)
   createat = models.DateTimeField()

#Paciente
class Patient(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_lenght=100)
    address = models.CharField(max_lenght=100)
    number = models.Charfield(max_lenght=100)
    city = models.Charfield(max_lenght=100)
    uf = models.Charfield(max_lenght=100)
    country = models.Charfield(max_lenght=100)
    createat = models.DateTimeField()

#Agendamento
class Scheduling(models.Model):
    description = models.TextField(models.TextField(_("300")))
    status = models.CharField()
    medic = models.ForeignKey(User, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    createat = models.DateTimeField()


