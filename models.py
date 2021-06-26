from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone

# User model
class User(AbstractUser):
    pass

#Category model
class Category(models.Model):
    name = models.CharField(max_length=50)

# Product model
class Item(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.URLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category", default=5)
    active = models.BooleanField(blank=False, default=True)
    date = models.DateTimeField(default=timezone.now)

#Bid Model
class Bid(models.Model):
    amount = models.FloatField(validators=[MinValueValidator(1)])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE,)
    winner = models.BooleanField(default=False)

#Comment Model
class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

#WatchList model
class WatchList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
