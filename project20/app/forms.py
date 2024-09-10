from django import forms
from .models import *


class School_Form(forms.ModelForm):
    class Meta:
        model=School
        fields = '__all__'