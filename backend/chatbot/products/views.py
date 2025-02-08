from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from products.serializers import ProductSerializer
from products.services import ProductService
from rest_framework.permissions import IsAuthenticated

class ProductViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    def list(self, request):
        products = ProductService.find_all()
        serializer = ProductSerializer(products, many=True)
        return Response({"products":serializer.data})

    def retrieve(self, request, pk=None):
        product = ProductService.find_by_id(pk)
        if product:
            serializer = ProductSerializer(product)
            return Response({"product":serializer.data})
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            product = ProductService.create_product(serializer.validated_data)
            return Response({'product':ProductSerializer(product).data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        product = ProductService.find_by_id(pk)
        if product:
            product = ProductService.update_product(product, request.data)
            return Response({'product':ProductSerializer(product).data})
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        product = ProductService.find_by_id(pk)
        if product:
            ProductService.delete_product(product)
            return Response({"message": "Product deleted"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
