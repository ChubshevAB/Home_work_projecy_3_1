from django.shortcuts import render
from django.http import HttpResponse
from my_app.models import Product
from django.views.generic import ListView, DetailView, View, TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


class CatalogListView(ListView):
    model = Product
    template_name = "my_app/catalog.html"


class ProductDetailView(DetailView):
    model = Product
    template_name = 'my_app/product_detail.html'


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'description', 'image', 'category', 'price', 'created_at', 'updated_at')
    success_url = reverse_lazy('my_app:catalog')


class ContactsView(View):
    template_name = 'my_app/contacts.html'

    def get(self, request, *args, **kwargs):
        """Обработка GET-запроса (отображение формы)"""
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        """Обработка POST-запроса (отправка формы)"""
        name = request.POST.get("name")
        message = request.POST.get("message")

        return HttpResponse(f'Спасибо, {name}! Ваше сообщение получено.')


class StartPageView(TemplateView):
    template_name = 'my_app/base.html'

# def catalog(request):
#     products = Product.objects.all()
#     context = {
#         "products": products
#     }
#     return render(request, 'my_app/post_list.html', context)


# def contacts(request):
#     if request.method == 'POST':
#         name = request.POST.get("name")
#         message = request.POST.get("message")
#
#         return HttpResponse(f'Спасибо, {name}! Ваше сообщение получено.')
#     return render(request, 'my_app/contacts.html')


# def start_page(request):
#     return render(request, 'my_app/base.html')


# def product_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {
#         "product": product
#     }
#     return render(request, 'my_app/product_detail.html', context)
