import os
import requests
from django.views import View
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .asset_requests import main


# Create your views here.

def redirect_request(request):
    return redirect('laptop-request', permanent=True)


@login_required
def laptop_request(request):
    user_input = request.GET.get('input', '')

    result = None

    if user_input:
        input = user_input
        result = main(input)

    return render(request, 'request_page.html', {'result': result})
