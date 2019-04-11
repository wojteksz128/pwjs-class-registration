from django.shortcuts import render, render_to_response
from . import navbar
from .models import Lecturer, Subject

# Create your views here.
def main_window(request):
    return render_to_response('index.html', 
    { 
        'navItems': navbar.navItems, 
        'active': navbar.navItems[0] 
    })

def lectures(request):
    return render_to_response('lectures.html', 
    { 
        'navItems': navbar.navItems, 
        'active': navbar.navItems[1], 
        "lectures": Lecturer.objects.all() 
    })

def subjects(request):
    return render_to_response('subjects.html', 
    { 
        'navItems': navbar.navItems, 
        'active': navbar.navItems[2],
        'subjects': Subject.objects.all()
    })

def getSubjectInfo(request, subject_id):
    return render_to_response('modal/subjectInfo.html', 
    {
        'subject': Subject.objects.get(pk=subject_id)
    })