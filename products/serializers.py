from rest_framework import serializers
from .models import Products

class ProductSeriliazer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    desc = serializers.CharField(max_length=500)
    price = serializers.IntegerField()
    inStock = serializers.BooleanField()
    image = serializers.CharField(max_length=1000)

    def create(self, validated_data):
        return Products.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.desc = validated_data.get('desc',instance.desc)
        instance.price = validated_data.get('price',instance.price)
        instance.inStock = validated_data.get('inStock',instance.inStock)
        instance.image = validated_data.get('image',instance.image)
        instance.save()
        return instance
        