from django.core.management.base import BaseCommand
from my_app.models import Product, Category


class Command(BaseCommand):
    help = 'Add products for database'

    def handle(self, *args, **options):

        all_categories = Category.objects.all()
        all_categories.delete()

        category, _ = Category.objects.get_or_create(name='Бытовая техника', description='Микроволновые печи, тостеры и т.д.')

        products = [
            {'name': 'Микроволновка Dexp', 'category': category, 'price': 5000},
            {'name': 'Посудомойка', 'category': category, 'price': 25000},
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Продукт успешно добавлен: {product.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Данный товар уже существует: {product.name}'))
