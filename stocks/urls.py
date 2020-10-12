from django.urls import path
from .views import StockList, StockDetail, BuysList, BuysDetail, SellsList, SellsDetail

urlpatterns = [
    path("<int:pk>", StockDetail.as_view()),
    path("", StockList.as_view()),
    path("buys/<int:pk>/", BuysDetail.as_view()),
    path("buys/", BuysList.as_view()),
    path("sells/<int:pk>/", SellsDetail.as_view()),
    path("sells/", SellsList.as_view()),
]
