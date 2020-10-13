from django.urls import path
from .views import (
    StockList,
    StockDetail,
    BuysList,
    BuysDetail,
    SellsList,
    SellsDetail,
    HistoryList,
    SummaryList,
)

urlpatterns = [
    path("", SummaryList.as_view()),
    path("symbols/<int:pk>", StockDetail.as_view()),
    path("symbols/", StockList.as_view()),
    path("buys/<int:pk>/", BuysDetail.as_view()),
    path("buys/", BuysList.as_view()),
    path("sells/<int:pk>/", SellsDetail.as_view()),
    path("sells/", SellsList.as_view()),
    path("history/", HistoryList.as_view()),
]
