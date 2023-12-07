from django.db import models


class Customers(models.Model):
    """ Клиенты """

    id = models.AutoField(primary_key=True, unique=True)

    address = models.CharField(max_length=255, verbose_name='Адрес')                        # Адрес
    customer_name = models.CharField(max_length=255, verbose_name='ФИО клиента')            # ФИО клиента
    phone = models.CharField(max_length=12, verbose_name='Телефон')                         # Телефон

    objects = models.Manager()

    # Возврат имени, чтобы отображать его в выпадающем списке формы.
    def __str__(self):
        return self.customer_name


class Contracts(models.Model):
    """ Договора """

    # Ссылка на модель клиентов.
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)

    contract_number = models.CharField(max_length=255, verbose_name='Номер договора')       # Номер договора.
    address = models.CharField(max_length=255, verbose_name='Адрес')                        # Адрес
    price = models.FloatField(verbose_name='Цена')                                          # Цена.
    prepayment = models.FloatField(verbose_name='Предоплата')                               # Предоплата.
    debt = models.FloatField(verbose_name='Долг')                                           # Долг.
    # delivery_date = models.DateField(verbose_name='Дата доставки')                        # Дата доставки.
    # montage_date = models.DateField(verbose_name='Дата монтажа')                          # Дата монтажа.
    delivery_date_by_contract = models.DateField(verbose_name='Дата доставки по договору')  # Дата доставки по договору.

    objects = models.Manager()

    def __str__(self):
        return self.contract_number


class Orders(models.Model):
    """ Заказы """

    # Ссылка на модель договоров.
    contract = models.ForeignKey(Contracts, on_delete=models.CASCADE)

    factory = models.CharField(max_length=255, verbose_name='Завод')                        # Завод.
    order_number = models.CharField(max_length=255, verbose_name='Номер заказа')            # Номер заказа.
    price = models.FloatField(verbose_name='Стоимость')                                     # Стоимость.
    payment = models.FloatField(verbose_name='Оплата')                                      # Оплата.
    delivery_date = models.DateField(verbose_name='Дата доставки от завода')                # Дата доставки от завода.
    square_meters = models.CharField(max_length=255, verbose_name='Квадратные мерты')                     # м2.
    slopes = models.CharField(max_length=255, verbose_name='Откосы')                        # Откосы.

    objects = models.Manager()


class Installations(models.Model):
    """ Монтажи """

    contract = models.ForeignKey(Contracts, on_delete=models.CASCADE)  # Ссылка на модель договоров.

    installation_date = models.DateField(verbose_name='Дата монтажа')                       # Дата монтажа.
    # square_meters = models.FloatField(max_length=255, verbose_name='Кол-во м2')             # Кол-во м2.
    square_meters_price = models.FloatField(verbose_name='Стоимость квадратных метров')                    # Стоимость м2.
    linear_meters = models.FloatField(max_length=255, verbose_name='Кол-во м/п')            # Кол-во м/п.
    linear_meters_price = models.FloatField(verbose_name='Стоимость м/п')                   # Стоимость м/п.
    additional_works = models.FloatField(verbose_name='Доп. работы')                        # Доп. работы.
    total_amount = models.FloatField(verbose_name='Сумма')                                  # Сумма.

    objects = models.Manager()


class Metrics(models.Model):
    """ Замеры """

    address = models.CharField(max_length=255, verbose_name='Адрес')                        # Адрес.
    metrics_date = models.DateField(verbose_name='Дата замера')                             # Дата замера.
    contacts = models.CharField(max_length=255, verbose_name='Контакты')                    # Контакты.
    comments = models.TextField(verbose_name='Комментарии')                                 # Комментарии.

    objects = models.Manager()


class Factories(models.Model):
    """ Список заводов """

    factory = models.CharField(max_length=255)
    objects = models.Manager()

    def __str__(self):
        return self.factory
