# CIAL Stock API

This project is a web API that retrieves stock data from an external financial API (Polygon.io) and performs data scraping from the MarketWatch website. The application exposes two endpoints to access and update stock information.

## Requirements

- Python 3.10 or higher
- Docker
- Docker Compose

## Project Setup

### Cloning the Repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd <REPOSITORY_NAME>
```
## Setting Up Environment Variables
Create a .env file in the root of the project and add the following environment variables:

```env
POSTGRES_DB=your_db_name
POSTGRES_USER=your_db_user
POSTGRES_PASSWORD=your_db_password
DATABASE_URL=postgres://your_db_user:your_db_password@db:5432/your_db_name
```

## Building and Running the Project with Docker
1. Build and run the containers:

```bash
docker-compose up --build
```

2. The API will be available at http://localhost:8000.

## API Endpoints
## [GET] /stock/{stock_symbol}
Returns the stock data for the given symbol.

Example Request:

```bash
curl --request GET \
--url http://localhost:8000/stock/AAPL
```

Example Response:

```json
{
  "status": "active",
  "purchased_amount": 0,
  "purchased_status": "not_purchased",
  "request_data": "2023-07-27",
  "company_code": "AAPL",
  "company_name": "Apple Inc.",
  "stock_values": {
    "open": 150.00,
    "high": 155.00,
    "low": 149.00,
    "close": 154.00
  },
  "performance_data": {
    "five_days": 1.5,
    "one_month": 3.0,
    "three_months": 5.0,
    "year_to_date": 10.0,
    "one_year": 15.0
  },
  "competitors": [
    {
      "name": "Microsoft Corp.",
      "market_cap": {
        "currency": "USD",
        "value": 2000.00
      }
    }
  ]
}
```

## [POST] /stock/{stock_symbol}
Updates the purchased amount of the stock based on the received argument: “amount” (integer type).

Example Request:

```bash
curl --request POST \
--url http://localhost:8000/stock/AAPL \
--header 'Content-Type: application/json' \
--data '{"amount": 5}'
```

Example Response:

```json
{
  "message": "5 units of stock AAPL were added to your stock record"
}
```

## Project Structure

```plaitext
.
├── Dockerfile
├── docker-compose.yml
├── entrypoint.sh
├── manage.py
├── README.md
├── requirements.txt
├── stock_api
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── stocks
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── serializers.py
    ├── tests.py
    └── views.py
```

# Useful Commands
## Apply Migrations

```bash
docker-compose run web python manage.py migrate
```

Create Superuser

```bash
docker-compose run web python manage.py createsuperuser
```

Collect Static Files

```bash
docker-compose run web python manage.py collectstatic
```
