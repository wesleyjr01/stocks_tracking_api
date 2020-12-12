from rest_framework.routers import DefaultRouter
from .views import (
    StockViewSet,
    SellsViewSet,
    BuysViewSet,
    HistoryViewSet,
    SummaryViewSet,
)

router = DefaultRouter()
router.register("symbols", StockViewSet, basename="symbols")
router.register("buys", BuysViewSet, basename="buys")
router.register("sells", SellsViewSet, basename="sells")
router.register("history", HistoryViewSet, basename="history")
router.register("summary", SummaryViewSet, basename="summary")

urlpatterns = router.urls
