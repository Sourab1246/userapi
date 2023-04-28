from django.shortcuts import render
from .models import Products,Category,Brand,Cart
from .serializers import BrandSerializer,CategorySerializer,ProductsSerializer,CartSerializer
from django.http import HttpResponse,JsonResponse
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.
class  BrandList(APIView):
    def get(self,request):
        
        brands=Brand.objects.all()
        serializer=BrandSerializer(brands,many=True)
        return JsonResponse(serializer.data,safe=False)
    
    def post(self,request):
        serializer=BrandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class  ProductsList(APIView):
    def get(self,request):
        
        products=Products.objects.all()
        serializer=ProductsSerializer(products,many=True)
        return JsonResponse(serializer.data,safe=False)
    
    def post(self,request):
        serializer=ProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProductsDetails(APIView):
    def get_object(self,id):
        try:
            return Products.objects.get(id=id)
        except Products.DoesNotExist:
            return JsonResponse(status=status.HTTP_404_NOT_FOUND)
      
    def get(self,request,id):
        products=self.get_object(id) 
        serializer=ProductsSerializer(products)
        return JsonResponse(serializer.data)
    def put(self,request,id):
        products=self.get_object(id) 
        serializer=ProductsSerializer(products,data=request.data)
        if serializer.is_valid():
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        products=self.get_object(id)
        products.delete
        return JsonResponse(status=status.HTTP_204_NO_CONTENT)
    
    # BRANDS DETAILS
class BrandDetails(APIView):
    def get_object(self,id):
        try:
            return Brand.object.get(id=id)
        except Brand.DoesNotExist:
            return JsonResponse(status=status.HTTP_404_NOT_FOUND)
      
    def get(self,request,id):
        brands=self.get_object(id) 
        serializer=BrandSerializer(brands)
        return JsonResponse(serializer.data)
    def put(self,request,id):
        brands=self.get_object(id) 
        serializer=ProductsSerializer(brands,data=request.data)
        if serializer.is_valid():
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        products=self.get_object(id)
        products.delete
        return JsonResponse(status=status.HTTP_204_NO_CONTENT)    
    
class Cart_details(APIView):
    def get(self,request):
        cart=Cart.objects.all()
        serializer=CartSerializer(cart,many=True)
        return JsonResponse(serializer.data,safe=False)
    def post(self,request):
        serializer=CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
        
            
        
            
     
        
                