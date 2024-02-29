from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Customer, Contract, Order, Metric, Installation, Factory
from ..employees.models import Measurer, Installer


# Клиенты
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['address', 'customer_name', 'phone']


# Договора
class ContractForm(forms.ModelForm):
    measurer = forms.ModelChoiceField(
        queryset=Measurer.objects.all(),
        label=_("Замерщик")
    )

    class Meta:
        model = Contract
        customer = forms.ModelChoiceField(queryset=Customer.objects.all())
        fields = ['contract_number', 'address', 'customer', 'measurer', 'price', 'prepayment',
                  'delivery_date_by_contract']
        # Исключаем поля 'debt', 'delivery_date' и 'montage_date' из формы.
        exclude = ['debt', 'delivery_date', 'montage_date']
        labels = {
            "customer": _("Клиент"),
        }
        widgets = {
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
class OrderForm(forms.ModelForm):
    factory = forms.ModelChoiceField(
        queryset=Factory.objects.all(),
        label=_("Завод")
    )

    class Meta:
        model = Order
        contract = forms.ModelChoiceField(queryset=Contract.objects.all())

        fields = ['contract', 'factory', 'order_number', 'price', 'payment', 'delivery_date', 'square_meters', 'slopes']
        widgets = {
            'delivery_date': forms.DateInput(attrs={'type': 'date'})
        }
        labels = {
            "contract": _("Договор"),
        }


# Замеры
class MetricForm(forms.ModelForm):
    class Meta:
        model = Metric
        measurer = forms.ModelChoiceField(queryset=Measurer.objects.all())

        fields = ['measurer', 'address', 'metrics_date', 'contacts', 'comments']
        labels = {
            "measurer": _("Замерщик"),
        }
        widgets = {
            'metrics_date': forms.DateInput(attrs={'type': 'date'})
        }


# Монтажи
class InstallationForm(forms.ModelForm):
    class Meta:
        model = Installation
        contract = forms.ModelChoiceField(queryset=Contract.objects.all())
        installer = forms.ModelChoiceField(queryset=Installer.objects.all())

        fields = ['contract', 'installer', 'installation_date', 'square_meters_price', 'linear_meters',
                  'linear_meters_price', 'additional_works']
        exclude = ['total_amount']

        labels = {
            "contract": _("Договор"),
            "installer": _("Монтажник"),
        }
        widgets = {
            'installation_date': forms.DateInput(attrs={'type': 'date'})
        }

    def clean(self):
        cleaned_data = super().clean()

        contract = cleaned_data.get('contract')

        if not Order.objects.filter(contract=contract).exists():
            self.add_error('contract', "Заказа на данный договор не существует! Сначала попробуйте создать заказ.")

        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)  # Вытаскиваем экземпляр без сохранения в БД.

        # Проверяем наличие привязанного договора
        square_meters = Order.objects.filter(contract=instance.contract).values("square_meters")[0]['square_meters']

        instance.total_amount = (
                float(square_meters)
                * instance.square_meters_price
                + instance.linear_meters
                * instance.linear_meters_price
                + instance.additional_works
        )

        # Добавляем ошибку к полю contract
        self.add_error('contract',
                       "Заказа на данный договор не существует! Сначала попробуйте создать заказ.")

        if commit:
            instance.save()
        return instance


# Форма добавления завода.
class FactoryForm(forms.ModelForm):
    class Meta:
        model = Factory
        fields = ['factory']
