from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# Create your models here.

class CommonInf(models.Model):
    stock = models.CharField(default="in_stock",choices=[("in_stock","In Stock"),("no_stock","no Stock")],max_length=10)
    created_at = models.DateField(default=timezone.now)
    published_at = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True

class User(AbstractUser,CommonInf):
    stock = None
    user_type = models.CharField(default="author",choices=[("author","Author"),("customer","Customer")],max_length=8)


class Book(CommonInf):
    book_name = models.CharField(max_length=100)
    book_title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    quantity = models.PositiveIntegerField()
    author = models.OneToOneField(User,on_delete=models.CASCADE,related_name="books",limit_choices_to={"user_type":"author"})


    
