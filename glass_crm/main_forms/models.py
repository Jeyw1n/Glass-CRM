from django.db import models


# Договора
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


# Заказы
class Orders(models.Model):
    contract_number = models.CharField(max_length=255, verbose_name='Номер договора')       # Номер договора.
    address = models.CharField(max_length=255, verbose_name='Адрес')                        # Адрес.
    factory = models.CharField(max_length=255, verbose_name='Завод')                        # Завод.
    order_number = models.CharField(max_length=255, verbose_name='Номер заказа')            # Номер заказа.
    price = models.IntegerField(verbose_name='Стоимость')                                   # Стоимость.
    # payment = models.IntegerField(verbose_name='Оплата')                                  # Оплата.
    delivery_date = models.DateField(verbose_name='Дата доставки от завода')                # Дата доставки.
    square_meters = models.CharField(max_length=255, verbose_name='м2')                     # м2.
    slopes = models.CharField(max_length=255, verbose_name='Откосы')                        # Откосы.
    objects = models.Manager()


# Клиенты
class Customers(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    address = models.CharField(max_length=255, verbose_name='Адрес')                        # Адрес
    customer = models.CharField(max_length=255, verbose_name='ФИО клиента')                 # ФИО клиента
    phone = models.CharField(max_length=12, verbose_name='Телефон')                         # Телефон
    # contract_count = models.IntegerField(verbose_name='Кол-во договоров')                   # Кол-во договоров
    # contract_cost = models.IntegerField(verbose_name='Стоимость договоров')                 # Стоимость договоров
    objects = models.Manager()


# Монтажи
class Installation(models.Model):
    contract_number = models.CharField(max_length=255, verbose_name='Номер договора')       # Номер договора.
    address = models.CharField(max_length=255, verbose_name='Адрес')                        # Адрес.
    installation_date = models.DateField(verbose_name='Дата монтажа')                       # Дата монтажа.
    square_meters_count = models.CharField(max_length=255, verbose_name='Кол-во м2')        # Кол-во м2.
    slopes = models.CharField(max_length=255, verbose_name='Откосы м/п')                    # Откосы м/п.
    price_per_square_meter = models.IntegerField(verbose_name='Стоимость м2')               # Стоимость м2.
    additional_works = models.TextField(verbose_name='Доп. работы')                         # Доп. работы.
    total_amount = models.IntegerField(verbose_name='Сумма')                                # Сумма.
    objects = models.Manager()


# Замеры
class Measurement(models.Model):
    address = models.CharField(max_length=255, verbose_name='Адрес')               # Адрес.
    measurement_date = models.DateField(verbose_name='Дата замера')                # Дата замера.
    contacts = models.CharField(max_length=255, verbose_name='Контакты')           # Контакты.
    comments = models.TextField(verbose_name='Комментарии')                        # Комментарии.
    objects = models.Manager()
