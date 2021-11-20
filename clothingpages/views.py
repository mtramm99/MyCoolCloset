from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def indexPageView(request) :
    return HttpResponse('thomas owns the homepage')

def closetPageView(request) :
    return HttpResponse('closet page lol')

def editPageView(request) :
    return HttpResponse('edit page teehee')

