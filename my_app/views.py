from django.shortcuts import render
from django.http import HttpResponse



def start_page(request, *args, **kwargs):
    return render(request, 'my_app/start_page.html', {})