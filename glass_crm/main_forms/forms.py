from django import forms
from main_forms.models import *
from django.utils.translation import gettext_lazy as _


# Клиенты
class CustomersForm(forms.ModelForm):
    class Meta:
        model = Customers
        fields = ['address', 'customer_name', 'phone']


# Договора
class ContractsForm(forms.ModelForm):
    class Meta:
        model = Contracts
        customer = forms.ModelChoiceField(queryset=Customers.objects.all())
        fields = ['customer', 'contract_number', 'price', 'prepayment', 'debt',
                  'delivery_date', 'montage_date', 'delivery_date_by_contract']
        exclude = ['debt']  # Исключаем поле 'debt' из формы

        labels = {
            "customer": _("Клиент"),
        }

        widgets = {
            'delivery_date': forms.DateInput(attrs={'type': 'date'}),
            'montage_date': forms.DateInput(attrs={'type': 'date'}),
            'delivery_date_by_contract': forms.DateInput(attrs={'type': 'date'}),
        }

        # !!!!!!!!!!!!!!!!!
        # Еще нужно исключить поля 'delivery_date' и 'montage_date'.

    # Высчитываем поле 'debt'.
    def save(self, commit=True):
        instance = super().save(commit=False)  # Вытаскиваем экземпляр без сохранения в БД.
        instance.debt = instance.price - instance.prepayment  # Ставим значения для 'debt'.

        if commit:
            instance.save()
        return instance


# Заказы
class OrdersForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = '__all__'
        widgets = {'delivery_date': forms.DateInput(attrs={'type': 'date'})}


# Замеры
class MetricsForm(forms.ModelForm):
    class Meta:
        model = Metrics
        fields = ['address', 'metrics_date', 'contacts', 'comments']
        widgets = {'metrics_date': forms.DateInput(attrs={'type': 'date'})}
