from rest_framework import serializers
from .models import Stock, Buys, Sells, History


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "stock_symbol", "company_name")
        model = Stock
        ordering = ["-id"]


class BuysSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        fields = (
            "id",
            "stock_symbol",
            "shares",
            "share_price_bought",
            "bought_at",
            "owner",
        )
        model = Buys
        ordering = ["-id"]


class SellsSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        fields = (
            "id",
            "stock_symbol",
            "shares",
            "share_price_sold",
            "sold_at",
            "owner",
        )
        model = Sells
        ordering = ["-id"]


class HistorySerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        fields = (
            "id",
            "stock_symbol",
            "shares",
            "share_price",
            "transaction_type",
            "transaction_at",
            "owner",
        )
        model = History
        ordering = ["-id"]


class SummarySerializer(serializers.ModelSerializer):
    sum_shares = serializers.IntegerField()

    class Meta:
        fields = (
            "stock_symbol",
            "sum_shares",
        )
        model = History