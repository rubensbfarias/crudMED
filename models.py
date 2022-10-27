from email.headerregistry import Address
from django.db import models

#Usuario
class User(models.Model):
   Name = models.CharField(max_length=100)
   Email = models.CharField(max_length=100)
   Password = models.CharField(max_length=100)
   CreateAt = models.DateTimeField()

#Paciente
class Patient(models.Model):
    Name = models.CharField(max_length=100)
    Phone = models.CharField(max_lenght=100)
    Address = models.CharField(max_lenght=100)
    Number = models.Charfield(max_lenght=100)
    City = models.Charfield(max_lenght=100)
    UF = models.Charfield(max_lenght=100)
    Country = models.Charfield(max_lenght=100)
    CreateAt = models.DateTimeField()

#Agendamento
class Scheduling(models.Model):
    CreateAt = models.DateTimeField()
    Description = models.TextField(models.TextField(_("300")))
    Status = models.CharField()
    Medic = models.ForeignKey(User, on_delete=models.CASCADE)
    Patient = models.ForeignKey()


