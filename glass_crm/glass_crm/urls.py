from django.contrib import admin
from django.urls import path

from main_forms import views


urlpatterns = [
    path("", views.create_contract, name="main"),
    path("forms/contracts", views.create_contract, name="create_contract"),
    path("forms/orders", views.create_order, name="create_order"),
    path("forms/customers", views.create_customer, name="create_customer"),
]
