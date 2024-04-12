from django.shortcuts import render
from .models import Employee

# Create your views here.
def home(request):
    if request.method=='GET':
        return render (request,'home.html')
    else:
        Employee(
            fname=request.POST.get('fname'),
            lname=request.POST.get('lname'),
            age=request.POST.get('age'),
            mobile=request.POST.get('mobile'),
            ).save()
        return render(request,'result.html')
    
