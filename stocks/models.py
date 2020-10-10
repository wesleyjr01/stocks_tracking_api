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