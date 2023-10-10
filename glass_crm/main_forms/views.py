from django.shortcuts import render


# Contracts, orders, clients, installations, metrics
def contracts(request):
    return render(request, "main_forms/index.html", 'contracts')


def orders(request):
    return render(request, "main_forms/index.html", 'orders')


def clients(request):
    return render(request, "main_forms/index.html", 'clients')


def installations(request):
    return render(request, "main_forms/index.html", 'installations')


def metrics(request):
    return render(request, "main_forms/index.html", 'metrics')
