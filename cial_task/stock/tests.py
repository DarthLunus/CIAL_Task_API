from django.test import TestCase
from rest_framework.test import APIClient
from .models import Stock


class Stocktests(TestCase):
    def setUp(self):
        self.client = APIClient()
        Stock.objects.create(
            status='active',
            purchased_amount=10,
            purchased_status='complete',
            request_data='2023-04-20',
            company_code='AAPL',
            company_name='Apple Inc',
            stock_values={'open': 150.0, 'high': 155.0, 'low': 149.0, 'close': 154.0},
            performance_data={'five_days': 2.0, 'one_month': 5.0, 'three_months': 10.0,
                              'year_to_date': 20.0, 'one_year': 30.0},
            competitors=[{'name': 'Google', 'market_cap': {'currency': 'USD', 'value': 1200.0}}],
        )

    def test_get_stock(self):
        response = self.client.get('/api/stock/AAPL/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['company_code'], 'AAPL')

    def test_post_stock(self):
        response = self.client.post
