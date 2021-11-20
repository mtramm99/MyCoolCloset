from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def indexPageView(request) :
    return render(request, 'index.html')

def closetPageView(request) :
    return render(request, 'display.html')

def editPageView(request) :
    return render(request, 'edit.html')

