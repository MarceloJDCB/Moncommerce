from typing import OrderedDict
from django.shortcuts import render, get_object_or_404
from collections import OrderedDict
from .models import Product
from .serializers import ProductSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status


def index(request):
    return render(request,'store/index.html',{'user':request.user,'last_products':Product.objects.all()[0:3]})

def product(request,product):
    return render(request,'store/product.html',{'user':request.user,'product':Product.objects.get(id=product)})
    

def products(request):
    return render(request,'store/products.html',{'products':Product.objects.all(), 'user':request.user})

class productsViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def retrieve(self, request, pk=None):
        product = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(product)
        response = {'name':product.name,
                    'description':product.description,
                    'price':product.price,
                    'image':product.frame_base64}
        return Response(response)
    
    def create(self, request):
        # create a new product
        super(productsViewset, self).create(request)
        response = {"response":"produto criado com sucesso!"}
        return Response(data=response,satus=status.HTTP_201_CREATED)
    
    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)


# Create your views here.
