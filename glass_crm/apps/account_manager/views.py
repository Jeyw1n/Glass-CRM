from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

from .forms import LoginUserForm, RegisterUserForm


def login_user(request):
    # Если отправляют данные в форму.
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():  # Проверяем валидность формы.
            cd = form.cleaned_data
            # Аутентифицируем пользователя.
            user = authenticate(request, username=cd['username'],
                                password=cd['password'])
            # Активна ли учетная запись? Если да, авторизуем.
            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('main'))
    else:
        form = LoginUserForm()
    return render(request, 'account_manager/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))


def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return HttpResponseRedirect(reverse('main'))
    else:
        form = RegisterUserForm()
    return render(request, 'account_manager/register.html', {'form': form})
