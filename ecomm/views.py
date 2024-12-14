from django.http import HttpResponse
from django.shortcuts import render

def base (request):
    return render (request, 'main/base.html')
def home(request):
    return render (request, 'main/index.html')