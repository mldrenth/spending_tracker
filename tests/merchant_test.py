import unittest
from models.merchant import Merchant

class TestMerchant(unittest.TestCase):

    def setUp(self):
        self.merchant_1 = Merchant("Amazon")

    def test_merchant_has_name(self):
        self.assertEqual("Amazon",self.merchant_1.name)
    
    def test_merchant_has_active(self):
        self.assertEqual(True, self.merchant_1.active)
    
    def test_can_toggle_active(self):
        self.merchant_1.toggle_active()
        self.assertEqual(False, self.merchant_1.active)