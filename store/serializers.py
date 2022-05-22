from rest_framework import serializers

from drf_extra_fields.fields import Base64ImageField
from .models import Product


class ProductSerializer(serializers.ModelSerializer):

    image = Base64ImageField(allow_empty_file=True, max_length=None, use_url=False, write_only=True, required=False)
    
    image_url = serializers.ReadOnlyField()

    class Meta:
        model = Product
        fields = '__all__'


