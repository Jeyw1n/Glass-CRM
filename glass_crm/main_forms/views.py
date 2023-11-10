from django.shortcuts import render, redirect

from main_forms.forms import *
from main_forms.models import *

# Список форм:
# contracts, orders, clients, installations, metrics.


# Шаблон страницы с формой.
def create_entity(request, model, form_class, template_name):
    table_data = model.objects.all()

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


def create_contract(request):
    return create_entity(request, Contracts, ContractsForm, "main_forms/contracts.html")


def create_order(request):
    return create_entity(request, Orders, OrdersForm, "main_forms/orders.html")


def create_customer(request):
    return create_entity(request, Customers, CustomersForm, "main_forms/customers.html")
