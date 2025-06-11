from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    get_image = serializers.SerializerMethodField()
    get_thumbnail = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "get_absolute_url",
            "description",
            "price",
            "get_image",
            "get_thumbnail"
        ]

    def get_get_image(self, obj):
        return obj.get_image()

    def get_get_thumbnail(self, obj):
        return obj.get_thumbnail()
