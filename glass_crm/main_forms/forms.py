from django import forms
from django.forms import widgets
from main_forms.models import *


class AddContract(forms.ModelForm):
    class Meta:
        model = Contracts
        fields = '__all__'
        widgets = {
            'delivery_date': widgets.SelectDateWidget(),
            'montage_date': widgets.SelectDateWidget(),
            'delivery_date_by_contract': widgets.SelectDateWidget(),
        }