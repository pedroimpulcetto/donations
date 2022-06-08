from rest_framework import viewsets
from django_filters import FilterSet

from products.api.serializers import ProductSerializer
from products.models import Product


class ProductFilters(FilterSet):
    class Meta:
        model = Product
        fields = {
            'status': ['exact'],
            'user_id_donor': ['exact']
        }


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilters
