from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import (
    StockViewSet,
    SellsViewSet,
    BuysViewSet,
    HistoryViewSet,
    SummaryViewSet,
)

router = SimpleRouter()
router.register("symbols", StockViewSet, basename="symbols")
router.register("buys", BuysViewSet, basename="buys")
router.register("sells", SellsViewSet, basename="sells")
router.register("history", HistoryViewSet, basename="history")
router.register("", SummaryViewSet, basename="summary")

urlpatterns = router.urls
