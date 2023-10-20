from django import forms
from main_forms.models import *


class AddContract(forms.ModelForm):
    class Meta:
        model = Contracts
        fields = '__all__'
        widgets = {
            'delivery_date': forms.DateInput(attrs={'type': 'date'}),
            'montage_date': forms.DateInput(attrs={'type': 'date'}),
            'delivery_date_by_contract': forms.DateInput(attrs={'type': 'date'}),
        }
