from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def products(request):
    return HttpResponse('<h1>There are variety of products present in the website</h1>')
