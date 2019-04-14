from django.shortcuts import render, render_to_response, HttpResponseRedirect
from . import navbar
from .models import Lecturer, Subject, Student
from .forms import RegisterForm

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

def getLectureInfo(request, lecture_id):
    lecturer = Lecturer.objects.get(pk=lecture_id)
    return render_to_response('modal/lectureInfo.html',
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
                return HttpResponseRedirect('/subjects/', {
                    'info': 'Student {0} był już wcześniej zapisany do przedmiotu {1}.'.format(str(student), str(subject))
                })
            subject.students.add(student)
            subject.save()

            return HttpResponseRedirect('/subjects/', {
                'success': 'Student {0} został zapisany do przedmiotu {1}.'.format(str(student), str(subject))
            })
    else:
        form = RegisterForm()
    return render(request, 'modal/registerStudent.html', 
    { 
        'form': form, 
        'subject_id': subject_id 
    })