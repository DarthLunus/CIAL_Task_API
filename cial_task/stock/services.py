import requests
from bs4 import BeautifulSoup


def get_stock_data(stock_symbol, date):
    api_key = 'bmN7i7CrzrpKqFvgbB1fEaztCwZKSUjJ'
    url = f'https://api.polygon.io/v1/open-close/{stock_symbol}/{date}'
    headers = {
        'Authorization': f'Bearer {api_key}'
    }
    response = requests.get(url, headers=headers)
    return response.json()


def scrape_marketwatch(stock_symbol):
    url = f'https://www.marketwatch.com/investing/stock/{stock_symbol}'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    performance_data = {
        'five_days': parse_float(soup.select_one('.performance .five-days').text),
        'one_month': parse_float(soup.select_one('.performance .one-month').text),
        'three_months': parse_float(soup.select_one('.performance .three-months').text),
        'year_to_date': parse_float(soup.select_one('.performance .year-to-date').text),
        'one_year': parse_float(soup.select_one('.performance .one-year').text),
    }

    competitors = []
    competitors_section = soup.select('.competitors .table .row')
    for row in competitors_section:
        competitors.append({
            'name': row.select_one('.name').text,
            'market_cap': {
                'currency': 'USD',
                'value': parse_float(row.select_one('.market-cap').text),
            },
        })

    return performance_data, competitors


def parse_float(value):
    try:
        return float(value.replace(',', '').replace('%', '').replace('$', ''))
    except ValueError:
        return None
