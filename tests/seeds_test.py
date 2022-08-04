import unittest

from models.seeds import Seeds

class TestSeed(unittest.TestCase):
    def test_can_get_lists_of_given_length(self):
        new_list = Seeds.get_list_of_length(5)
        self.assertEqual(5, len(new_list))
