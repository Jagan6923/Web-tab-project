# views.py in formapp app
from django.shortcuts import render
from django.http import JsonResponse
from .models import Project, DraggableInput
from django.core.exceptions import ObjectDoesNotExist

def index(request):
    return render(request, 'index.html')

def save_project(request):
    if request.method == 'POST':
        project_name = request.POST.get('project_name')
        if Project.objects.filter(name=project_name).exists():
            return JsonResponse({'message': 'Name already used'}, status=400)
        else:
            Project.objects.create(name=project_name)
            return JsonResponse({'message': 'Project name saved successfully!!'})
    return JsonResponse({'message': 'Invalid request'}, status=400)

def validate_project_name(request):
    if request.method == 'POST':
        project_name = request.POST.get('project_name')
        exists = Project.objects.filter(name=project_name).exists()
        return JsonResponse({'exists': exists})
    return JsonResponse({'exists': False})

def save_draggable_input(request):
    if request.method == 'POST':
        try:
            data = request.POST.get('data')
            x_axis = request.POST.get('x_axis')
            y_axis = request.POST.get('y_axis')
            input_id = request.POST.get('input_id')
            
            # Perform any necessary validation here
            
            # Create DraggableInput instance and save to the database
            DraggableInput.objects.create(data=data, x_axis=x_axis, y_axis=y_axis, input_id=input_id)
            
            return JsonResponse({'message': 'Data submitted successfully!'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)
