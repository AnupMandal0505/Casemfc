from django.shortcuts import render
from django.http import HttpResponse

from app.models import Company

def home(request):

    companydata = Company.objects.first()
    context={
        "company":companydata
    }
    return render(request,"home/index.html",context)