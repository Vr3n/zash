from django import forms
from .models import *

# Write your forms here


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Files
        exclude = ['owner']
