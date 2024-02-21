from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from apps.main_forms import views
from apps.pivot_table.views import pivot_table_view
from apps.employees.views import create_measurer, create_installer

urlpatterns = [
    path("admin/", admin.site.urls),
    
    # Маршруты приложения "Account manager".
    path("users/", include("apps.account_manager.urls", namespace="users")),
    
    path("", views.create_contract, name="main"),
    path("forms/contracts", views.create_contract, name="create_contract"),
    path("forms/orders", views.create_order, name="create_order"),
    path("forms/customers", views.create_customer, name="create_customer"),
    path("forms/metrics", views.create_metrics, name="create_metrics"),
    path("forms/installations", views.create_installation, name="create_installation"),
    path("forms/pivot_table", pivot_table_view, name="pivot_table"),

    path("forms/measurers", create_measurer, name="create_measurer"),
    path("forms/installers", create_installer, name="create_installer"),
]
