from django import forms
from base.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['display_name', 'image', 'bio']