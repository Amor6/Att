from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404
from users.models import User
from partners.models import Partners
from products.permissions import IsAdmin, IsOwner
from partners.serializers import SupplierSerializer
from partners.filters import SupplierFilter
from django_filters.rest_framework import DjangoFilterBackend


class SupplierViewSet(viewsets.ModelViewSet):
    """Партнёрский View"""
    queryset = Partners.objects.all()
    serializer_class = SupplierSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = SupplierFilter

    def get_permissions(self):
        """
        Права доступа и их возможности.
        Инкогнтито(не авторизованный):
        - видит список поставщиков.

        Прошедший регистрацию пользователь :
        - видит список поставщиков,
        - видит одного поставщика (детально),
        - создаёт поставщиков поставщиков,
        - редактирует своих поставщиков,
        - удаляет своих поставщиков.

        Админитсратор:
        - видит список поставщиков,
        - видит одного поставщика (детально),
        - создаёт поставщиков,
        - редактирует своих и чужих поставщиков,
        - удалет своих и чужих поставщиков.
        """

        if self.action == 'retrieve':
            permission_classes = [IsAuthenticated]
        elif self.action == 'create':
            permission_classes = [IsAuthenticated]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated, IsOwner | IsAdmin]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        """Создание продукта и отображение партнёра"""
        partner = serializer.save()
        partner.author = get_object_or_404(User, id=self.request.user.id)
        partner.save()
