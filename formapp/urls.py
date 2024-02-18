from django.urls import path
from .views import index, save_project, validate_project_name, save_draggable_input  # Fix the import

urlpatterns = [
    path('', index, name='index'),  # URL for the index view
    path('save_project/', save_project, name='save_project'),  # URL for saving project
    path('validate_project_name/', validate_project_name, name='validate_project_name'),  # URL for validating project name
    path('save_draggable_input/', save_draggable_input, name='save_draggable_input'),  # Fix the function name here
]
