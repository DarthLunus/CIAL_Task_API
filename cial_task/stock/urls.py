from django.urls import path
from .views import StockDetailView

urlpatterns = [
    path('stock/<str:stock_symbol>/', StockDetailView.as_view()),
]
