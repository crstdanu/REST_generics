from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import ProductSerializer
from myapp.models import Product


@api_view(['GET', 'POST'])
def list_create_view(request):
    if request.method == 'GET':
        items = Product.objects.all()
        serializer = ProductSerializer(items, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', "DELETE"])
def retrieve_update_destroy(request, id):
    try:
        item = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(item, many=False)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProductSerializer(data=item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
