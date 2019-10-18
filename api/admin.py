from django.contrib import admin
from .models import Project, Employee, Client
# Register your models here.

admin.site.register(Project)
admin.site.register(Employee)
admin.site.register(Client)
