from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseForbidden
from my_app.models import Product, Category
from django.views.generic import ListView, DetailView, View, TemplateView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import CreateProduct
from .services import get_products_by_category
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.core.cache import cache


class ChangeProduct(LoginRequiredMixin, View):
    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)

        if 'unpublish' in request.POST:
            if not request.user.has_perm('my_app.can_unpublish_product'):
                return HttpResponseForbidden('У вас нет прав для отмены публикации')
            product.is_published = False
            product.save()
            messages.success(request, 'Публикация товара отменена!')

        elif 'delete' in request.POST:
            if not request.user.has_perm('my_app.can_delete_product'):
                return HttpResponseForbidden('У вас нет прав для удаления товара')
            product.delete()
            messages.success(request, 'Товар успешно удален!')

        return redirect('my_app:catalog')

class CatalogListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = "my_app/catalog.html"
    context_object_name = "products"
    login_url = reverse_lazy('users:login')

    def get_queryset(self):
        queryset = cache.get('products_queryset')

        if not queryset:
            queryset = super().get_queryset()
            cache.set('products_queryset', queryset, 900)
        return queryset


@method_decorator(cache_page(900), name='dispatch')
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

    def form_valid(self, form):
        form.instance.owner = self.request.user
        messages.success(self.request, 'Товар успешно создан!')
        return super().form_valid(form)


class StartPageView(TemplateView):
    template_name = 'my_app/base.html'


class ProductUnpublishView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    fields = ['is_published']
    template_name = 'my_app/product_unpublish.html'
    success_url = reverse_lazy('my_app:catalog')
    permission_required = 'my_app.can_unpublish_product'
    login_url = reverse_lazy('users:login')

    def form_valid(self, form):
        form.instance.is_published = False
        messages.success(self.request, 'Публикация товара отменена!')
        return super().form_valid(form)

class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = 'my_app/product_delete.html'
    success_url = reverse_lazy('my_app:catalog')
    permission_required = 'my_app.can_delete_product'
    login_url = reverse_lazy('users:login')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Товар успешно удален!')
        return super().delete(request, *args, **kwargs)


class ProductPublishView(LoginRequiredMixin, UpdateView):
    model = Product
    fields = ['is_published']
    template_name = 'my_app/product_publish.html'
    success_url = reverse_lazy('my_app:catalog')

    def form_valid(self, form):
        form.instance.is_published = True
        messages.success(self.request, 'Товар успешно опубликован!')
        return super().form_valid(form)


class ProductsByCategoryView(LoginRequiredMixin, ListView):
    template_name = 'my_app/products_by_category.html'
    context_object_name = 'products'
    login_url = reverse_lazy('users:login')

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return get_products_by_category(category_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = get_object_or_404(Category, id=self.kwargs['category_id'])
        return context


class CategoriesListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'my_app/categories_list.html'
    context_object_name = 'categories'
    login_url = reverse_lazy('users:login')
