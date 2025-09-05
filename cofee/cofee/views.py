from django.http import HttpResponse
from django.shortcuts import render
def home(request):
  return render(request,'index.html')
def all_chai(request):
  return render(request,'chai/all_chai.html')



