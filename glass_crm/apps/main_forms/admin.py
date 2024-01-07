from django.contrib import admin

from apps.main_forms.models import Customers, Contracts, Orders, Metrics, Installations, Factories

admin.site.register(Customers)
admin.site.register(Contracts)
admin.site.register(Orders)
admin.site.register(Metrics)
admin.site.register(Installations)
admin.site.register(Factories)