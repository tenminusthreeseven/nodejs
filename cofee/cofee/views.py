from django.http import HttpResponse
from django.shortcuts import render
def home(request):
  return render(request,'index.html')
def home(request):
  return HttpResponse("hello world ,you are nice")

def about(request):
  return HttpResponse("you dumbfuck")

def contact(request):
  return("you dumnbfuck")


