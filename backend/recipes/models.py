from colorfield.fields import ColorField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import UniqueConstraint

from users.models import User


class Ingredient(models.Model):
    name = models.CharField(
        'Название',
        max_length=200,
        blank=False
    )
    measurement_unit = models.CharField(
        'Единица измерения',
        max_length=100
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'
        constraints = [
            UniqueConstraint(
                fields=['name', 'measurement_unit'],
                name='ingredient_name_unit_unique'
            )
        ]

    def __str__(self):
        return f'{self.name} в {self.measurement_unit}'


class Tag(models.Model):
    name = models.CharField(
        'Тэг',
        unique=True,
        max_length=200,
        blank=False
    )
    slug = models.SlugField(
        unique=True,
        blank=False,
        db_index=True
    )
    color = ColorField(
        'Цвет в HEX формате',
        default='#FF0000'
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class Recipe(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=False,
        related_name='recipes'
    )
    name = models.CharField(
        'Название рецепта',
        max_length=200,
        blank=False
    )
    image = models.ImageField(
        'Картинка',
        upload_to='recipes/',
        blank=True
    )
    text = models.TextField(
        'Описание рецепта',
        blank=False
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        through='IngredientInRecipe',
        blank=False
    )
    tags = models.ManyToManyField(
        Tag,
        through='RecipeTag',
        related_name='tags',
        blank=False
    )
    cooking_time = models.IntegerField(
        verbose_name='Время приготовления',
        blank=False,
        validators=[
            MinValueValidator(
                1,
                message='Время приготовления должно быть не менее 1 минуты!'
            ),
            MaxValueValidator(
                600,
                message='Время приготовления должно быть не более 600 минут!'
            )]
    )
    pub_date = models.DateField(
        'Дата публикации',
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        ordering = ['-pub_date']

    def __str__(self):
        return self.name


class IngredientInRecipe(models.Model):
    """ Модель связи ингредиента и рецепта. """

    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name='Рецепт'
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        verbose_name='Ингредиент'
    )
    amount = models.PositiveSmallIntegerField(
        'Количество',
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10000)
            ]
    )

    class Meta:
        verbose_name_plural = 'Ингредиенты в рецепте'
        constraints = [
            UniqueConstraint(
                fields=['recipe', 'ingredient'],
                name='recipe_ingredient_unique'
            )
        ]


class RecipeTag(models.Model):
    """ Модель связи тега и рецепта. """

    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name='Рецепт'
    )
    tag = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE,
        verbose_name='Тег'
    )

    class Meta:
        verbose_name_plural = 'Теги рецепта'
        constraints = [
            UniqueConstraint(
                fields=['recipe', 'tag'],
                name='recipe_tag_unique'
            )
        ]


class ShopingCartAndFavorite(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name='Рецепт',
    )

    class Meta:
        abstract = True
        verbose_name = 'Корзина и Избранное'
        constraints = [
            UniqueConstraint(
                fields=['user', 'recipe'],
                name='user_favorite_shoppingcart_unique'
            )
        ]


class Favorite(ShopingCartAndFavorite):

    class Meta:
        default_related_name = 'favorites'
        verbose_name = 'Избранный рецепт'
        verbose_name_plural = 'Избранные рецепты'


class ShoppingCart(ShopingCartAndFavorite):

    class Meta:
        default_related_name = 'shopping_cart'
        verbose_name = 'Рецепт в корзине'
        verbose_name_plural = 'Рецепты в корзине'
