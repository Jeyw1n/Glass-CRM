from django import forms
from main_forms.models import Customers, Contracts, Orders, Metrics, Installations, Factories
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
        fields = ['contract_number', 'address', 'customer', 'price',
                  'prepayment', 'delivery_date_by_contract']
        # Исключаем поля 'debt', 'delivery_date' и 'montage_date' из формы.
        exclude = ['debt', 'delivery_date', 'montage_date']
        labels = {
            "customer": _("Клиент"),
        }

        widgets = {
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
    factory = forms.ModelChoiceField(queryset=Factories.objects.all())

    class Meta:
        model = Orders
        contract = forms.ModelChoiceField(queryset=Contracts.objects.all())

        fields = ['contract', 'factory', 'order_number', 'price', 'payment', 'delivery_date', 'square_meters', 'slopes']
        widgets = {'delivery_date': forms.DateInput(attrs={'type': 'date'})}
        labels = {
            "contract": _("Договор"),
            "factory": _("Завод"),
        }


# Замеры
class MetricsForm(forms.ModelForm):
    class Meta:
        model = Metrics
        fields = ['address', 'metrics_date', 'contacts', 'comments']
        widgets = {'metrics_date': forms.DateInput(attrs={'type': 'date'})}


# Монтажи
class InstallationsForm(forms.ModelForm):
    class Meta:
        model = Installations
        contract = forms.ModelChoiceField(queryset=Contracts.objects.all())
        fields = ['contract', 'installation_date', 'square_meters_price',
                  'linear_meters', 'linear_meters_price', 'additional_works']
        exclude = ['total_amount']

        labels = {
            "contract": _("Договор"),
        }
        widgets = {'installation_date': forms.DateInput(attrs={'type': 'date'})}

    def save(self, commit=True):
        instance = super().save(commit=False)  # Вытаскиваем экземпляр без сохранения в БД.

        # Достаем привязанный договор.
        square_meters = Orders.objects.filter(contract=instance.contract).values("square_meters")[0]['square_meters']

        instance.total_amount = (float(square_meters) * instance.square_meters_price +
                                 instance.linear_meters * instance.linear_meters_price +
                                 instance.additional_works)
        if commit:
            instance.save()
        return instance
