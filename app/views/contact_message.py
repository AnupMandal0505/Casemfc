from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from app.models import ContactMessage
@login_required(login_url='signin')
def new_message(request):
    # Retrieve all ContactMessage records
    data = ContactMessage.objects.filter(status='Pending')

    context = {
        "data": data
    }
    return render(request,"dashboard/new_message.html",context)


@login_required(login_url='signin')
def history(request):
    # Retrieve all ContactMessage records
    data = ContactMessage.objects.all()

    context = {
        "data": data
    }

    return render(request, "dashboard/history.html", context)