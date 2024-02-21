from django.contrib import admin

from .models import Measurer, Installer

admin.site.register(Measurer)
admin.site.register(Installer)