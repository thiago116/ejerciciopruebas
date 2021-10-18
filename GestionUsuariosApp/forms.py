from django import forms
from django.forms import fields
from .models import Ambiente


class agregarambiente(forms.ModelForm):
    class Meta:
        model= Ambiente
        fields='__all__'