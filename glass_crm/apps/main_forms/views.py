from django.shortcuts import render, redirect
from django.db.models import Count, Sum, Max, OuterRef, Subquery, Prefetch
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse
from django.apps import apps

from .forms import CustomerForm, ContractForm, OrderForm, MetricForm, InstallationForm
from .models import Customer, Contract, Order, Metric, Installation

# Список форм:
# contracts, orders, clients, installations, metrics.


# Шаблон страницы с формой.

# @login_required(login_url='/users/login/')
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
    table_data = Customer.objects.annotate(
        num_contracts=Count('contract'),     # Количество связанных договоров.
        total_amount=Sum('contract__price')  # Общая сумма договоров.
    )
    return create_entity(request, table_data, CustomerForm, "main_forms/customers.html", ("customers", 'Клиенты'))


def create_contract(request):
    subquery = Installation.objects.filter(contract=OuterRef('contract_number')).order_by('installation_date').values(
        'installation_date')[:1]
    table_data = Contract.objects.annotate(installation_date=Subquery(subquery))
    return create_entity(request, table_data, ContractForm, "main_forms/contracts.html", ("contracts", "Договоры"))


def create_order(request):
    table_data = Order.objects.all()
    return create_entity(request, table_data, OrderForm, "main_forms/orders.html", ("orders", "Заказы"))


def create_metrics(request):
    table_data = Metric.objects.all()
    return create_entity(request, table_data, MetricForm, "main_forms/metrics.html", ("metrics", "Замеры"))


def create_installation(request):
    subquery = Order.objects.filter(contract=OuterRef('contract')).order_by('square_meters').values(
        'square_meters')[:1]
    table_data = Installation.objects.annotate(square_meters=Subquery(subquery))

    return create_entity(request, table_data, InstallationForm, "main_forms/installations.html", ("installations", "Монтажи"))


# Удаление записи в таблице.
@staff_member_required
def delete_item(request, model_name, row_id, redirect_name):
    model = apps.get_model(app_label='main_forms', model_name=model_name)
    row = model.objects.get(id=row_id)
    row.delete()
    return redirect(redirect_name)  # перенаправьте на страницу, которую вы передали в шаблоне
