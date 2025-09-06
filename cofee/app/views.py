from django.http import HttpResponse
from django.shortcuts import render

def home(request):
  return HttpResponse("welcome to the coffee app!")
def all_chai(request):
  return render(request,'all_chai.html')