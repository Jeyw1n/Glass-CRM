from django.contrib import admin

from .models import Customers, Contracts, Orders, Metrics, Installations, Factories

admin.site.register(Customers)
admin.site.register(Contracts)
admin.site.register(Orders)
admin.site.register(Metrics)
admin.site.register(Installations)
admin.site.register(Factories)
