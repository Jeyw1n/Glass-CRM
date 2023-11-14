from django import forms
from main_forms.models import Customers, Contracts, Orders, Metrics
from django.utils.translation import gettext_lazy as _


# Клиенты
class CustomersForm(forms.ModelForm):
    class Meta:
        model = Customers
        fields: list[str] = ['address', 'customer_name', 'phone']


# Договора
class ContractsForm(forms.ModelForm):
    class Meta:
        model = Contracts
        customer = forms.ModelChoiceField(queryset=Customers.objects.all())
        fields: list[str] = ['contract_number', 'address', 'customer', 'price',
                             'prepayment', 'delivery_date_by_contract']
        # Исключаем поля 'debt', 'delivery_date' и 'montage_date' из формы.
        exclude: list[str] = ['debt', 'delivery_date', 'montage_date']
        labels: dict = {
            "customer": _("Клиент"),
        }

        widgets: dict = {
            # 'delivery_date': forms.DateInput(attrs={'type': 'date'}),
            # 'montage_date': forms.DateInput(attrs={'type': 'date'}),
            'delivery_date_by_contract': forms.DateInput(attrs={'type': 'date'}),
        }

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
        contract = forms.ModelChoiceField(queryset=Contracts.objects.all())
        fields = ['contract', 'factory', 'order_number', 'price', 'payment', 'delivery_date', 'square_meters', 'slopes']
        widgets: dict = {'delivery_date': forms.DateInput(attrs={'type': 'date'})}
        labels: dict = {
            "contract": _("Договор"),
        }


# Замеры
class MetricsForm(forms.ModelForm):
    class Meta:
        model = Metrics
        fields: list[str] = ['address', 'metrics_date', 'contacts', 'comments']
        widgets: dict = {'metrics_date': forms.DateInput(attrs={'type': 'date'})}
