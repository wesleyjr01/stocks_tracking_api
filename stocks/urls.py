from django.urls import path
from .views import StockList, StockDetail, BuysList

urlpatterns = [
    path("<int:pk>", StockDetail.as_view()),
    path("", StockList.as_view()),
    path("buys/", BuysList.as_view()),
]
