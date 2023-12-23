from django.contrib import admin
from django.urls import include, path

from main_forms import views


urlpatterns = [
    path("users/", include("account_manager.urls", namespace="users")),
    
    path("", views.create_contract, name="main"),
    path("forms/contracts", views.create_contract, name="create_contract"),
    path("forms/orders", views.create_order, name="create_order"),
    path("forms/customers", views.create_customer, name="create_customer"),
    path("forms/metrics", views.create_metrics, name="create_metrics"),
    path("forms/installations", views.create_installation, name="create_installation"),
]
