import json

from django.core.management.base import BaseCommand
from recipes.models import Ingredient


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("--path", type=str, help="file path")

    def handle(self, *args, **options):
        file_path = options["path"]

        with open(file_path, encoding='utf-8') as f:
            jsondata = json.load(f)
            try:
                Ingredient.objects.bulk_create(
                    [Ingredient(**ingredient) for ingredient in jsondata]
                )
                print(f'{Ingredient.objects.all().count()} '
                      'ингредиентов импортированою.')
            except Exception as error_message:
                raise Exception(error_message)
