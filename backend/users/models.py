from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    # !!! ЭТО КРИТИЧЕСКИЙ ФИКС ДЛЯ ПРОБЛЕМЫ "Reverse accessor clashes" !!!
    # Мы явно определяем эти поля с уникальными related_name,
    # чтобы избежать конфликтов с встроенной моделью User.
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="custom_user_groups", # Уникальное имя
        related_query_name="custom_user",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="custom_user_permissions", # Уникальное имя
        related_query_name="custom_user",
    )

    USERNAME_FIELD = 'username' # Или 'email', если хотите логин по почте
    REQUIRED_FIELDS = ['email'] # Поля, которые обязательны при создании через createsuperuser

    def __str__(self):
        return self.username