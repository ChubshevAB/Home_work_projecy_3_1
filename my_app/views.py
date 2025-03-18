from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from my_app.models import Product


def catalog(request):
    products = Product.objects.all()
    context = {
        "products": products
    }
    return render(request, 'my_app/catalog.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        message = request.POST.get("message")

        return HttpResponse(f'Спасибо, {name}! Ваше сообщение получено.')
    return render(request, 'my_app/contacts.html')


def start_page(request):
    return render(request, 'my_app/base.html')


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        "product": product
    }
    return render(request, 'product_detail.html', context)
