from django import forms
from .models import Bug

class AddBugForm(forms.ModelForm):
    class Meta: 
        model = Bug
        fields = ('title', 'description')