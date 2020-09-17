from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #print(dir(request))
    return HttpResponse('Hi')

def test(request):
    #print(dir(request))
    return HttpResponse('<h1>Test</h1>')

# Create your views here.
