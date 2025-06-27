from django.forms import ModelForm

from my_app.models import Product

from django.core.exceptions import ValidationError


forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

class CreateProduct(ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'category', 'image')

    def __init__(self, *args, **kwargs):
        super(CreateProduct, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите наименование товара'
        })

        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите описание товара'
        })

        self.fields['price'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Укажите стоимость товара'
        })

        self.fields['category'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Выберете категорию'
        })

        self.fields['image'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Загрузите фото товара'
        })

    def clean_price(self):
        price = self.cleaned_data.get('price')

        if int(price) <= 0:
            raise ValidationError('Стоимость товара должна быть меньше нуля!')

        return price

    def clean(self):
        cleaned_data = super().clean()
        description = cleaned_data.get('description', '').lower()
        name = cleaned_data.get('name', '').lower()

        # Проверка описания
        found_word = next((word for word in forbidden_words if word in description), None)
        if found_word:
            self.add_error('description', f'В описании товара не может использоваться слово "{found_word}"')
            return cleaned_data  # Прекращаем проверку после первого найденного слова

        # Проверка названия
        found_word = next((word for word in forbidden_words if word in name), None)
        if found_word:
            self.add_error('name', f'В наименовании товара не может использоваться слово "{found_word}"')

        return cleaned_data
