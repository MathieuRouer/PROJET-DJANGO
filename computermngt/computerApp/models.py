from platform import machine
import re
from wsgiref.util import request_uri
from django.db import models
from regex import F
import requests
from datetime import datetime

# Create your models here.

class Machine(models.Model):
    TYPE = (
        ('PC', ('PC - Run windows ')) ,
        ('Mac', ( ' MAc - Run MacOS ')) ,
        ('Serveur', ('Serveur - Simple Server to deploy virtual machines')),
        ('Switch', ('Switch - To maintains and connect servers')),
    )

    id = models.AutoField(primary_key=True, editable=False)
    nom = models.CharField(max_length=6)
    maintenanceDate = models.DateField(default = datetime.now())
    mach = models.CharField(max_length=32, choices=TYPE, default='PC')
