from django import forms
from .models import Measurer, Installer


class MeasurersForm(forms.ModelForm):
    class Meta:
        model = Measurer
        fields = ['name']


class InstallersForm(forms.ModelForm):
    class Meta:
        model = Installer
        fields = ['name']
