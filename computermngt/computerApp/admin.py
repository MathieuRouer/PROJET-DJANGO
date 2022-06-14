from django.contrib import admin

# AJOUT DE NOS 2 MODELES

from .models import Machine
from .models import employe

admin.site.register(Machine)
admin.site.register(employe)