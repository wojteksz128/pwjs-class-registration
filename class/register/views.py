from django.shortcuts import render, render_to_response, redirect
from . import navbar
from .models import Lecturer, Subject, Student
from .forms import RegisterForm
from urllib.parse import urlencode

# Create your views here.
def copy_alerts(request):
    alert_types = ['primary', 'secondary', 'success', 'danger', 'warning', 'info', 'light', 'dark']
    alerts = {}
    for atype in alert_types:
        if request.GET.get(atype):
            alerts[atype] = request.GET.get(atype)
    return alerts

def main_window(request):
    return render(request, 'index.html', 
    { 
        'navItems': navbar.navItems, 
        'active': navbar.navItems[0],
        'alerts': copy_alerts(request)
    })

def lectures(request):
    return render(request, 'lectures.html', 
    { 
        'navItems': navbar.navItems, 
        'active': navbar.navItems[1], 
        "lectures": Lecturer.objects.all(),
        'alerts': copy_alerts(request)
    })

def subjects(request):
    return render(request, 'subjects.html', 
    { 
        'navItems': navbar.navItems, 
        'active': navbar.navItems[2],
        'subjects': Subject.objects.all(),
        'alerts': copy_alerts(request)
    })

def getSubjectInfo(request, subject_id):
    return render(request, 'modal/subjectInfo.html', 
    {
        'subject': Subject.objects.get(pk=subject_id)
    })

def getLectureInfo(request, lecture_id):
    lecturer = Lecturer.objects.get(pk=lecture_id)
    return render(request, 'modal/lectureInfo.html',
    {
        'lecture': lecturer,
        'subjects': Subject.objects.filter(lecturer__id=lecturer.id)
    })

def registerStudent(request, subject_id):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            student = Student.objects.filter(first_name=cd['first_name'], last_name=cd['last_name'], album_no=cd['album_no'])
            if len(student) == 0:
                student = Student(first_name=cd['first_name'], last_name=cd['last_name'], album_no=cd['album_no'])
                student.save()
            else:
                student = student[0]
            subject = Subject.objects.get(pk=subject_id)
            if len(subject.students.filter(pk=student.id)) != 0:
                return redirect('/subjects/?{}'.format(urlencode({
                    'info': 'Student {0} był już wcześniej zapisany do przedmiotu {1}.'.format(str(student), str(subject))
                })))
            subject.students.add(student)
            subject.save()

            return redirect('/subjects/?{}'.format(urlencode({
                'success': 'Student {0} został zapisany do przedmiotu {1}.'.format(str(student), str(subject))
            })))
    else:
        form = RegisterForm()
    return render(request, 'modal/registerStudent.html', 
    { 
        'form': form, 
        'subject_id': subject_id 
    })