from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Stock
from .services import get_stock_data, scrape_marketwatch
from django.utils.dateparse import parse_date
from django.core.cache import cache


class StockDetailView(APIView):
    @staticmethod
    def get(stock_symbol):
        stock = Stock.objects.filter(company_code=stock_symbol).first()
        if not stock:
            stock_data = get_stock_data(stock_symbol, 'latest')
            performance_data, competitors = scrape_marketwatch(stock_symbol)
            stock = Stock.objects.create(
                status=stock_data.get('status', ''),
                purchased_amount=0,
                purchased_status='',
                request_data=parse_date(stock_data.get('date', '')),
                company_code=stock_symbol,
                company_name=stock_data.get('companyName', ''),
                stock_values={
                    'open': stock_data.get('open', 0.0),
                    'high': stock_data.get('high', 0.0),
                    'low': stock_data.get('low', 0.0),
                    'close': stock_data.get('close', 0.0),
                },
                performance_data=performance_data,
                competitors=competitors,
            )
        return Response({
            'status': stock.status,
            'purchased_amount': stock.purchased_amount,
            'purchased_status': stock.purchased_status,
            'request_data': stock.request_data,
            'company_code': stock.company_code,
            'company_name': stock.company_name,
            'stock_values': stock.stock_values,
            'performance_data': stock.performance_data,
            'competitors': stock.competitors,
        }, status=status.HTTP_200_OK)

    @staticmethod
    def post(request, stock_symbol):
        stock = Stock.objects.filter(company_code=stock_symbol).first()
        if not stock:
            return Response({'error': 'Stock not found.'}, status=status.HTTP_404_NOT_FOUND)

        amount = request.data.get('amount')
        if not amount:
            return Response({'error': 'Amount is required.'}, status=status.HTTP_400_BAD_REQUEST)

        stock.purchased_amount += amount
        stock.save()
        return Response({
            'message': f'{amount} units of stock {stock_symbol} were added to your stock record'
        }, status=status.HTTP_201_CREATED)


class Stockdetailview(APIView):
    @staticmethod
    def get(stock_symbol):
        cached_stock = cache.get(stock_symbol)
        if cached_stock:
            return Response(cached_stock, status=status.HTTP_200_OK)

        cache.set(stock_symbol, stock_data, timeout=60 * 60)
        return Response(stock_data, status=status.HTTP_200_OK)
