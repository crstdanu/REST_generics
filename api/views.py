from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)

from myapp.models import Product
from .serializers import ProductSerializer


class ListCreateProductAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class RetrieveUpdateDestroyProductAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'

# class ListProductApiView(ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


# class CreateProductAPIView(CreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


# class RetrieveProductAPIView(RetrieveAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     lookup_field = 'id'


# class UpdateProductAPIView(UpdateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     lookup_field = 'id'


# class DestroyProductAPIView(DestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     lookup_field = 'id'
