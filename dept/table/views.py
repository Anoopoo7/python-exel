from django.shortcuts import render
from .models import Dpt_model
from .download import convert

def index(request):
    if request.method == "POST":
        dept = request.POST['department']
        fac = request.POST['faculty']

        model  =Dpt_model()
        model.department = dept
        model.faculties = fac
        # model.save()
        convert()
        print("success")
        return render(request,'home.html')
        
        
    return render(request,'home.html')
