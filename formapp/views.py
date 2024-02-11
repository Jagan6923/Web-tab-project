# views.py in formapp app
from django.shortcuts import render
from django.http import JsonResponse
from .models import Project

def index(request):
    return render(request, 'index.html')

def save_project(request):
    if request.method == 'POST':
        project_name = request.POST.get('project_name')
        if Project.objects.filter(name=project_name).exists():
            return JsonResponse({'message': 'Name already used'}, status=400)
        else:
            Project.objects.create(name=project_name)
            return JsonResponse({'message': 'Project name saved successfully'})
    return JsonResponse({'message': 'Invalid request'}, status=400)

def validate_project_name(request):
    if request.method == 'POST':
        project_name = request.POST.get('project_name')
        exists = Project.objects.filter(name=project_name).exists()
        return JsonResponse({'exists': exists})
    return JsonResponse({'exists': False})
