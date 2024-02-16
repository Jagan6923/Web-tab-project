# models.py
from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=255, unique=True)

class DraggableInput(models.Model):
    data = models.CharField(max_length=255)  # Add this line
    x_axis = models.FloatField()
    y_axis = models.FloatField()
