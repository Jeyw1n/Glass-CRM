from django.shortcuts import render
from django.urls import reverse
from .models import Measurer, Installer
from .forms import MeasurersForm, InstallersForm


def create_entity(request, table_data, form_class, template_name, this_page):
    register_url = reverse('users:register')
    login_url = reverse('users:login')
    logout_url = reverse('users:logout')

    # Если это POST запрос.
    if request.method == 'POST':
        form = form_class(request.POST)

        # Была ли нам предоставлена действительная форма?
        if form.is_valid():
            task = form.save(commit=False)
            task.save()

    # Если это GET запрос (или какой-либо ещё).
    else:
        form = form_class

    context = {
        'table_data': table_data,
        "form": form,
        "this_page": this_page[0],
        "page_label": this_page[1],

        'register_url': register_url,
        'login_url': login_url,
        'logout_url': logout_url,
    }

    return render(request, template_name, context=context)


def create_measurer(request):
    table_data = Measurer.objects.all()
    return create_entity(
        request,
        table_data,
        MeasurersForm,
        "employees/measurers.html",
        ("measurers", 'Замерщики')
    )


def create_installer(request):
    table_data = Installer.objects.all()
    return create_entity(
        request,
        table_data,
        InstallersForm,
        "employees/installers.html",
        ("installers", 'Монтажники')
    )