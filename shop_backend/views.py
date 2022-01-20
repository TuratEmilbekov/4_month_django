from dataclasses import dataclass
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductListSerializer, ProductCreateSerializer, TagSerializer, ReviewListSerializer
from .models import Products, Tag, Review
from django.shortcuts import render

# Create your views here.
@api_view(['GET'])
def product_list_view(request):
    product = Products.objects.all()
    data = ProductListSerializer(product, many=True).data
    return Response(data=data)

@api_view(['GET', 'PUT', 'DELETE'])
def product_detail_view(request, id):
    try:
        product = Products.objects.get(id=id)
    except Products.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'error': 'Product not found!'})
    if request.method == 'GET':
        data = ProductListSerializer(product, many=False).data
        return Response(data=data)
    elif request.method == 'PUT':
        serializer = ProductCreateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
                                data={'message': 'error', 
                                    'errors': serializer.errors})
        product.title == request.data['title']
        product.description == request.data['description', '']
        product. price == request.data['price']
        product.category == request.data['category']
        product.tags.set(request.data['tags'])
        product.save()
        return Response(data={'message': 'Product update!'})
    elif request.method == 'DELETE':
        product.delete()
        return Response(data={'message': 'Product successfully removed!'})

@api_view(['GET'])
def get_review(request):
    review = Products.objects.all()
    data = ReviewListSerializer(review, many=True).data
    return Response(data=data)

@api_view(['GET'])
def get_tags(request):
    tags = Tag.objects.all()
    data = TagSerializer(tags.filter(is_active=True), many=True).data
    return Response(data=data)


