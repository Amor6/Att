from django.urls import include, path
from rest_framework.routers import DefaultRouter
from partners.views import SupplierViewSet
from partners.apps import PartnersConfig

app_name = PartnersConfig.name

partners_router = DefaultRouter()
partners_router.register(r'Партёры', SupplierViewSet, basename='Партнёр')

urlpatterns = [
    path('', include(partners_router.urls)),
]
