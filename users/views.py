from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def users(request):
    return HttpResponse('<h1>users per day is increasing day by day</h1>')
