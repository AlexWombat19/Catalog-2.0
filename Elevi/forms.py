from django import forms
from Elevi.models import Elevi

class EleviForm(forms.ModelForm):
    class Meta:
        model = Elevi
        fields = ['name', 'class_number']
