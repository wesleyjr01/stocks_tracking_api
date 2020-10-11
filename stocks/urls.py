from django.urls import path
from .views import StockList, StockDetail

urlpatterns = [
    path("<int:pk>", StockDetail.as_view()),
    path("", StockList.as_view()),
]
