from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q
from django.contrib.auth import get_user_model
from .models import Product, Category, Cart, CartItem, Review, Wishlist
from .serializers import ProductListSerializer, ProductDetailSerializer, CategoryListSerializer, CartSerializer, CartItemSerializer, ReviewSerializer, WishlistSerializer

User =  get_user_model()
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
    cartitem, created =  CartItem.objects.get_or_create(product = product, cart = cart)
    cartitem.quantity = 1
    cartitem.save()

    serializer = CartSerializer(cart)
    return Response(serializer.data)

@api_view(['PUT'])
def update_cartitem_quantity(request):
   cartitem_id = request.data.get('item_id')
   quantity = request.data.get("quantity")

   quantity = int(quantity) 
   cartitem = CartItem.objects.get(id = cartitem_id)
   cartitem.quantity = quantity
   cartitem.save()

   serializer =  CartItemSerializer(cartitem)     
   return Response({"data": serializer.data, "message": "CartItem Updated Successfully"})

@api_view(['POST'])
def add_review(request):
    product_id = request.data.get("product_id")
    email = request.data.get("email")   
    rating = request.data.get("rating")
    review_text = request.data.get("review")

    product = Product.objects.get( id =  product_id)
    user = User.objects.get(email = email)

    if Review.objects.filter(product=product, user=user).exists(): #gives the you have reviewed it response if the product have been reviewed
        return Response("You have already Reviewed This Product")

    review = Review.objects.create(product=product, user=user, rating=rating, review=review_text)
    serializer = ReviewSerializer(review)
    return Response(serializer.data)

@api_view(['PUT'])
def update_review(request,pk):
    review = Review.objects.get(id = pk)
    rating = request.data.get("rating")
    review_text = request.data.get("review")

    review.rating = rating
    review.review = review_text
    review.save()

    serializer = ReviewSerializer(review)
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_review(request, pk):
    review =  Review.objects.get(id=pk)
    review.delete()

    return Response("Review Deleted Sucessfully")        

@api_view(['POST'])
def add_to_wishlist(request):
    email = request.data.get("email")
    product_id = request.data.get("product_id")

    user = User.objects.get(email = email)
    product = Product.objects.get(id = product_id)

    wishlist =  Wishlist.objects.filter(user = user, product = product)    
    if wishlist:
        wishlist.delete()
        return Response("Wishlist deleted sucessfully", status = 204)

    new_wishlist = Wishlist.objects.create(user= user, product = product)
    serializer = WishlistSerializer(new_wishlist)
    return Response(serializer.data)    

@api_view(['DELETE'])
def delete_cartitem(request, pk):
    cartitem = CartItem.objects.get(id=pk)
    cartitem.delete()

    return Response("Cart Item Deleted Sucessfully")        
   
@api_view(['GET'])
def product_search(request):
    query = request.query_params.get("query")
    if not query:
        return Response("No Query Provided", status=400)

    products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query) | Q(category__name__icontains = query)) #Q is a django built in feature which helps us to search 

    serializer = ProductListSerializer(products, many = True) #can return many products that match the search
    return Response(serializer.data)
