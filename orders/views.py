from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def orders(request):
    return HttpResponse('<h1>orders per one day is more than 10000</h1>')
