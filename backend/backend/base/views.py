from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from base.models import Product
from base.serializers import ProductSerializer


@api_view(["GET"])
def check_health(request):
    return Response({"status": "ok"}, status=status.HTTP_200_OK)


@api_view(["GET", "POST"])
def get_or_create_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_product(request, pk):
    try:
        product = Product.objects.get(_id=pk)
    except Product.DoesNotExist:
        return Response(
            {"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND
        )

    serializer = ProductSerializer(product)
    return Response(serializer.data, status=status.HTTP_200_OK)
