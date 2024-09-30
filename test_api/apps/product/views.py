from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product
from  .serializers import ProductSerializer
# Create your views here.


class ProductView(APIView):
    def get(self, request):
        n = Product.objects.all()
        return Response({'products': ProductSerializer(n,many=True).data})

    def post(self,request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        product=Product.objects.create(
                name=serializer.validated_data['name'],
                price=serializer.validated_data['price'],
                description=serializer.validated_data['description'],
                quantity=serializer.validated_data['quantity'],
                is_active=serializer.validated_data['is_active'],
                created_at=serializer.validated_data['created_at']
        )
        return Response({'product': ProductSerializer(product).data})


#Методы
# GET - получить Данные
# POST- создать Данные отправить Данные
# PUT- изменить данные
# DELETE- удалить данные
# PATCH- изменить данные частично
# HEAD- получить заголовки
# OPTIONS- получить доступные методы