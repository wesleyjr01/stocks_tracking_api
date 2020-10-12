from rest_framework import generics
from .models import Stock, Buys
from .serializers import StockSerializer, BuysSerializer
from .permissions import IsAdminOrReadOnly


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