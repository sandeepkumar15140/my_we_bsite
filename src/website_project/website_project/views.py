from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def us(request):
    return HttpResponse("We are the world's best Diamond Merchants")