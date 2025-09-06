from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("Welcome to the Coffee app!")

def all_chai(request):
    return render(request, 'all_chai.html')
