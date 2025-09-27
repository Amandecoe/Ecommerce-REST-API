from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product, Category, Cart
from .serializers import ProductListSerializer, ProductDetailSerializer, CategoryListSerializer

# @api_view turns a normal django view function into a REST API endpoint 

@api_view(["GET"]) #this function will only support GET requests
def product_list(request):
    products = Product.objects.filter(featured=True)
    serializer = ProductListSerializer(products, many = True) #can have more than one products
    return Response(serializer.data)

@api_view(["GET"])
def product_detail(request, slug): #Gets each product with its #slug
    product = Product.objects.get(slug = slug)
    serializer = ProductDetailSerializer(product)
    return Response(serializer.data)

@api_view(["GET"])
def category_list(request):
    categories = Category.objects.all()
    serializer = CategoryListSerializer(categories, many = True)
    return Response(serializer.data)    

@api_view(["GET"])
def category_detail(request, slug):
    category = Category.objects.get(slug=slug)
    serializer = CategoryDetailSerializer(category)
    return Response(serializer.data)

@api_view(["POST"])
def add_to_cart(request): #request comes from the frontend when someone adds some product to cart
    cart_code = request.data.get("cart_code")
    product_id = request.data.get("product_id")      

    cart, created = Cart.objects.get_or_create(cart_code = cart_code) #retrieves the object if it exists or creates it if it doesn't
    product = Product.objects.get(id = product_id)
    cartitem, created =  CartItem.object.get_or_create(product = product, Cart = Cart)
    CartItem.quantity = 1
    CartItem.save()

    serializer = CartSerializer(Cart)
    return Response(serializer.data)