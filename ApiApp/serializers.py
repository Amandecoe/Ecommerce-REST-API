from rest_framework import serializers
from .models import Product, Category, CartItem, Cart

class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "slug", "image", "price"]

class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name","description", "slug", "image", "price"]        

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category        
        fields = ["id", "name", "image", "slug"]

class CategoryDetailSerializer(serializers.ModelSerializer):
    products = ProductListSerializer(many = True, read_only = True)  #there can be many products inside one category, and they are only listed(read_only)
    class Meta:
        model = Category        
        fields = ["id", "name", "image", "products"]

class CartItemSerializer(serializers.ModelSerializer):
    product =  ProductListSerializer(read_only = True) #refers to the product that is serialized
    sub_total = serializers.SerializerMethodField()
    #when using SerializerMethodField you are creating a read-only field on the serializer whose value comes from a custom method you define, instead of directly from the model
    class Meta:
        model = CartItem
        fields = [ "id", "product", "quantity", "sub_total"] 

    def get_sub_total(self, cartitem):        
        total = cartitem.product.price * cartitem.quantity
        return total  

class CartSerializer(serializers.ModelSerializer):
    CartItems = CartItemSerializer(read_only = True, many = True)
    cart_total = serializers.SerializerMethodField()
    class Meta:
        model = Cart
        fields = ["id", "cart_code", "CartItems", "cart_total"]    

    def get_cart_total(self, Cart):
        items = Cart.cartitems.all()
        total = (item.quantity * item.product.price for item in items)
        return total 


class CarStatSerializer(serializers.ModelSerializer):
    total_quantity = serializers.SerializerMethodField()
    class Meta:
        model = Cart
        fields = ["id", "cart_code", "total_quantity"]


        def get_total_quantity(self, Cart):
            items = Cart.CartItems.all()
            total = sum([item.quantity for item in items])
            return total