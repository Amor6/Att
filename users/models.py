from django.contrib.auth.models import AbstractUser
from django.db import models
from users.managers import UserManager
# from phonenumbers_field.modelfields import PhoneNumberField

NULLABLE = {'blank': True, 'null': True}


class UserRoles(models.TextChoices):
    """Статус пользователя"""

    USER = 'user'
    ADMIN = 'admin'


class User(AbstractUser):
    """Создание пользователя и то, что необходимо будет ввести при регистрации"""

    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', 'status']

    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    phone = models.IntegerField(verbose_name='Номер телефона', **NULLABLE)
    email = models.EmailField(unique=True, verbose_name='Электронная почта')
    image = models.ImageField(upload_to='users/avatars', verbose_name='Аватар', **NULLABLE)
    role = models.CharField(max_length=50, choices=UserRoles.choices, default=UserRoles.USER, verbose_name='Статус')
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
