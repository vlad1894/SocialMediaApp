from django import forms
from .models import Thought

class ThoughtForm(forms.ModelForm):
    body = forms.CharField(required=True)

    class Meta:
        model=Thought
        exclude=("user", )