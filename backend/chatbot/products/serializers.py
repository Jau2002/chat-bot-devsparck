from rest_framework import serializers
from products.models import Product
from features.serializers import FeatureSerializer
from makers.serializers import MakerSerializer
from makers.models import Maker

class ProductSerializer(serializers.ModelSerializer):
    features = FeatureSerializer(many=True, read_only=True)  # Nested Features
    maker = MakerSerializer(read_only=True)  # Muestra el fabricante en detalle
    maker_id = serializers.PrimaryKeyRelatedField(
        queryset=Maker.objects.all(), source="maker", write_only=True
    ) 

    class Meta:
        model = Product
        fields = '__all__'