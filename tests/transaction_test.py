import unittest
from datetime import datetime
from models.transaction import Transaction
from models.merchant import Merchant
from models.tag import Tag

class TestTransaction(unittest.TestCase):

    def setUp(self):
        self.tag = Tag("Groceries")
        self.merchant = Merchant("ASDA")
        self.date_1 = datetime(2020,10,8,15,30,42)
        self.transaction = Transaction ("Groceries Week 42", 55.32, self.merchant, self.tag, self.date_1 )

    def test_transaction_has_name(self):
        self.assertEqual("Groceries Week 42",self.transaction.name)
    
    def test_transaction_has_price(self):
        self.assertEqual(55.32, self.transaction.price)
    
    def test_transaction_has_merchant(self):
        self.assertEqual(self.merchant, self.transaction.merchant)

    def test_transaction_has_tag(self):
        self.assertEqual(self.tag, self.transaction.tag)

    def test_transaction_has_timestamp(self):
        self.assertEqual(self.date_1, self.transaction.timestamp)    
    