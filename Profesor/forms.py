from django import forms
from Profesor.models import Profesor, Grade, Attendance


class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['name', 'subject', 'class_numbers']
        widgets = {
            'class_numbers': forms.CheckboxSelectMultiple,
        }

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['student', 'class_number', 'grade']

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['student', 'class_number', 'is_absent']