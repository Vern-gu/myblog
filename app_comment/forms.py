from django import forms
from .models import *


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['user_name', 'email', 'url', 'text']