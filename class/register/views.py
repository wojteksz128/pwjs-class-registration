from django.shortcuts import render, render_to_response
from . import navbar

# Create your views here.
def main_window(request):
    return render_to_response('index.html', { 'navItems': navbar.navItems, 'active': navbar.navItems[0] })

def lectures(request):
    return render_to_response('lectures.html', { 'navItems': navbar.navItems, 'active': navbar.navItems[1] })

def subjects(request):
    return render_to_response('subjects.html', { 'navItems': navbar.navItems, 'active': navbar.navItems[2] })