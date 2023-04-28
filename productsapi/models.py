from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser
# from django.utils.translation import gettext as _
# from .managers import CustomUserManager

# class CustomUser(AbstractUser):
#     email = models.EmailField(_('email address'), unique=True)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ('username',)

#     objects = CustomUserManager()

#     def __str__(self):
#         return self.email


class Profile(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # user = User.objects.create_user(username='johndoe', email='johndoe@example.com', password='mypassword')
    bio = models.TextField()
    avatar = models.ImageField(upload_to='avatars/')

    def __str__(self):
        return self.user.username
    
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
   
    

    def __str__(self):
        return self.name
class Brand(models.Model):
    name=models.CharField(max_length=200)
    country=models.CharField(default="india",max_length=200)
    website=models.URLField(default="url")
    
    def __str__(self):
        return self.name    
    
class Products(models.Model):
    
 name=models.CharField(verbose_name='Name of the products',max_length=200)
 mrp=models.IntegerField(verbose_name='MRP')
 selling_price=models.IntegerField()
 discount_percent = models.DecimalField(max_digits=4, decimal_places=2, default=0)
 qty=models.PositiveIntegerField(verbose_name='quantity')
 image_link=models.URLField()
 category=models.ForeignKey(Category,on_delete=models.CASCADE)
 color=models.CharField(max_length=20)
 brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
@property
def discounted_price(self):
        return self.price * (1 - (self.discount_percent / 100))
    
class Cart(models.Model):
    id=models.AutoField(primary_key=True)
    Products_id=models.ForeignKey(Products,on_delete=models.CASCADE)
    added_on=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.Products_id
             
    
        
    
    