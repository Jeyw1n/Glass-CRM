from django.shortcuts import render, redirect

from main_forms.forms import *
from main_forms.models import *

# Список форм:
# contracts, orders, clients, installations, metrics.


def contracts(request):
    table_data = Contracts.objects.all()

    # Если это POST запрос.
    if request.method == 'POST':
        form = AddContract(request.POST)

        # Была ли нам предоставлена действительная форма?
        if form.is_valid():
            # Обработка данных формы и сохранение в БД.
            task = form.save(commit=False)
            task.save()

            # Редирект на главную (/)
            return redirect('/')

    # Если это GET запрос (или какой-либо ещё).
    else:
        form = AddContract()

    context = {'table_data':  table_data,
               "form": form}
    return render(request, f"main_forms/contracts.html", context)
