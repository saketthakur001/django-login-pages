from django.shortcuts import render
from django.http import HttpResponseServerError, HttpResponse

# Create your views here.
def about(request):
    return HttpResponse("this is the about page")

def help_(request):
    return HttpResponse("this is the help page")

def Home(request):
    return HttpResponse("this is the Home page")
