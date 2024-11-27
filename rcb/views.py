from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def kohli(request):
    return HttpResponse('<h1>Captain of rcb</h1>')