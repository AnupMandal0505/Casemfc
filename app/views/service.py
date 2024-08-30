from django.shortcuts import render, redirect
from app.models import Service
from django.http import HttpResponseBadRequest
from django.contrib.auth.decorators import login_required


def service(request):
    service = Service.objects.all().order_by('-created_at')
    return render(request, 'service/service.html', {'service': service})


@login_required(login_url='signin')
def service_list(request):
    service = Service.objects.all().order_by('-created_at')
    return render(request, 'service/history.html', {'service': service})


@login_required(login_url='signin')
def service_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        

        # Validate the data
        if not name or not description:
            return HttpResponseBadRequest("Missing required fields.")

        # Create and save the project
        Service.objects.create(
            name=name,
            description=description       )
        return redirect('dashboard')
    else:
        return render(request, 'service/service_form.html')
