from rest_framework import serializers
from products.models import Product
from features.serializers import FeatureSerializer

class ProductSerializer(serializers.ModelSerializer):
    features = FeatureSerializer(many=True, read_only=True)  # Nested Features

    class Meta:
        model = Product
        fields = '__all__'