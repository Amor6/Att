import django_filters
from partners.models import Partners


class SupplierFilter(django_filters.FilterSet):
    """Фильтр по городам, благодаря import django_filters"""
    city = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Partners
        fields = ['city']
