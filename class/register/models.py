from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Lecturer(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()

    def __str__(self):
        return "%s %s (%s)" % (self.first_name, self.last_name, self.email)

class Student(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    album_no = models.IntegerField()

    def __str__(self):
        return "%s %s (%s)" % (self.first_name, self.last_name, self.album_no)

class Subject(models.Model):
    name = models.CharField(max_length=100)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, blank=True)

    def __str__(self):
        return "%s\nProwadzący: %s" % (self.name, self.lecturer)