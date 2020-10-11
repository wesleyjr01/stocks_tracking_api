from rest_framework import serializers
from .models import Stock


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "stock_symbol", "company_name")
        model = Stock