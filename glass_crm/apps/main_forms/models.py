from django.db import models
from ..employees.models import Measurer, Installer


class Customer(models.Model):
    """ Клиенты """

    id = models.AutoField(primary_key=True, unique=True)

    address = models.CharField(max_length=255, verbose_name='Адрес')                        # Адрес
    customer_name = models.CharField(max_length=255, verbose_name='ФИО клиента')            # ФИО клиента
    phone = models.CharField(max_length=12, verbose_name='Телефон')                         # Телефон

    objects = models.Manager()

    # Возврат имени, чтобы отображать его в выпадающем списке формы, например.
    def __str__(self):
        return self.customer_name


class Contract(models.Model):
    """ Договора """

    # Ссылка на модель клиентов.
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    # Поле замерщика - обычное текстовое поле. Связи нет, чтобы не удалять заказ в случае удаления замерщика.
    measurer = models.CharField(max_length=255, verbose_name='Замерщик')

    contract_number = models.CharField(max_length=255, verbose_name='Номер договора')       # Номер договора.
    address = models.CharField(max_length=255, verbose_name='Адрес')                        # Адрес
    price = models.FloatField(verbose_name='Цена')                                          # Цена.
    prepayment = models.FloatField(verbose_name='Предоплата')                               # Предоплата.
    debt = models.FloatField(verbose_name='Долг')                                           # Долг.
    delivery_date_by_contract = models.DateField(verbose_name='Дата доставки по договору')  # Дата доставки по договору.

    objects = models.Manager()

    def __str__(self):
        return self.contract_number


class Order(models.Model):
    """ Заказы """

    # Ссылка на модель договоров.
    contract = models.OneToOneField(Contract, on_delete=models.CASCADE, related_name='order')

    factory = models.CharField(max_length=255, verbose_name='Завод')                        # Завод.
    order_number = models.CharField(max_length=255, verbose_name='Номер заказа')            # Номер заказа.
    price = models.FloatField(verbose_name='Стоимость заказа')                              # Стоимость заказа.
    payment = models.FloatField(verbose_name='Оплата')                                      # Оплата.
    delivery_date = models.DateField(verbose_name='Дата доставки от завода')                # Дата доставки от завода.
    square_meters = models.CharField(max_length=255, verbose_name='Квадратные мерты')       # м2.
    slopes = models.CharField(max_length=255, verbose_name='Откосы')                        # Откосы.

    objects = models.Manager()


class Installation(models.Model):
    """
    Монтажи:

    Одна модель договора связывается ТОЛЬКО с одним "монтажом".
    Если контракт будет удалён, то и данный монтаж автоматически удалится,
    так-же, если монтажник будет удалён, то и текущая запись будет так-же удалена.
    """

    # Ссылка на модель договоров.
    contract = models.OneToOneField(Contract, on_delete=models.CASCADE, related_name='installation')
    # Поле монтажника со связью.
    installer = models.ForeignKey(Installer, on_delete=models.CASCADE, related_name='installer')

    installation_date = models.DateField(verbose_name='Дата монтажа')                       # Дата монтажа.
    square_meters_price = models.FloatField(verbose_name='Стоимость квадратных метров')     # Стоимость м2.
    linear_meters = models.FloatField(max_length=255, verbose_name='Кол-во м/п')            # Кол-во м/п.
    linear_meters_price = models.FloatField(verbose_name='Стоимость м/п')                   # Стоимость м/п.
    additional_works = models.FloatField(verbose_name='Доп. работы')                        # Доп. работы.
    total_amount = models.FloatField(verbose_name='Сумма')                                  # Сумма.

    objects = models.Manager()


class Metric(models.Model):
    """
    Замеры:

    Если замерщик будет удалён, то и текущая запись будет так-же удалена.
    """
    # Поле замерщика со связью.
    measurer = models.ForeignKey(Measurer, on_delete=models.CASCADE, related_name='measurer')

    address = models.CharField(max_length=255, verbose_name='Адрес')                        # Адрес.
    metrics_date = models.DateField(verbose_name='Дата замера')                             # Дата замера.
    contacts = models.CharField(max_length=255, verbose_name='Контакты')                    # Контакты.
    comments = models.TextField(verbose_name='Комментарии')                                 # Комментарии.

    objects = models.Manager()


class Factory(models.Model):
    """ Список заводов """

    factory = models.CharField(max_length=255, verbose_name='Завод')

    objects = models.Manager()

    def __str__(self):
        return self.factory
