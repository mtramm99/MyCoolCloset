from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def indexPageView(request) :
    return HttpResponse('home page haha')

def closetPageView(request) :
    return HttpResponse('closet page lol')

def editPageView(request) :
    return HttpResponse('edit page teehee')