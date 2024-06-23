from django import forms
from .models import Project

class CreateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ()
        