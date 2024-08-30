from django.shortcuts import render, redirect
from app.models import Project
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.http import HttpResponseBadRequest
from django.contrib.auth.decorators import login_required


def project(request):
    projects = Project.objects.all().order_by('-created_at')
    return render(request, 'projects/project.html', {'projects': projects})


@login_required(login_url='signin')
def project_list(request):
    projects = Project.objects.all().order_by('-created_at')
    return render(request, 'projects/history.html', {'projects': projects})


@login_required(login_url='signin')
def project_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        url = request.POST.get('url')
        client = request.POST.get('client')

        # Validate the data
        if not name or not description or not start_date:
            return HttpResponseBadRequest("Missing required fields.")

        try:
            url_validator = URLValidator()
            if url:
                url_validator(url)
        except ValidationError:
            return HttpResponseBadRequest("Invalid URL format.")

        # Create and save the project
        Project.objects.create(
            name=name,
            description=description,
            start_date=start_date,
            end_date=end_date,
            url=url,
            client=client        )
        return redirect('dashboard')
    else:
        return render(request, 'projects/project_form.html')
