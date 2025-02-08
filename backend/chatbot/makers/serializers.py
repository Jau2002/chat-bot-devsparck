from rest_framework import serializers
from makers.models import Maker

class MakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maker
        fields = '__all__'