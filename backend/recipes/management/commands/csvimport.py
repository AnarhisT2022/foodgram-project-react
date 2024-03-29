import json

from django.core.management.base import BaseCommand
from recipes.models import Ingredient


class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('recipes/data/ingredients.json', encoding='utf-8') as f:
            jsondata = json.load(f)
            if 'measurement_unit' in jsondata[0]:
                for line in jsondata:
                    if not Ingredient.objects.filter(
                       name=line['name'],
                       measurement_unit=line['measurement_unit']).exists():
                        Ingredient.objects.create(
                            name=line['name'],
                            measurement_unit=line['measurement_unit']
                        )
