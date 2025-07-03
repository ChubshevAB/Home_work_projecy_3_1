from django.shortcuts import render, redirect
from django.http import HttpResponse
from my_app.models import Product, Category
from django.views.generic import ListView, DetailView, View, TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import CreateProduct


class CatalogListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = "my_app/catalog.html"
    context_object_name = "products"
    login_url = reverse_lazy('users:login')

class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'my_app/product_detail.html'
    context_object_name = "product"
    login_url = reverse_lazy('users:login')

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = CreateProduct
    template_name = 'my_app/create_product.html'
    success_url = reverse_lazy('my_app:catalog')
    login_url = reverse_lazy('users:login')

class ContactsView(View):
    template_name = 'my_app/contacts.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        message = request.POST.get("message")
        return HttpResponse(f'Спасибо, {name}! Ваше сообщение получено.')


class StartPageView(TemplateView):
    template_name = 'my_app/base.html'
