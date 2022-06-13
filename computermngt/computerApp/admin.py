from django.contrib import admin

# Register your models here.

from .models import Machine
from .models import employe

admin.site.register(Machine)
admin.site.register(employe)