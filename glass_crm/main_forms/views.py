from django.shortcuts import render, redirect
from django.db.models import Count, Sum, Max

from main_forms.forms import CustomersForm, ContractsForm, OrdersForm, MetricsForm, InstallationsForm
from main_forms.models import Customers, Contracts, Orders, Metrics, Installations

# Список форм:
# contracts, orders, clients, installations, metrics.


# Шаблон страницы с формой.
def create_entity(request, table_data, form_class, template_name):
    # Если это POST запрос.
    if request.method == 'POST':
        form = form_class(request.POST)

        # Была ли нам предоставлена действительная форма?
        if form.is_valid():
            task = form.save(commit=False)
            task.save()

    # Если это GET запрос (или какой-либо ещё).
    else:
        form = form_class

    context = {'table_data': table_data, "form": form}
    return render(request, template_name, context=context)


def create_customer(request):
    table_data = Customers.objects.annotate(
        num_contracts=Count('contracts'),     # Количество связанных договоров.
        total_amount=Sum('contracts__price')  # Общая сумма договоров.
    )
    return create_entity(request, table_data, CustomersForm, "main_forms/customers.html")


def create_contract(request):
    contracts_with_installation_dates = Contracts.objects.annotate(
        installation_date=Max('installations__installation_date')
    )

    # Теперь у нас есть информация о договорах с аннотированным полем 'installation_date'
    for contract in contracts_with_installation_dates:
        print(f"Договор: {contract.contract_number}, Дата установки: {contract.installation_date}")

    table_data = Contracts.objects.all()
    return create_entity(request, table_data, ContractsForm, "main_forms/contracts.html")


def create_order(request):
    table_data = Orders.objects.all()
    return create_entity(request, table_data, OrdersForm, "main_forms/orders.html")


def create_metrics(request):
    table_data = Metrics.objects.all()
    return create_entity(request, table_data, MetricsForm, "main_forms/metrics.html")


def create_installation(request):
    table_data = Installations.objects.all()
    return create_entity(request, table_data, InstallationsForm, "main_forms/installations.html")
