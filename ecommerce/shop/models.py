
# Create your models here.

from django.db import models

# Create your models here.
class Category(models.Model):
      name = models.CharField(max_length=100)
      description = models.CharField(max_length=100)
      image = models.ImageField(upload_to='images')

      def __str__(self):
         return self.name

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

class Products(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products')
    description = models.TextField(max_length=100)
    price = models.IntegerField()
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")



    def __str__(self):
        return self.name

from django.contrib.auth.models import AbstractUser
from random import randint

from random import randint
from secrets import randbelow

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
     phone = models.IntegerField()
     is_verified = models.BooleanField(default=False)
     otp = models.CharField(max_length=10,null=True,blank=True)


     def generate_otp(self):
         otp_number = int(str(randint(1000, 9999)) + str(self.id))
         self.otp=otp_number


         self.save()

