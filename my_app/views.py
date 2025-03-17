from django.shortcuts import render
from django.http import HttpResponse


def main_page(request):
    return render(request, 'my_app/main_page.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        message = request.POST.get("message")

        return HttpResponse(f'Спасибо, {name}! Ваше сообщение получено.')
    return render(request, 'my_app/contacts.html')


def catalog(request):
    return render(request, 'my_app/catalog.html')


def start_page(request):
    return render(request, 'my_app/base.html')
