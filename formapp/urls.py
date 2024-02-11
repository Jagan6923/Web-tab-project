# urls.py in formapp app
from django.urls import path
from .views import index, save_project  # Make sure to import the index view

urlpatterns = [
    path('', index, name='index'),  # Ensure the index view is included in urlpatterns
    path('save_project/', save_project, name='save_project'),
]
