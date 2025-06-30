from django.shortcuts import render, redirect
from django.http import HttpResponse
from my_app.models import Product, Category
from django.views.generic import ListView, DetailView, View, TemplateView, CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import CreateProduct  # Импортируем вашу форму


class CatalogListView(ListView):
    model = Product
    template_name = "my_app/catalog.html"
    context_object_name = "products"


class ProductDetailView(DetailView):
    model = Product
    template_name = 'my_app/product_detail.html'
    context_object_name = "product"

class ProductCreateView(CreateView):
    model = Product
    form_class = CreateProduct
    template_name = 'my_app/create_product.html'
    success_url = reverse_lazy('my_app:catalog')

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


# from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from my_app.models import Product, Category
# from django.views.generic import ListView, DetailView, View, TemplateView
# from django.views.generic.edit import CreateView
# from django.urls import reverse_lazy
# from django.contrib import messages
#
#
# def create_product(request):
#     if request.method == 'POST':
#
#         name = request.POST.get('name')
#         description = request.POST.get('description')
#         price = request.POST.get('price')
#         category_id = request.POST.get('category')
#         image = request.FILES.get('image')
#
#         try:
#             # Создаем товар
#             category = Category.objects.get(id=category_id)
#             product = Product.objects.create(
#                 name=name,
#                 description=description,
#                 price=price,
#                 category=category,
#                 image=image
#             )
#             messages.success(request, 'Товар успешно добавлен!')
#             return redirect('my_app:product_detail', pk=product.id)
#         except Exception as e:
#             messages.error(request, f'Ошибка при создании товара: {e}')
#
#     categories = Category.objects.all()
#     return render(request, 'my_app/create_product.html', {'categories': categories})
#
#
# class CatalogListView(ListView):
#     model = Product
#     template_name = "my_app/catalog.html"
#
#
# class ProductDetailView(DetailView):
#     model = Product
#     template_name = 'my_app/product_detail.html'
#
#
# class ProductCreateView(CreateView):
#     model = Product
#     fields = ('name', 'description', 'image', 'category', 'price', 'created_at', 'updated_at')
#     success_url = reverse_lazy('my_app:catalog')
#
#
# class ContactsView(View):
#     template_name = 'my_app/contacts.html'
#
#     def get(self, request, *args, **kwargs):
#         """Обработка GET-запроса (отображение формы)"""
#         return render(request, self.template_name)
#
#     def post(self, request, *args, **kwargs):
#         """Обработка POST-запроса (отправка формы)"""
#         name = request.POST.get("name")
#         message = request.POST.get("message")
#
#         return HttpResponse(f'Спасибо, {name}! Ваше сообщение получено.')
#
#
# class StartPageView(TemplateView):
#     template_name = 'my_app/base.html'

