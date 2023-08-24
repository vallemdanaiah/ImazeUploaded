from django import forms 
from .models import Imaze
class ImazeForms(forms.ModelForm):
    class Meta:
        model=Imaze
        fields="__all__"
        labels = {'photo':''}