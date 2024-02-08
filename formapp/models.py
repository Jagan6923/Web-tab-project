from django.db import models

class Form(models.Model):
    form_id = models.CharField(max_length=100, unique=True)
    form_input_field_data = models.TextField(default="")
    redirect_path_input_field = models.CharField(max_length=255)

    def __str__(self):
        return self.form_id

class Field(models.Model):
    form = models.ForeignKey(Form, related_name='fields', on_delete=models.CASCADE)
    field_id = models.CharField(max_length=100, unique=True)
    field_input_data = models.TextField()
    selection_box_data = models.TextField()
    is_required = models.BooleanField(default=False)
    is_checked = models.BooleanField(default=False)

    def __str__(self):
        return self.field_id
