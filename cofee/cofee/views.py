from django.http import HttpResponse

def all_chai(request):
  return render(request,'chai/all_chai.html')



