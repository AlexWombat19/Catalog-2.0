from django import forms
from administrator.models import Class

class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['name']
