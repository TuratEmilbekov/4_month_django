from turtle import title
from django.forms import CharField
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import *

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'

        
class ProductListSerializer(serializers.ModelSerializer):
    reviews = ''
    class Meta:
        model = Products
        # fields = '__all__'
        fields = ['id', 'title', 'tags', 'reviews']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ProductCreateSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=23)
    description = serializers.CharField(required=False)
    price = serializers.FloatField()
    category = serializers.IntegerField()
    tags = serializers.ListField()

    # def validate_name(self, name):
    #     products = Products.objects.filter(name=name)
    #     if products:
    #         raise ValidationError('Product already exist!')
    #     return name

    def validate(self, attrs):
        title = attrs['title']
        products = Products.objects.filter(title=title)
        if products:
            raise ValidationError('Produc already exist!')