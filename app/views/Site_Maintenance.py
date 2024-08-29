from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def site504(request):
    return render(request,"Site_Maintenance/Site_Maintenance.html")