from django.shortcuts import render
from ..main_forms.models import Customers, Contracts, Orders, Metrics, Installations


# Cводная таблица
# @login_required(login_url='/users/login/')
def pivot_table_view(request):
    contracts = Contracts.objects.all()
    table_data: list = []

    for c in contracts:

        order = Orders.objects.filter(contract=c.id).first()
        ini = Installations.objects.filter(contract=c.id).first()
        # metric = Metrics.objects.filter(contract=c.id).first()

        data: dict = {
            "contract_number": c.contract_number,                       # Номер договора
            "price": c.price,                                           # Стоимость договора
            "prepayment": c.prepayment,                                 # Оплачено
            "debt": c.debt,                                             # Долг
            "factory":  order.factory if order else None,               # Завод
            "measurer": c.measurer,                                     # Замерщик
            "address": c.address,                                       # адрес объекта
            "customer_name": c.customer.customer_name,                  # Фио клиента
            "phone": c.customer.phone,                                  # Телефон
            "delivery_date_by_contract": c.delivery_date_by_contract,   # Дата
            "delivery_date": order.delivery_date if order else None,    # Доставка завода
            "ini_date": ini.installation_date if ini else None,         # Дата монтажа
            # Бригада
            "total_amount": ini.total_amount if ini else None           # Стоимость монтажа
            # Заводской номер заказа
            # Стоимость от завода
            # ЗП замерщика
            # Себестоимость
            # Прибыль
            # %
        }

        table_data.append(data)

    print(table_data)
    context: dict = {
        'table_data': table_data,
        'this_page': 'pivot_table',
        'page_label': 'Сводная таблица',
    }
    return render(request, 'pivot_table/index.html', context=context)
