from django.db import models
from django.contrib.auth.models import User


class Stock(models.Model):
    stock_symbol = models.CharField(max_length=6)
    company_name = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_creator = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.stock_symbol}: {self.company_name}"


class Buys(models.Model):
    stock_symbol = models.CharField(max_length=6)
    shares = models.IntegerField()
    share_price_bought = models.FloatField()
    bought_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.stock_symbol}, shares :{self.shares} at {self.bought_at}"


class Sells(models.Model):
    stock_symbol = models.CharField(max_length=6)
    shares = models.IntegerField()
    share_price_sold = models.FloatField()
    sold_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)