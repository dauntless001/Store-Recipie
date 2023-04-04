from django import forms
from stave.models import Stave


class StaveForm(forms.ModelForm):
    model = Stave
    fields = ['content']