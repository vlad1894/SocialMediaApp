from django import forms
from .models import Thought


class ThoughtForm(forms.ModelForm):
    body = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "Share a thought ",
                "class": "textarea is-info is-medium"
            }
        ),
        label="",
    )

    class Meta:
        model = Thought
        exclude = ("profile", )



