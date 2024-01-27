from django.shortcuts import render, redirect
from django.db.models import Count, Sum, Max, OuterRef, Subquery, Prefetch
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .forms import CustomersForm, ContractsForm, OrdersForm, MetricsForm, InstallationsForm
from .models import Customers, Contracts, Orders, Metrics, Installations

# Список форм:
# contracts, orders, clients, installations, metrics.


# Шаблон страницы с формой.

@login_required(login_url='/users/login/')
def create_entity(request, table_data, form_class, template_name, this_page):
    
    register_url = reverse('users:register')
    login_url = reverse('users:login')
    logout_url = reverse('users:logout')
    
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

    context = {
        'table_data': table_data,
        "form": form,
        "this_page": this_page[0],
        "page_label": this_page[1],
        
        'register_url': register_url,
        'login_url': login_url,
        'logout_url': logout_url,
    }
    
    return render(request, template_name, context=context)


def create_customer(request):
    table_data = Customers.objects.annotate(
        num_contracts=Count('contracts'),     # Количество связанных договоров.
        total_amount=Sum('contracts__price')  # Общая сумма договоров.
    )
    return create_entity(request, table_data, CustomersForm, "main_forms/customers.html", ("customers", 'Клиенты'))


def create_contract(request):
    subquery = Installations.objects.filter(contract=OuterRef('contract_number')).order_by('installation_date').values(
        'installation_date')[:1]
    table_data = Contracts.objects.annotate(installation_date=Subquery(subquery))
    return create_entity(request, table_data, ContractsForm, "main_forms/contracts.html", ("contracts", "Договоры"))


def create_order(request):
    table_data = Orders.objects.all()
    return create_entity(request, table_data, OrdersForm, "main_forms/orders.html", ("orders", "Заказы"))


def create_metrics(request):
    table_data = Metrics.objects.all()
    return create_entity(request, table_data, MetricsForm, "main_forms/metrics.html", ("metrics", "Замеры"))


def create_installation(request):
    subquery = Orders.objects.filter(contract=OuterRef('contract')).order_by('square_meters').values(
        'square_meters')[:1]
    table_data = Installations.objects.annotate(square_meters=Subquery(subquery))

    return create_entity(request, table_data, InstallationsForm, "main_forms/installations.html", ("installations", "Монтажи"))


# Cводная таблица
@login_required(login_url='/users/login/')
def final_table(request):
    contracts = Contracts.objects.all()

    table_data = []
    for contract in contracts:
        order = Orders.objects.filter(contract=contract).first()
        installation = Installations.objects.filter(contract=contract).first()

        data = {
            'Номер_договора': contract.contract_number,
            'Стоимость_договора': contract.price,
            'Оплачено': order.payment,
            'Долг': contract.debt,
            'Завод': order.factory,
            'ФИО_клиента': contract.customer.customer_name,
            'Телефон': contract.customer.phone,
            'Дата_доставки_по_договору': contract.delivery_date_by_contract,
            'Доставка_завода': order.delivery_date,
            'Дата_монтажа': installation.installation_date if installation else None,
            'Стоимость_монтажа': installation.total_amount if installation else None,
        }

        table_data.append(data)

    return render(request, 'main_forms/final_table.html', {'data': table_data})
