from django.shortcuts import render
from django.http import HttpResponse



def start_page(request, *args, **kwargs):
    return render(request, 'my_app/start_page.html', {})


def work(request, *args, **kwargs):
    return render(request, 'works/works.html', {})


def shop(request, *args, **kwargs):
    return render(request, 'shop/shop.html', {})


def about(request, *args, **kwargs):
    return render(request, 'about/about.html', {})