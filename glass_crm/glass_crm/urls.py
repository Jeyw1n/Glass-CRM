from django.contrib import admin
from django.urls import path

from main_forms import views


urlpatterns = [
    path("contracts", views.contracts),
    path("orders", views.orders),
    path("clients", views.clients),
    path("installations", views.installations),
    path("metrics", views.metrics),
]
