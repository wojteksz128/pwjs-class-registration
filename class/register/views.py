from django.shortcuts import render, render_to_response

# Create your views here.
def main_window(request):
    return render_to_response('index.html')