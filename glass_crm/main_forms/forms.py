from django import forms
from main_forms.models import *


# Клиенты клиенты customers Customers clients Clients.
class CustomersForm(forms.ModelForm):
    class Meta:
        model = Customers
        fields = ['address', 'customer_name', 'phone']


class ContractsForm(forms.ModelForm):
    class Meta:
        model = Contracts
        customer = forms.ModelChoiceField(queryset=Customers.objects.all())
        fields = ['customer', 'contract_number', 'price', 'prepayment', 'debt',
                  'delivery_date', 'montage_date', 'delivery_date_by_contract']
        widgets = {
            'delivery_date': forms.DateInput(attrs={'type': 'date'}),
            'montage_date': forms.DateInput(attrs={'type': 'date'}),
            'delivery_date_by_contract': forms.DateInput(attrs={'type': 'date'}),
        }
        exclude = ['debt']  # Исключаем поле 'debt' из формы

        # !!!!!!!!!!!!!!!!!
        # Еще нужно исключить поля 'delivery_date' и 'montage_date'.

    # Высчитываем поле 'debt'.
    def save(self, commit=True):
        instance = super().save(commit=False)  # Вытаскиваем экземпляр без сохранения в БД.
        instance.debt = instance.price - instance.prepayment  # Ставим значения для 'debt'.

        if commit:
            instance.save()
        return instance


class OrdersForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = '__all__'
        widgets = {'delivery_date': forms.DateInput(attrs={'type': 'date'}), }
