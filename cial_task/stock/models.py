from django.db import models


class Stock(models.Model):
    status = models.CharField(max_length=50)
    purchased_amount = models.IntegerField()
    purchased_status = models.CharField(max_length=50)
    request_data = models.DateField()
    company_code = models.CharField(max_length=10)
    company_name = models.CharField(max_length=100)
    stock_values = models.JSONField()
    performance_data = models.JSONField()
    competitors = models.JSONField()

    def __str__(self):
        return self.company_code
