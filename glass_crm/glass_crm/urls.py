from django.contrib import admin
from django.urls import path

from main_forms import views


urlpatterns = [
    path("", views.contracts, name="main"),
    path("forms/contracts", views.contracts),
]
