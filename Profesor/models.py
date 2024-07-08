from django.db import models
from Elevi.models import Elevi

from administrator.models import Class

class Profesor(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=50, choices=[
        ('mathematics', 'Mathematics'),
        ('chemistry', 'Chemistry'),
        ('history', 'History'),
        # si tot asa
    ])
    class_numbers = models.ManyToManyField(Class, blank=True)

    def __str__(self):
        return self.name

class Grade(models.Model):
    student = models.ForeignKey(Elevi, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    class_number = models.ForeignKey(Class, on_delete=models.CASCADE)
    grade = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.name} - {self.grade}"

class Attendance(models.Model):
    student = models.ForeignKey(Elevi, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    class_number = models.ForeignKey(Class, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    is_absent = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.name} - {'Absent' if self.is_absent else 'Present'}"