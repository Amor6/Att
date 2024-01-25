from django.contrib import admin
from partners.models import Partners


@admin.register(Partners)
class SupplierAdmin(admin.ModelAdmin):
    """Отображение поставщика в админке.
    Фильтрация по статусу,названию продукта
    Поиск по продукту, строне"""

    list_display = ('pk', 'author', 'title', 'levels', 'country', 'city', 'debt', 'created_at')
    list_filter = ('levels', 'title', 'product', 'country',)
    search_fields = ('levels', 'product', 'country')
    actions = ['cleanup_debt']

    def cleanup_debt(self, request, queryset):
        """Очистить задолжность"""

        for supply_object in queryset:
            supply_object.debt = 0
            supply_object.save()
        self.message_user(request, f'Задолжность очищена(у выбраного постовщека)')

    cleanup_debt.short_description = 'Очистить задолженность'
