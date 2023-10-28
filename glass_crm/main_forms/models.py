from django.db import models


class Contracts(models.Model):
    contract_number = models.CharField(max_length=255, verbose_name='Номер договора')       # Номер договора.
    address = models.CharField(max_length=255, verbose_name='Адрес')                        # Адрес.
    customer = models.CharField(max_length=255, verbose_name='ФИО клиента')                 # ФИО клиента.
    phone = models.CharField(max_length=255, verbose_name='Номер телефона')                 # Номер телефона.
    price = models.IntegerField(verbose_name='Цена')                                        # Цена.
    prepayment = models.IntegerField(verbose_name='Предоплата')                             # Предоплата.
    debt = models.IntegerField(verbose_name='Долг')                                         # Долг.
    delivery_date = models.DateField(verbose_name='Дата доставки')                          # Дата доставки.
    montage_date = models.DateField(verbose_name='Дата монтажа')                            # Дата монтажа.
    delivery_date_by_contract = models.DateField(verbose_name='Дата доставки по договору')  # Дата доставки по договору.

    objects = models.Manager()


class Orders(models.Model):
    contract_number = models.CharField(max_length=255, verbose_name='Номер договора')       # Номер договора.
    address = models.CharField(max_length=255, verbose_name='Адрес')                        # Адрес.
    factory = models.CharField(max_length=255, verbose_name='Завод')                        # Завод.
    order_number = models.CharField(max_length=255, verbose_name='Номер заказа')            # Номер заказа.
    price = models.IntegerField(verbose_name='Стоимость')                                   # Стоимость.
    delivery_date = models.DateField(verbose_name='Дата доставки')                          # Дата доставки.
    m2 = models.CharField(max_length=255, verbose_name='м2')                                # м2.
    slopes = models.CharField(max_length=255, verbose_name='Откосы')                        # Откосы.


