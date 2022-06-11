from rest_framework import viewsets
from django_filters import FilterSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from products.api.serializers import ProductSerializer
from products.models import Product
from products.status import Status


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

    @action(detail=False, url_path='(?P<user_id>[^/.]+)/pendentes', methods=['get'])
    def pendents(self, request, **kwargs):
        user = kwargs.get('user_id')
        list_products = Product.objects.exclude(user_id_donor=user).filter(status=Status.OPEN.value)
        list_products_response = self.serializer_class(list_products, many=True)
        return Response(list_products_response.data, status=status.HTTP_200_OK)

    @action(detail=False, url_path='(?P<user_id>[^/.]+)/minhas-doacoes', methods=['get'])
    def myDonations(self, request, **kwargs):
        user = kwargs.get('user_id')
        list_products = Product.objects.filter(user_id_donor=user) | Product.objects.filter(user_id_recipient=user)
        list_products_response = self.serializer_class(list_products, many=True)
        return Response(list_products_response.data, status=status.HTTP_200_OK)
