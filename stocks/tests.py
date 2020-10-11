from django.test import TestCase
from django.contrib.auth.models import User
from .models import Stock


class StockTests(TestCase):
    user_creator = "testuser1"
    password = "abc123"

    stock_symbol = "QWERT"
    company_name = "FLANGOS S.A."

    @classmethod
    def setUpTestData(cls):
        testuser1 = User.objects.create(
            username=cls.user_creator,
            password=cls.password,
        )
        testuser1.save()

        test_stock = Stock.objects.create(
            stock_symbol=cls.stock_symbol,
            company_name=cls.company_name,
            user_creator=testuser1,
        )
        test_stock.save()

    def test_stock_content(self):
        stock = Stock.objects.get(id=1)
        stock_symbol = f"{stock.stock_symbol}"
        company_name = f"{stock.company_name}"
        user_creator = f"{stock.user_creator}"
        self.assertEqual(stock_symbol, self.stock_symbol)
        self.assertEqual(company_name, self.company_name)
        self.assertEqual(user_creator, self.user_creator)