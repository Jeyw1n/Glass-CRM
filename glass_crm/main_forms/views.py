from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

from main_forms.forms import *


# contracts, orders, clients, installations, metrics

@csrf_protect
def contracts(request):
    form = AddContract()
    return render(request, f"main_forms/contracts.html", {"form": form})
