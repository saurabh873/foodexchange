from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def base (request):
    return render (request, 'main/base.html')
def r(request):
    return HttpResponse ("hii")
