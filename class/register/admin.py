from django.contrib import admin
from .models import Lecturer, Student, Subject

# Register your models here.

admin.site.register(Lecturer)
admin.site.register(Student)
admin.site.register(Subject)