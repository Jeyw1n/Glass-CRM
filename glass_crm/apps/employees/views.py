from django.contrib.admin.views.decorators import staff_member_required
from django.apps import apps
from django.shortcuts import redirect

import utils.SimplifiedViews as sv

from .models import Measurer, Installer
from .forms import MeasurersForm, InstallersForm


# Утилита для создания представлений форм с таблицами.
APP_PATH = "employees/"


def create_measurer(request):

    model_data = Measurer.objects.all()
    form_class = MeasurersForm
    this_page = "create_measurer"
    page_label = "Замерщики"
    this_model = "Measurer"

    return sv.create_entity(request, model_data, form_class, this_page, page_label, this_model, APP_PATH)


def create_installer(request):

    model_data = Installer.objects.all()
    form_class = InstallersForm
    this_page = "create_installer"
    page_label = "Монтажники"
    this_model = "Installer"

    return sv.create_entity(request, model_data, form_class, this_page, page_label, this_model, APP_PATH)


@staff_member_required
def delete_empl(request, this_model, row_id, this_page):
    """ Отвечает за удаление записей в таблице. """

    model = apps.get_model(app_label="employees", model_name=this_model)
    row = model.objects.get(id=row_id)
    row.delete()
    return redirect(this_page)
