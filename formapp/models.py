from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
class DraggableInput(models.Model):
    field_id = models.IntegerField()
    data = models.CharField(max_length=255)
    x_axis = models.FloatField()
    y_axis = models.FloatField()

    def __str__(self):
        return f"Field ID: {self.field_id}, Data: {self.data}, Position: ({self.x_axis}, {self.y_axis})"