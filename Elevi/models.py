from django.db import models
from administrator.models import Class  # Import the Class model

class Elevi(models.Model):
    name = models.CharField(max_length=100)
    class_number = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
