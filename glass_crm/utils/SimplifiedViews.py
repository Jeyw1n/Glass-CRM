from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import render


LOGIN_PATH = "/users/login/"

REG_URL = "users:register"
LOGIN_URL = "users:login"
LOGOUT_URL = "users:logout"


@login_required(login_url=LOGIN_PATH)
def create_entity(request, model_data, form_class, this_page, page_label, this_model, app_path):
    """ Универсальный шаблон представления форм и таблиц. """

    # Если это POST запрос.
    if request.method == "POST":
        form = form_class(request.POST)
        # Была ли нам предоставлена действительная форма?
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
    # Если это GET запрос (или какой-либо ещё).
    else:
        form = form_class

    context = {
        'model_data': model_data,
        # Название файла шаблона должно быть равным "name" в urls.py!!!
        "this_page": this_page,
        "page_label": page_label,
        "form": form,
        "this_model": this_model,
        "register_url": reverse(REG_URL),
        "login_url": reverse(LOGIN_URL),
        "logout_url": reverse(LOGOUT_URL),
    }

    return render(request, f"{app_path + this_page}.html", context=context)
