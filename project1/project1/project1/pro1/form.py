from django import forms
from .models import *

class empform(forms.Modfelform):
    class Meta:
        model=Emp
        fields='__all__'