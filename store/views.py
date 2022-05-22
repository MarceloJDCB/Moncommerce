from math import prod
from django.shortcuts import render, get_object_or_404
from .models import Product
from .serializers import ProductSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from userapp.models import User


def index(request):
    return render(request,'store/index.html',{'user':request.user,'last_products':Product.objects.all()[0:10]})

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

class ProductAPIView(APIView):
    @api_view(('POST',))
    def buy_product(request):
        params = request.data
        user = User.objects.get(id=request.user.id)
        product = params['product']
        product = Product.objects.get(id=product)
        
        if product.supply > 0:
            if user.bananas > product.price:
                user.bananas = user.bananas - product.price
                product.supply -= 1
                product.save()
                user.save()
                return Response(data={"response":"produto comprado com sucesso"},status=status.HTTP_200_OK)
            else:
                return Response(data={"response":"você não tem bananas o suficiente para realizar está compra!"},status=status.HTTP_402_PAYMENT_REQUIRED)
        else:
            response = {"response":f"não temos {product.name} o suficiente em nosso estoque"}
            return Response(response=response,status=status.HTTP_400_BAD_REQUEST)
