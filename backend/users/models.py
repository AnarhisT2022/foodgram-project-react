from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import UniqueConstraint
from rest_framework.exceptions import ValidationError

from .validators import validate_username

USER = 'user'
ADMIN = 'admin'

ROLES = [
    (USER, 'Пользователь'),
    (ADMIN, 'Админ'),
]


class User(AbstractUser):
    """Модель пользователя."""
    email = models.EmailField(
        max_length=254,
        unique=True,
        verbose_name='Почта',
    )
    username = models.CharField(
        max_length=150,
        blank=False,
        unique=True,
        verbose_name='Логин',
        validators=[validate_username]
    )
    first_name = models.CharField(
        max_length=150,
        blank=False,
        verbose_name='Имя',
    )
    last_name = models.CharField(
        max_length=150,
        blank=False,
        verbose_name='Фамилия',
    )
    password = models.CharField(
        max_length=150,
        blank=False,
        verbose_name='Пароль',
    )
    role = models.CharField(
        max_length=25,
        choices=ROLES,
        default=USER
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Subscription(models.Model):
    """ Модель подписок. """

    user = models.ForeignKey(
        User,
        related_name='follower',
        on_delete=models.CASCADE,
        verbose_name='Подписчик'
    )
    author = models.ForeignKey(
        User,
        related_name='author',
        on_delete=models.CASCADE,
        verbose_name='Автор'
    )

    def clean(self):
        if self.user == self.author:
            raise ValidationError(
                'Запрещено подписываться на себя'
            )

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        unique_together = ('user', 'author')
        constraints = [
            UniqueConstraint(
                fields=['user', 'author'],
                name='user_author_unique'
            )
        ]

    def __str__(self):
        return f'Пользователь {self.user} подписался на {self.author}'
