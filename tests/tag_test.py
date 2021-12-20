import unittest
from models.tag import Tag

class TestTag(unittest.TestCase):

    def setUp(self):
        self.tag_1 = Tag("Groceries")

    def test_tag_has_name(self):
        self.assertEqual("Groceries",self.tag_1.name)
    
    def test_tag_has_active(self):
        self.assertEqual(True, self.tag_1.active)
    
    def test_can_toggle_active(self):
        self.tag_1.toggle_active()
        self.assertEqual(False, self.tag_1.active)