from rest_framework import serializers
from .models import Products,Category,Brand,Cart

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model=Brand
        fields='__all__'
     
class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields='__all__'
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'
      

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cart
        fields='__all__'             