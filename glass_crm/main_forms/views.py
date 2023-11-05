from django.shortcuts import render, redirect

from main_forms.forms import *
from main_forms.models import *

# Список форм:
# contracts, orders, clients, installations, metrics.


def create_contract(request):
    table_data = Contracts.objects.all()

    # Если это POST запрос.
    if request.method == 'POST':
        form = ContractsForm(request.POST)

        # Была ли нам предоставлена действительная форма?
        if form.is_valid():
            # Обработка данных формы и сохранение в БД.
            task = form.save(commit=False)
            task.save()

            # Редирект на главную (/)
            return redirect('create_contract')

    # Если это GET запрос (или какой-либо ещё).
    else:
        form = ContractsForm()

    context = {'table_data':  table_data,
               "form": form}
    return render(request, "main_forms/contracts.html", context)


def create_order(request):
    table_data = Orders.objects.all()

    if request.method == 'POST':
        form = OrdersForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.save()

            return redirect('create_order')
    else:
        form = OrdersForm()

    context = {'table_data': table_data,
               "form": form}
    return render(request, "main_forms/orders.html", context=context)
