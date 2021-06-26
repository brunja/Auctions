from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone

# User model
class User(AbstractUser):
    def __str__(self):
        return f"{self.username}"

#Category model
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Product model
class Item(models.Model):
    title = models.CharField(max_length=64, null=True)
    description = models.TextField()
    price = models.FloatField(validators=[MinValueValidator(0.01)], null=True)
    image = models.URLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_creator", null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    active = models.BooleanField(blank=False, default=True, null=True)
    date = models.DateTimeField(default=timezone.now, null=True)
    watchers = models.ManyToManyField(User, blank=True, related_name="watchlist")

    def __str__(self):
        return self.title
    
    def is_closed(self):
        if self.active:
            return False
        else:
            return True

#Bid Model
class Bid(models.Model):
    amount = models.FloatField(validators=[MinValueValidator(0.01)], null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    winner = models.BooleanField(default=False, null=True)

#Comment Model
class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
