from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def welcome(request):
    s= '<h1>Hi this is marsh<h1>'
    return HttpResponse(s)

def wish(request):
    return render(request,'testApp/demo1.html')
