from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from django.conf import settings
# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique = True)
    profile_picture_url = models.URLField(blank = True, null = True)

    def __str__(self):
        return self.email

class Category(models.Model):
    name = models.CharField(max_length = 100)
    slug = models.SlugField(unique =  True, blank = True)
    image = models.ImageField(upload_to = "category_img", blank = True, null = True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs): #slugify the name and set it to unique_slug and make sure every slug is unique and it does not exist before, if it exists add a number to it to make it unique
        if not self.slug:
            self.slug = slugify(self.name)
            unique_slug = self.slug
            counter = 1
            if Product.objects.filter(slug = unique_slug).exists():
                unique_slug = f'{self.slug}-{counter}'
                counter += 1
            self.slug = unique_slug
        super().save(*args, **kwargs)     

class Product(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    slug = models.SlugField(unique = True, blank = True, null = True)
    image = models.ImageField(upload_to = "product_img", blank = True, null = True)
    featured = models.BooleanField(default = True)
    category = models.ForeignKey(Category, on_delete = models.SET_NULL, related_name = "products", blank = True, null = True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs): #slugify the name and set it to unique_slug and make sure every slug is unique and it does not exist before, if it exists add a number to it to make it unique
        if not self.slug:
            self.slug = slugify(self.name)
            unique_slug = self.slug
            counter = 1
            if Product.objects.filter(slug = unique_slug).exists():
                unique_slug = f'{self.slug}-{counter}'
                counter += 1
            self.slug = unique_slug
        super().save(*args, **kwargs)    

class Cart(models.Model):
    cart_code = models.CharField(max_length = 11, unique = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.cart_code

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete = models.CASCADE, related_name = "cartitems")
    product = models.ForeignKey(Product, on_delete= models.CASCADE, related_name = "item")
    quantity = models.IntegerField(default = 1)


    def __str__(self):
        return f"{self.quantity} x {self.product.name} in cart {self.cart.cart_code}"        

class Review(models.Model):
    RATING_CHOICES = [
        (1, '1 - Poor'),
        (2, '2 - Fair'),
        (3, '3 - Good'),
        (4, '4 - Very Good'),
        (5, '5 - Excellent'),
    ]
    product = models.ForeignKey(Product, on_delete = models.CASCADE, related_name = 'reviews')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = "reviews")
    rating = models.PositiveIntegerField(choices = RATING_CHOICES)
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f"{self.user.user}'s review on {self.product.name}"

    class Meta:
        unique_together = ["user", "product"] #a user can only have 1 review on 1 product
        ordering = ["-created"] #the last created review is going to come first      
