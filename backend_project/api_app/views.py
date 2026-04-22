from django.shortcuts import render,get_object_or_404
from .serializers import ProductSerializer,OrderSerializer
from .models import ProductModel,OrderModel,OrderItem
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import viewsets

# Create your views here.

# Product List & create
class product_list(viewsets.ModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer

    
# Product update & delete
class product_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer



class order_list(viewsets.ModelViewSet):
    queryset = OrderModel.objects.all().prefetch_related('items__product')
    serializer_class = OrderSerializer

  
