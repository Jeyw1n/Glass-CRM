from django.contrib import admin

from .models import Customers, Contracts, Orders, Metrics, Installations, Factories, Measurers

admin.site.register(Customers)
admin.site.register(Contracts)
admin.site.register(Orders)
admin.site.register(Metrics)
admin.site.register(Installations)
admin.site.register(Factories)
admin.site.register(Measurers)
