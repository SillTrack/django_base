
from django.core.management.base import BaseCommand

from authapp.models import ShopUser
from mainapp.models import ProductCategory
from mainapp.models import Product
import json
import os


JSON_PATH = 'mainapp/jsons'


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), mode='r') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = load_from_json('categories')

        ProductCategory.objects.all().delete()
        for category in categories:
            new_category = ProductCategory(**category)
            new_category.save()

        products = load_from_json('products')

        Product.objects.all().delete()
        for product in products:
            category_name = product['category']
            _category = ProductCategory.objects.get(name=category_name)
            product['category'] = _category
            new_product = Product(**product)
            new_product.save()


        super_user = ShopUser.objects.create_superuser('admin', 'admin@stranger.local', '123', age='30')
        if super_user:
            print('Super user was created')
