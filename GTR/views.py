from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello(request):
    return HttpResponse('<h1><marquee>this is GTR</marquee></h1>')
