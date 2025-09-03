from django.http import HttpResponse
def home(request):
  return HttpResponse("hello world ,you are nice")

def about(request):
  return HttpResponse("you dumbfuck")

def contact(request):
  return("you dumnbfuck")

