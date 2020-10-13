from rest_framework import generics
from .models import Stock, Buys, Sells, History
from .serializers import (
    StockSerializer,
    BuysSerializer,
    SellsSerializer,
    HistorySerializer,
)
from .permissions import IsAdminOrReadOnly
from rest_framework.exceptions import ValidationError


class StockList(generics.ListCreateAPIView):
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


class StockDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


class BuysList(generics.ListCreateAPIView):
    queryset = Buys.objects.all()
    serializer_class = BuysSerializer

    def get_queryset(self):
        user = self.request.user
        return Buys.objects.filter(owner=user)

    def perform_create(self, serializer):
        request_user = self.request.user
        request_stock_symbol = self.request.data["stock_symbol"]
        request_shares = int(self.request.data["shares"])
        request_share_price_bought = self.request.data["share_price_bought"]
        request_bought_at = self.request.data["bought_at"]

        # save register at buys database
        serializer.save()

        # save register at history database
        history_buys_register = History.objects.create(
            stock_symbol=request_stock_symbol,
            shares=request_shares,
            share_price=request_share_price_bought,
            transaction_type=History.TransactionType.BUY,
            transaction_at=request_bought_at,
            owner=request_user,
        )
        history_buys_register.save()


class BuysDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Buys.objects.all()
    serializer_class = BuysSerializer

    def get_queryset(self):
        user = self.request.user
        return Buys.objects.filter(owner=user)


class SellsList(generics.ListCreateAPIView):
    queryset = Sells.objects.all()
    serializer_class = SellsSerializer

    def get_queryset(self):
        user = self.request.user
        return Sells.objects.filter(owner=user)

    def perform_create(self, serializer):
        request_user = self.request.user
        request_stock_symbol = self.request.data["stock_symbol"]
        request_shares = int(self.request.data["shares"])
        request_share_price_sold = self.request.data["share_price_sold"]
        request_sold_at = self.request.data["sold_at"]

        stocks_bought = Buys.objects.filter(
            owner=request_user,
            stock_symbol=request_stock_symbol,
        )
        shares_bought = sum([f.shares for f in stocks_bought])

        stocks_sold = Sells.objects.filter(
            owner=request_user,
            stock_symbol=request_stock_symbol,
        )
        shares_sold = sum([f.shares for f in stocks_sold])

        current_shares = shares_bought - shares_sold
        if current_shares < 0:
            message = f"Negative shares balance for {request_stock_symbol}"
            raise ValidationError(message)
        elif current_shares < request_shares:
            message = f"Not enough {request_stock_symbol} to sell. Available: {current_shares}."
            raise ValidationError(message)
        else:
            # save register at sells database
            serializer.save()

            # save register at history database
            history_sell_register = History.objects.create(
                stock_symbol=request_stock_symbol,
                shares=-1 * (request_shares),
                share_price=request_share_price_sold,
                transaction_type=History.TransactionType.SELL,
                transaction_at=request_sold_at,
                owner=request_user,
            )
            history_sell_register.save()


class SellsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sells.objects.all()
    serializer_class = SellsSerializer

    def get_queryset(self):
        user = self.request.user
        return Sells.objects.filter(owner=user)


class HistoryList(generics.ListCreateAPIView):
    queryset = History.objects.all()
    serializer_class = HistorySerializer

    def get_queryset(self):
        user = self.request.user
        return History.objects.filter(owner=user)