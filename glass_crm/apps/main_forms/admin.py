from django.contrib import admin

from .models import Customer, Contract, Order, Metric, Installation, Factory

admin.site.register(Customer)
admin.site.register(Contract)
admin.site.register(Order)
admin.site.register(Metric)
admin.site.register(Installation)
admin.site.register(Factory)

