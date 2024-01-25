from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Фильтр по пользователям"""
    list_display = ('email', 'first_name', 'phone', 'is_active', 'role', 'pk')
    list_filter = ('role',)
