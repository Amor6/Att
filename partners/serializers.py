from rest_framework import serializers
from partners.models import Partners
from products.serializers import ProductSerializer


class SupplierSerializer(serializers.ModelSerializer):
    """Сериализатор партнёров"""

    author_first_name = serializers.CharField(source="author.first_name", read_only=True)
    author_last_name = serializers.CharField(source="author.last_name", read_only=True)
    product = ProductSerializer(many=True, required=False)
    part = serializers.SlugRelatedField(slug_field='title', queryset=Partners.objects.all())

    class Meta:
        model = Partners
        fields = "__all__"
