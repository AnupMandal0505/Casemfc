from django.shortcuts import render, redirect
from app.models import Company



def about(request):
    company = Company.objects.first()
    return render(request, 'home/about.html', {'company': company})
