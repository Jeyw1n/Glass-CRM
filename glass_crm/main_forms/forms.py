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
        exclude = ['debt']  # Исключаем поле 'debt' из формы

        # !!!!!!!!!!!!!!!!!
        # Еще нужно исключить поля 'phone', 'delivery_date' и 'montage_date'.

    # Высчитываем поле 'debt'.
    def save(self, commit=True):
        instance = super().save(commit=False)  # Вытаскиваем экземпляр без сохранения в БД.
        instance.debt = instance.price - instance.prepayment  # Ставим значения для 'debt'.

        if commit:
            instance.save()
        return instance
