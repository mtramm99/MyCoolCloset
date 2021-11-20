from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def indexPageView(request) :
    return render(request, 'clothingpages/index.html')

def closetPageView(request) :
    return render(request, 'clothingpages/display.html')

def editPageView(request) :
    return render(request, 'clothingpages/edit.html')

