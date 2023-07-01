from django.contrib import admin

from .models import Favorite, Ingredient, Recipe, RecipeTag, ShoppingCart, Tag


class IngredientsInLine(admin.TabularInline):
    model = Recipe.ingredients.through
    extra = 2


class TagInLine(admin.TabularInline):
    model = Recipe.tags.through
    extra = 2


@admin.register(RecipeTag)
class RecipetagAdmin(admin.ModelAdmin):
    list_display = ['id', 'recipe', 'tag']


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    search_fields = ['user__username', 'user__email']
    empty_value_display = '-пусто-'


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'measurement_unit']
    search_fields = ['name']
    empty_value_display = '-пусто-'


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'author', 'favorites']
    search_fields = ['name', 'author__username']
    list_filter = ['tags']
    empty_value_display = '-пусто-'
    inlines = (
        IngredientsInLine,
        TagInLine
    )

    def favorites(self, obj):
        return Favorite.objects.filter(recipe=obj).count()


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'recipe']
    search_fields = ['user__username', 'user__email']
    empty_value_display = '-пусто-'


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'color', 'slug']
    search_fields = ['name', 'slug']
    empty_value_display = '-пусто-'
