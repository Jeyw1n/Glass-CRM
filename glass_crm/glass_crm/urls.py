from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from apps.main_forms import views


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
    path("forms/final_table", views.final_table, name="final_table"),
]
