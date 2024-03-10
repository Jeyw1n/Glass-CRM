from django.shortcuts import render, redirect
from django.db.models import Count, Sum, Max, OuterRef, Subquery, Prefetch
from django.contrib.admin.views.decorators import staff_member_required
from django.apps import apps

import utils.SimplifiedViews as sv

from .forms import CustomerForm, ContractForm, OrderForm, MetricForm, InstallationForm, FactoryForm
from .models import Customer, Contract, Order, Metric, Installation, Factory


APP_PATH = "main_forms/tables/"


def create_customer(request):

    model_data = Customer.objects.annotate(
        num_contracts=Count('contract'),  # Количество связанных договоров.
        total_amount=Sum('contract__price')  # Общая сумма договоров.
    )
    form_class = CustomerForm
    this_page = "create_customer"
    page_label = "Клиенты"
    this_model = "Customer"

    return sv.create_entity(request, model_data, form_class, this_page, page_label, this_model, APP_PATH)


def create_contract(request):

    subquery = Installation.objects.filter(contract=OuterRef('contract_number')).order_by('installation_date').values(
        'installation_date')[:1]
    model_data = Contract.objects.annotate(installation_date=Subquery(subquery))
    form_class = ContractForm
    this_page = "create_contract"
    page_label = "Договоры"
    this_model = "Contract"

    return sv.create_entity(request, model_data, form_class, this_page, page_label, this_model, APP_PATH)


def create_order(request):

    model_data = Order.objects.all()
    form_class = OrderForm
    this_page = "create_order"
    page_label = "Заказы"
    this_model = "Order"

    return sv.create_entity(request, model_data, form_class, this_page, page_label, this_model, APP_PATH)


def create_metrics(request):

    model_data = Metric.objects.all()
    form_class = MetricForm
    this_page = "create_metrics"
    page_label = "Замеры"
    this_model = "Metric"

    return sv.create_entity(request, model_data, form_class, this_page, page_label, this_model, APP_PATH)


def create_installation(request):

    subquery = Order.objects.filter(contract=OuterRef('contract')).order_by('square_meters').values('square_meters')[:1]
    model_data = Installation.objects.annotate(square_meters=Subquery(subquery))
    form_class = InstallationForm
    this_page = "create_installation"
    page_label = "Монтажи"
    this_model = "Installation"

    return sv.create_entity(request, model_data, form_class, this_page, page_label, this_model, APP_PATH)


def add_factory(request):

    model_data = Factory.objects.all()    # Все объекты модели.
    form_class = FactoryForm              # Класс формы.
    this_page = "add_factory"             # Используется для добавления стилей меню и перенаправления.
    page_label = "Заводы"                 # Заголовок страницы.
    this_model = "Factory"                # Название модели.

    return sv.create_entity(request, model_data, form_class, this_page, page_label, this_model, APP_PATH)


@staff_member_required
def delete_item(request, this_model, row_id, this_page):
    """ Отвечает за удаление записей в таблице. """

    model = apps.get_model(app_label="main_forms", model_name=this_model)
    row = model.objects.get(id=row_id)
    row.delete()
    return redirect(this_page)  # Перенаправьте на страницу, которую вы передали в шаблоне.
