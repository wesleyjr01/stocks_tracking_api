from rest_framework import generics
from .models import Stock, Buys, Sells
from .serializers import StockSerializer, BuysSerializer, SellsSerializer
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
            serializer.save()


class SellsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sells.objects.all()
    serializer_class = SellsSerializer

    def get_queryset(self):
        user = self.request.user
        return Sells.objects.filter(owner=user)