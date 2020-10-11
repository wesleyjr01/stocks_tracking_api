from rest_framework import generics, permissions
from .models import Stock
from .serializers import StockSerializer
from .permissions import IsAdminOrReadOnly


class StockList(generics.ListCreateAPIView):
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


class StockDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Stock.objects.all()
    serializer_class = StockSerializer